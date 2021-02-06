"""
Generate data for modeling.

Written by Ed Oughton.

Winter 2020

"""
import os
import csv
import configparser
import pandas as pd
import geopandas
from collections import OrderedDict

from options import OPTIONS, TELECOM_CIRCLE_PARAMETERS, generate_policy_options
from india5g.demand import estimate_demand
from india5g.supply import estimate_supply
from india5g.assess import assess

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.join(os.path.dirname(__file__), 'script_config.ini'))
BASE_PATH = CONFIG['file_locations']['base_path']

DATA_RAW = os.path.join(BASE_PATH, 'raw')
DATA_INTERMEDIATE = os.path.join(BASE_PATH, 'intermediate')
DATA_PROCESSED = os.path.join(BASE_PATH, 'processed')


def load_regions(path, telecom_circle):
    """
    Load country regions.

    """
    regions = pd.read_csv(path)

    regions['tc_code'] = telecom_circle['tc_code']
    regions['geotype'] = regions.apply(define_geotype, axis=1)

    regions = regions.dropna(subset = ['population'])

    return regions


def define_geotype(x):
    """
    Allocate geotype given a specific population density.

    """
    if x['population_km2'] > 5000:
        return 'urban'
    elif x['population_km2'] > 1500:
        return 'suburban 1'
    elif x['population_km2'] > 1000:
        return 'suburban 2'
    elif x['population_km2'] > 500:
        return 'rural 1'
    elif x['population_km2'] > 100:
        return 'rural 2'
    elif x['population_km2'] > 50:
        return 'rural 3'
    elif x['population_km2'] > 10:
        return 'rural 4'
    else:
        return 'rural 5'


def read_capacity_lookup(path):
    """

    """
    capacity_lookup_table = {}

    with open(path, 'r') as capacity_lookup_file:
        reader = csv.DictReader(capacity_lookup_file)
        for row in reader:

            if float(row["capacity_mbps_km2"]) <= 0:
                continue
            environment = row["environment"].lower()
            ant_type = row["ant_type"]
            frequency_GHz = str(int(float(row["frequency_GHz"]) * 1e3))
            generation = str(row["generation"])
            ci = str(row['confidence_interval'])

            if (environment, ant_type, frequency_GHz, generation, ci) \
                not in capacity_lookup_table:
                capacity_lookup_table[(
                    environment, ant_type, frequency_GHz, generation, ci)
                    ] = []

            capacity_lookup_table[(
                environment,
                ant_type,
                frequency_GHz,
                generation,
                ci)].append((
                    float(row["sites_per_km2"]),
                    float(row["capacity_mbps_km2"])
                ))

        for key, value_list in capacity_lookup_table.items():
            value_list.sort(key=lambda tup: tup[0])

    return capacity_lookup_table


def lookup_cost(lookup, strategy, environment):
    """
    Find cost of network.

    """
    if (strategy, environment) not in lookup:
        raise KeyError("Combination %s not found in lookup table",
                       (strategy, environment))

    density_capacities = lookup[
        (strategy, environment)
    ]

    return density_capacities


def load_penetration(path):
    """
    Load penetration forecast.

    """
    output = {}

    with open(path, 'r') as source:
        reader = csv.DictReader(source)
        for row in reader:
            output[int(row['year'])] = float(row['penetration'])

    return output


def load_smartphones(country, path):
    """
    Load phone types forecast. The function either uses the specific data
    for the country being modeled, or data from another country in the same
    cluster. If no data are present for the country of the cluster, it
    defaults to the mean values across all surveyed countries.
    """
    output = {}
    settlement_types = [
        'urban',
        'rural']

    for settlement_type in settlement_types:
        with open(path, 'r') as source:
            reader = csv.DictReader(source)
            intermediate = {}
            for row in reader:
                if settlement_type == row['settlement_type']:
                    intermediate[int(row['year'])] = float(row['penetration'])
            output[settlement_type] = intermediate

    return output


