"""
Assessment Module

Written by Ed Oughton.

Taken from the Python Telecommunication Assessment Library (pytal)

"""

def assess(country, regions, option, global_parameters, country_parameters, costs, timesteps):
    """
    For each region, assess the viability level.

    Parameters
    ----------
    country : dict
        Country information.
    regions : dataframe
        Geopandas dataframe of all regions.
    option : dict
        Contains the scenario and strategy. The strategy string controls
        the strategy variants being testes in the model and is defined based
        on the type of technology generation, core and backhaul, and the level
        of sharing, subsidy, spectrum and tax.
    global_parameters : dict
        All global model parameters.
    country_parameters : dict
        All country specific parameters.

    Returns
    -------
    output : list of dicts
        Contains all output data.

    """
    interim = []

    strategy = option['strategy']
    available_for_cross_subsidy = 0

    total_tc_population = round(sum([p['population'] for p in regions]))

    for region in regions:

        # add customer acquition cost
        region = get_administration_cost(region, country_parameters,
        global_parameters, timesteps)

        # npv spectrum cost
        region['spectrum_cost'] = get_spectrum_costs(region, option['strategy'],
            global_parameters, country_parameters, timesteps, total_tc_population)

        #tax on investment
        region['tax'] = calculate_tax(region, strategy, country_parameters)

        #profit margin value calculated on all costs + taxes
        region['profit_margin'] = calculate_profit(region, country_parameters)

        region['total_cost'] = (
            region['network_cost'] +
            region['ops_and_acquisition'] +
            region['spectrum_cost'] +
            region['tax'] +
            region['profit_margin']
        )

        region['total_cost_km2'] = region['total_cost'] / region['area_km2']

        #avoid zero division
        if region['total_cost'] > 0 and region['mno_smartphones_on_network'] > 0:
            region['cost_per_sp_user'] = region['total_cost'] / region['mno_smartphones_on_network']
        else:
            region['cost_per_sp_user'] = 0

        region = allocate_available_excess(region)
        available_for_cross_subsidy += region['available_cross_subsidy']

        interim.append(region)

    interim = sorted(interim, key=lambda k: k['deficit'], reverse=False)

    output = []

    for region in interim:

        region, available_for_cross_subsidy = estimate_subsidies(
            region, available_for_cross_subsidy)

        output.append(region)

    return output


def get_administration_cost(region, country_parameters, global_parameters, timesteps):
    """
    There is an annual administration cost to deploying and operating all assets.
    Parameters
    ----------
    regions : list of dicts
        Data for all regions (one dict per region).
    country_parameters : dict
        All country specific parameters.
    Returns
    -------
    region : dict
        Contains all regional data.
    """
    annual_cost = (
        region['network_cost'] *
        (country_parameters['financials']['administration_percentage_of_network_cost'] /
        100))

    costs = []

    for timestep in timesteps:

        timestep = timestep - 2020

        discounted_cost = discount_cost(annual_cost, timestep, global_parameters)

        costs.append(discounted_cost)

    region['ops_and_acquisition'] = sum(costs)

    return region


def allocate_available_excess(region):
    """
    Allocate available excess capital (if any).

    """
    difference = region['total_revenue'] - region['total_cost']

    if difference > 0:
        region['available_cross_subsidy'] = difference
        region['deficit'] = 0
    else:
        region['available_cross_subsidy'] = 0
        region['deficit'] = abs(difference)

    return region