def load_core_lut(path):
    """

    """
    interim = []

    with open(path, 'r') as source:
        reader = csv.DictReader(source)
        for row in reader:
            interim.append({
                'GID_id': row['GID_id'],
                'asset': row['asset'],
                'source': row['source'],
                'value': int(round(float(row['value']))),
            })

    asset_types = [
        'core_edge',
        'core_node',
        'regional_edge',
        'regional_node'
    ]

    output = {}

    for asset_type in asset_types:
        asset_dict = {}
        for row in interim:
            if asset_type == row['asset']:
                combined_key = '{}_{}'.format(row['GID_id'], row['source'])
                asset_dict[combined_key] = row['value']
                output[asset_type] = asset_dict

    return output


def define_deciles(regions):

    # regions = regions.drop(regions[regions['tc_code'] == 'MU'].index)

    regions = regions.sort_values(by='population_km2', ascending=True)

    regions['decile'] = regions.groupby([
        'GID_0', 'scenario', 'strategy', 'confidence'], as_index=True).population_km2.apply(
            pd.qcut, q=11, precision=0,
            #[0,10,20,30,40,50,60,70,80,90,100]
            labels=[100,90,80,70,60,50,40,30,20,10,0], duplicates='drop')

    return regions


def write_mno_demand(regional_annual_demand, folder, metric, path):
    """
    Write all annual demand results for a single hypothetical Mobile
    Network Operator (MNO).

    """
    print('Writing annual_demand')
    regional_annual_demand = pd.DataFrame(regional_annual_demand)
    regional_annual_demand = define_deciles(regional_annual_demand)
    regional_annual_demand.to_csv(path, index=False)