def get_spectrum_costs(region, strategy, global_parameters, country_parameters,
    timesteps, total_tc_population):
    """
    Calculate spectrum costs.

    """
    population_share = int(round(region['population'])) / total_tc_population
    frequencies = country_parameters['frequencies']
    generation = strategy.split('_')[0]
    frequencies = frequencies[generation]

    spectrum_cost = strategy.split('_')[5]

    coverage_spectrum_cost = 'spectrum_baseline_cov_usd_mhz'
    capacity_spectrum_cost = 'spectrum_baseline_cap_usd_mhz'

    coverage_cost_usd_mhz = country_parameters['financials'][coverage_spectrum_cost]
    capacity_cost_usd_mhz = country_parameters['financials'][capacity_spectrum_cost]

    if not spectrum_cost == 'baseline':
        coverage_cost_usd_mhz = coverage_cost_usd_mhz * ((100 - int(spectrum_cost)) / 100)
        capacity_cost_usd_mhz = capacity_cost_usd_mhz * ((100 - int(spectrum_cost)) / 100)

    annual_cov_cost_usd_mhz = coverage_cost_usd_mhz / global_parameters['return_period_spectrum']
    annual_cap_cost_usd_mhz = capacity_cost_usd_mhz / global_parameters['return_period_spectrum']

    annual_cov_costs = []
    annual_cap_costs = []

    for timestep in timesteps:

        timestep = timestep - 2020

        discounted_cov_cost = discount_cost(annual_cov_cost_usd_mhz, timestep, global_parameters)
        discounted_cap_cost = discount_cost(annual_cap_cost_usd_mhz, timestep, global_parameters)

        annual_cov_costs.append(discounted_cov_cost)
        annual_cap_costs.append(discounted_cap_cost)

    coverage_cost_usd_mhz_npv = sum(annual_cov_costs)
    capacity_cost_usd_mhz_npv = sum(annual_cap_costs)

    all_costs = []
    undiscounted_costs = []
    for frequency in frequencies:

        channel_number = int(frequency['bandwidth'].split('x')[0])
        channel_bandwidth = float(frequency['bandwidth'].split('x')[1])
        bandwidth_total = channel_number * channel_bandwidth

        if frequency['frequency'] < 1000:
            cost = (coverage_cost_usd_mhz_npv * bandwidth_total)
            all_costs.append(cost)
            undiscounted_costs.append(coverage_cost_usd_mhz * bandwidth_total)
        else:
            cost = (capacity_cost_usd_mhz_npv * bandwidth_total)
            all_costs.append(cost)
            undiscounted_costs.append(capacity_cost_usd_mhz * bandwidth_total)

    return sum(all_costs) * population_share


def calculate_tax(region, strategy, country_parameters):
    """
    Calculate tax.

    """
    tax_rate = strategy.split('_')[6]
    tax_rate = 'tax_{}'.format(tax_rate)

    tax_rate = country_parameters['financials'][tax_rate]

    investment = region['network_cost']

    tax = investment * (tax_rate / 100)

    return tax


def calculate_profit(region, country_parameters):
    """
    Estimate npv profit.

    """
    investment = (
        region['network_cost'] +
        region['spectrum_cost'] +
        region['tax']
    )

    profit = investment * (country_parameters['financials']['profit_margin'] / 100)

    return profit


def estimate_subsidies(region, available_for_cross_subsidy):
    """
    Estimates either the contribution to cross-subsidies, or the
    quantity of subsidy required.

    Parameters
    ----------
    region : Dict
        Contains all variable for a single region.
    available_for_cross_subsidy : int
        The amount of capital available for cross-subsidization.

    Returns
    -------
    region : Dict
        Contains all variable for a single region.
    available_for_cross_subsidy : int
        The amount of capital available for cross-subsidization.

    """
    if region['deficit'] > 0:

        if available_for_cross_subsidy >= region['deficit']:
            region['used_cross_subsidy'] = region['deficit']
            available_for_cross_subsidy -= region['deficit']
        elif 0 < available_for_cross_subsidy < region['deficit']:
            region['used_cross_subsidy'] = available_for_cross_subsidy
            available_for_cross_subsidy = 0
        else:
            region['used_cross_subsidy'] = 0

    else:
        region['used_cross_subsidy'] = 0

    required_state_subsidy = (region['total_cost'] -
        (region['total_revenue'] + region['used_cross_subsidy']))

    if required_state_subsidy > 0:
        region['required_state_subsidy'] = required_state_subsidy
    else:
        region['required_state_subsidy'] = 0

    return region, available_for_cross_subsidy


def discount_cost(cost, timestep, global_parameters):
    """
    Discount cost based on return period.
    192,744 = 23,773 / (1 + 0.05) ** (0:9)
    Parameters
    ----------
    cost : float
        Annual cost.
    timestep : int
        Time period (year) to discount against.
    global_parameters : dict
        All global model parameters.
    Returns
    -------
    discounted_cost : float
        The discounted admin cost over the desired time period.
    """
    discount_rate = global_parameters['discount_rate'] / 100

    discounted_cost = cost / (1 + discount_rate) ** timestep

    return discounted_cost