def write_results(regional_results, folder, metric):
    """
    Write all results.

    """
    print('Writing national results')
    national_results = pd.DataFrame(regional_results)

    national_results = national_results[[
        'GID_0', 'scenario', 'strategy', 'confidence', 'population', 'area_km2',
        'population_km2', 'mno_phones_on_network', 'mno_smartphones_on_network',
        'sites_estimated_total', 'existing_network_sites', 'upgraded_sites', 'new_sites',
        'total_revenue', 'total_cost', 'cost_per_sp_user','spectrum_cost'
    ]]

    national_results = national_results.groupby([
        'GID_0', 'scenario', 'strategy', 'confidence'], as_index=True).sum()
    national_results['cost_per_network_user'] = (
        national_results['total_cost'] / national_results['mno_phones_on_network'])

    path = os.path.join(folder,'national_results_{}.csv'.format(metric))
    national_results.to_csv(path, index=True)

    print('Writing national cost composition results')
    national_cost_results = pd.DataFrame(regional_results)
    national_cost_results = national_cost_results[[
        'GID_0', 'scenario', 'strategy', 'confidence', 'population', 'population_km2',
        'mno_phones_on_network', 'cost_per_sp_user',
        'total_revenue', 'ran', 'backhaul_fronthaul', 'civils', 'core_network',
        'ops_and_acquisition',
        'spectrum_cost', 'tax', 'profit_margin', 'total_cost',
        'available_cross_subsidy', 'deficit', 'used_cross_subsidy',
        'required_state_subsidy',
    ]]

    national_cost_results = national_cost_results.groupby([
        'GID_0', 'scenario', 'strategy', 'confidence'], as_index=True).sum()
    national_cost_results['cost_per_network_user'] = (
        national_cost_results['total_cost'] / national_cost_results['mno_phones_on_network'])

    path = os.path.join(folder,'national_cost_results_{}.csv'.format(metric))
    national_cost_results.to_csv(path, index=True)

    print('Writing decile results')
    decile_results = pd.DataFrame(regional_results)
    decile_results = define_deciles(decile_results)
    decile_results = decile_results[[ #'tc_code',
        'scenario', 'strategy', 'decile', 'confidence', #
        'population', 'area_km2', #'population_km2',
        'total_population_with_phones', #'total_phone_density_km2',
        'mno_phones_on_network', #'mno_phone_density_on_network_km2',
        'total_population_with_smartphones', #'total_sp_density_km2',
        'mno_smartphones_on_network', #'mno_sp_density_on_network_km2',
        'sites_estimated_total', 'existing_network_sites', 'upgraded_sites', 'new_sites',
        'total_revenue', 'total_cost', #'cost_per_sp_user',
    ]]
    decile_results = decile_results.groupby([ #'tc_code',
        'scenario', 'strategy', 'confidence', 'decile'], as_index=True).sum() #'tc_code',

    decile_results['population_km2'] = (
        decile_results['population'] / decile_results['area_km2'])
    decile_results['total_phone_density_km2'] = (
        decile_results['total_population_with_phones'] / decile_results['area_km2'])
    decile_results['total_sp_density_km2'] = (
        decile_results['total_population_with_smartphones'] / decile_results['area_km2'])
    decile_results['mno_phone_density_on_network_km2'] = (
        decile_results['mno_phones_on_network'] / decile_results['area_km2'])
    decile_results['mno_sp_density_on_network_km2'] = (
        decile_results['mno_smartphones_on_network'] / decile_results['area_km2'])
    decile_results['sites_estimated_total_km2'] = (
        decile_results['sites_estimated_total'] / decile_results['area_km2'])
    decile_results['existing_network_sites_km2'] = (
        decile_results['existing_network_sites'] / decile_results['area_km2'])
    decile_results['cost_per_network_user'] = (
        decile_results['total_cost'] / decile_results['mno_phones_on_network'])
    decile_results['cost_per_sp_user'] = (
        decile_results['total_cost'] / decile_results['mno_smartphones_on_network'])

    path = os.path.join(folder,'decile_results_{}.csv'.format(metric))
    decile_results.to_csv(path, index=True)

    print('Writing decile cost results')
    decile_cost_results = pd.DataFrame(regional_results)
    decile_cost_results = define_deciles(decile_cost_results)
    decile_cost_results = decile_cost_results[[
        'scenario', 'strategy', 'decile', 'confidence', #'tc_code',
        'population', 'area_km2', #'population_km2',
        'mno_phones_on_network', 'mno_smartphones_on_network',#'cost_per_sp_user',
        'total_revenue', 'ran', 'backhaul_fronthaul', 'civils', 'core_network',
        'ops_and_acquisition', 'spectrum_cost', 'tax', 'profit_margin', 'total_cost',
        'available_cross_subsidy', 'deficit', 'used_cross_subsidy',
        'required_state_subsidy',
    ]]

    decile_cost_results = decile_cost_results.groupby([
        'scenario', 'strategy', 'confidence', 'decile'], as_index=True).sum() #'tc_code',
    decile_cost_results['cost_per_network_user'] = (
        decile_cost_results['total_cost'] / decile_cost_results['mno_phones_on_network'])
    decile_cost_results['cost_per_sp_user'] = (
        decile_cost_results['total_cost'] / decile_cost_results['mno_smartphones_on_network'])

    path = os.path.join(folder,'decile_cost_results_{}.csv'.format(metric))
    decile_cost_results.to_csv(path, index=True)

    print('Writing telecom circle results')
    tc_results = pd.DataFrame(regional_results)
    tc_results = tc_results[[
        'tc_code', 'scenario', 'strategy', 'confidence', 'population', 'area_km2',
        'population_km2', 'mno_phones_on_network', 'mno_smartphones_on_network',
        'sites_estimated_total', 'existing_network_sites', 'upgraded_sites', 'new_sites',
        'total_revenue', 'total_cost', 'cost_per_sp_user',
    ]]

    tc_results = tc_results.groupby([
        'tc_code', 'scenario', 'strategy', 'confidence'], as_index=True).sum()
    tc_results['cost_per_network_user'] = (
        tc_results['total_cost'] / tc_results['mno_phones_on_network'])

    path = os.path.join(folder,'tc_results_{}.csv'.format(metric))
    tc_results.to_csv(path, index=True)

    print('Writing telecom circle cost composition results')
    tc_results_cost_results = pd.DataFrame(regional_results)
    tc_results_cost_results = tc_results_cost_results[[
        'tc_code', 'scenario', 'strategy', 'confidence', 'population', 'population_km2',
        'mno_phones_on_network', 'cost_per_sp_user',
        'total_revenue', 'ran', 'backhaul_fronthaul', 'civils', 'core_network',
        'ops_and_acquisition',
        'spectrum_cost', 'tax', 'profit_margin', 'total_cost',
        'available_cross_subsidy', 'deficit', 'used_cross_subsidy',
        'required_state_subsidy',
    ]]

    tc_results_cost_results = tc_results_cost_results.groupby([
        'tc_code', 'scenario', 'strategy', 'confidence'], as_index=True).sum()
    tc_results_cost_results['cost_per_network_user'] = (
        tc_results_cost_results['total_cost'] / tc_results_cost_results['mno_phones_on_network'])

    path = os.path.join(folder,'tc_results_cost_results_{}.csv'.format(metric))
    tc_results_cost_results.to_csv(path, index=True)

    print('Writing regional results')
    regional_results = pd.DataFrame(regional_results)
    regional_results = define_deciles(regional_results)
    regional_results = regional_results[[
        'tc_code', 'GID_id', 'scenario', 'strategy', 'decile', #'tc_code',
        'confidence', 'population', 'area_km2', #'population_km2',
        'mno_phones_on_network', 'cost_per_sp_user',
        'upgraded_sites','new_sites', 'total_revenue', 'total_cost',
    ]]
    regional_results['cost_per_network_user'] = (
        regional_results['total_cost'] / regional_results['mno_phones_on_network'])

    path = os.path.join(folder,'regional_results_{}.csv'.format(metric))
    regional_results.to_csv(path, index=True)


def allocate_deciles(data):
    """
    Convert to pandas df, define deciles, and then return as a list of dicts.

    """
    data = pd.DataFrame(data)

    data = define_deciles(data)

    data = data.to_dict('records')

    return data


if __name__ == '__main__':

    BASE_YEAR = 2020
    END_YEAR = 2030
    TIMESTEP_INCREMENT = 1
    TIMESTEPS = [t for t in range(BASE_YEAR, END_YEAR + 1, TIMESTEP_INCREMENT)]

    COSTS = {
        #all costs in $USD
        'single_sector_antenna': 1500,
        'single_remote_radio_unit': 3500,
        'io_fronthaul': 1500,
        'processing': 1500,
        'io_s1_x2': 1500,
        'control_unit': 2000,
        'cooling_fans': 250,
        'distributed_power_supply_converter': 250,
        'power_generator_battery_system': 10000,
        'bbu_cabinet': 200,
        'tower': 5000,
        'civil_materials': 5000,
        'transportation': 5000,
        'installation': 5000,
        'site_rental_urban': 15000,
        'site_rental_suburban': 5000,
        'site_rental_rural': 1000,
        'router': 2000,
        'wireless_small': 20000,
        'wireless_medium': 30000,
        'wireless_large': 60000,
        'fiber_urban_m': 20,
        'fiber_suburban_m': 10,
        'fiber_rural_m': 5,
        'core_node_epc': 200000,
        'core_node_nsa': 200000,
        'core_node_sa': 250000,
        'core_edge': 4,
        'regional_node_epc': 100000,
        'regional_node_nsa': 100000,
        'regional_edge': 2,
        'regional_node_lower_epc': 50000,
        'regional_node_lower_nsa': 50000,
    }

    GLOBAL_PARAMETERS = {
        'overbooking_factor': 20,
        'return_period': 10,
        'return_period_spectrum': 15,
        'discount_rate': 5,
        'opex_percentage_of_capex': 10,
        'sectorization': 3,
        'confidence': [50], #[2.5, 50, 97.5],
        }

    path = os.path.join(DATA_RAW, 'pysim5g', 'capacity_lut_by_frequency.csv')
    lookup = read_capacity_lookup(path)

    tc_codes =  {
        'AP':'A',
        'AS':'C',
        'BR':'C',
        'DL':'Metro',
        'GJ':'A',
        'HP':'C',
        'HR':'B',
        'JK':'C',
        'KA':'A',
        'KL':'B',
        'KO':'Metro',
        'MH':'A',
        'MP':'B',
        'MU':'Metro',
        'NE':'C',
        'OR':'C',
        'PB':'B',
        'RJ':'B',
        'TN':'A',
        'UE':'B',
        'UW':'B',
        'WB':'C',
    }

    telecom_circles = []

    for tc_code, category in tc_codes.items():
        telecom_circles.append({
            'iso3': 'IND', 'iso2': 'IN', 'tc_code': tc_code, 'category': category,
            'regional_level': 3, 'regional_nodes_level': 2
        })

    decision_options = [
        'technology_options',
        'policy_options',
    ]

    for decision_option in decision_options:#[:1]:

        options = OPTIONS[decision_option]

        regional_annual_demand = []
        regional_results = []
        regional_cost_structure = []

        frequencies = set()

        for telecom_circle in telecom_circles:#[:1]:

            iso3 = telecom_circle['iso3']
            tc_code = telecom_circle['tc_code']
            category = telecom_circle['category']
            tc_parameters = TELECOM_CIRCLE_PARAMETERS[tc_code]

            folder = os.path.join(DATA_INTERMEDIATE, iso3, tc_code, 'subscriptions')
            filename = 'subs_forecast.csv'
            penetration_lut = load_penetration(os.path.join(folder, filename))

            folder = os.path.join(DATA_INTERMEDIATE, iso3, tc_code, 'smartphones')
            filename = 'smartphone_forecast.csv'
            smartphone_lut = load_smartphones(telecom_circle, os.path.join(folder, filename))

            folder = os.path.join(DATA_INTERMEDIATE, iso3)
            filename = 'core_lut.csv'
            core_lut = load_core_lut(os.path.join(folder, filename))

            print('-----')
            print('Working on {} in {}, {}'.format(decision_option, tc_code, iso3))
            print(' ')

            for option in options:#[:1]:

                print('Working on {} and {}'.format(option['scenario'], option['strategy']))

                confidence_intervals = GLOBAL_PARAMETERS['confidence']

                for ci in confidence_intervals:

                    print('CI: {}'.format(ci))

                    path = os.path.join(DATA_INTERMEDIATE, iso3, tc_code, 'regional_data.csv')
                    data = load_regions(path, telecom_circle)

                    data_initial = data.to_dict('records')

                    data_demand, annual_demand = estimate_demand(
                        data_initial,
                        option,
                        GLOBAL_PARAMETERS,
                        tc_parameters,
                        TIMESTEPS,
                        penetration_lut,
                        smartphone_lut,
                        category
                    )

                    data_supply = estimate_supply(
                        telecom_circle,
                        data_demand,
                        lookup,
                        option,
                        GLOBAL_PARAMETERS,
                        tc_parameters,
                        COSTS,
                        core_lut,
                        ci
                    )

                    data_assess = assess(
                        telecom_circle,
                        data_supply,
                        option,
                        GLOBAL_PARAMETERS,
                        tc_parameters,
                        COSTS,
                        TIMESTEPS
                    )

                    final_results = data_assess

                    regional_annual_demand = regional_annual_demand + annual_demand
                    regional_results = regional_results + final_results

        folder = os.path.join(BASE_PATH, '..', 'results')
        if not os.path.exists(folder):
            os.makedirs(folder)

        path = os.path.join(folder, 'regional_annual_demand_{}.csv'.format(decision_option))
        write_mno_demand(regional_annual_demand, folder, decision_option, path)

        write_results(regional_results, folder, decision_option)

        print('Completed model run')
