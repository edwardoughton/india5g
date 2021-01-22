import pytest
from india5g.assess import (
    get_administration_cost,
    get_spectrum_costs,
    calculate_tax,
    calculate_profit,
    assess,
    estimate_subsidies,
    allocate_available_excess
)


def test_assess(setup_option, setup_global_parameters, setup_country_parameters,
    setup_costs, setup_timesteps):
    """
    Integration test for main function.

    """
    regions = [
        {
            'GID_id': 'a',
            'geotype': 'rural 1',
            'population': 1000,
            'population_km2': 500,
            'total_revenue': 20000,
            'network_cost': 5000,
            'mno_smartphones_on_network': 250,
            'mno_phones_on_network': 500,
        },
        {
            'GID_id': 'b',
            'geotype': 'rural 1',
            'population': 500,
            'population_km2': 250,
            'total_revenue': 12000,
            'network_cost': 8000,
            'mno_smartphones_on_network': 250,
            'mno_phones_on_network': 500,
        },
    ]

    setup_country_parameters['financials']['spectrum_baseline_cov_usd_mhz'] = 100
    setup_country_parameters['financials']['spectrum_baseline_cap_usd_mhz'] = 100

    answer = assess('MWI', regions, setup_option, setup_global_parameters,
        setup_country_parameters, setup_costs, setup_timesteps)

    assert answer[0]['total_revenue'] == 20000
    assert answer[0]['network_cost'] == 5000
    assert answer[0]['spectrum_cost'] == 266.66666666666663
    assert answer[0]['tax'] == 1250
    assert answer[0]['profit_margin'] == 1303.3333333333335
    assert answer[0]['total_cost'] == 8820.0
    assert answer[0]['available_cross_subsidy'] == 11180.0
    assert answer[0]['used_cross_subsidy'] == 0
    assert answer[0]['required_state_subsidy'] == 0

    assert answer[1]['total_revenue'] == 12000
    assert answer[1]['network_cost'] == 8000
    assert answer[1]['spectrum_cost'] == 133.33333333333331
    assert answer[1]['tax'] == 2000
    assert answer[1]['profit_margin'] == 2026.6666666666665
    assert answer[1]['total_cost'] == 13760.0
    assert answer[1]['available_cross_subsidy'] == 0
    assert answer[1]['used_cross_subsidy'] == 1760.0
    assert answer[1]['required_state_subsidy'] == 0

    regions = [
        {
            'GID_id': 'a',
            'population': 1000,
            'population_km2': 500,
            'total_revenue': 20000,
            'network_cost': 5200,
            'mno_smartphones_on_network': 250,
            'mno_phones_on_network': 500,
        },
        {
            'GID_id': 'b',
            'population': 1000,
            'population_km2': 500,
            'total_revenue': 2500,
            'network_cost': 5200,
            'mno_smartphones_on_network': 250,
            'mno_phones_on_network': 500,
        },
    ]

    answer = assess('MWI', regions, setup_option, setup_global_parameters,
        setup_country_parameters, setup_costs, setup_timesteps)

    assert answer[0]['available_cross_subsidy'] == 10920.0
    assert answer[0]['used_cross_subsidy'] == 0
    assert answer[0]['required_state_subsidy'] == 0
    assert answer[1]['available_cross_subsidy'] == 0
    assert answer[1]['used_cross_subsidy'] == 6580.0
    assert answer[1]['required_state_subsidy'] == 0


def test_get_administration_cost(setup_region, setup_country_parameters,
    setup_global_parameters, setup_timesteps):
    """
    Unit test.
    """
    setup_region[0]['network_cost'] = 100
    setup_timesteps = list(range(2020, 2030 + 1))

    answer = get_administration_cost(setup_region[0], setup_country_parameters,
        setup_global_parameters, setup_timesteps)

    assert round(answer['ops_and_acquisition']) == 174


def test_get_spectrum_costs(setup_region, setup_option, setup_global_parameters,
    setup_country_parameters, setup_timesteps):

    setup_region[0]['new_sites'] = 1
    setup_timesteps = list(range(2020, 2030))
    setup_global_parameters['return_period'] = 10

    # 20 = 1e6 * 40 (cost = cost_mhz_pop * bw ) discounted annually
    assert get_spectrum_costs(setup_region[0], setup_option['strategy'],
        setup_global_parameters, setup_country_parameters, setup_timesteps, 1000) == 324312867.0257621

    setup_region[0]['new_sites'] = 1

    # test high spectrum costs which are 50% higher
    assert get_spectrum_costs(setup_region[0], '4G_epc_wireless_baseline_baseline_high_baseline',
        setup_global_parameters, setup_country_parameters, setup_timesteps, 1000) == (
            324312867.0257621 * (setup_country_parameters['financials']['spectrum_cost_high'] / 100))

    # test low spectrum costs which are 50% lower
    assert get_spectrum_costs(setup_region[0], '4G_epc_wireless_baseline_baseline_low_baseline',
        setup_global_parameters, setup_country_parameters, setup_timesteps, 1000) == (
            324312867.0257621 * (setup_country_parameters['financials']['spectrum_cost_low'] / 100))


def test_calculate_tax(setup_region, setup_option, setup_country_parameters):

    setup_region[0]['total_revenue'] = 1e7
    setup_region[0]['network_cost'] = 1e6
    setup_region[0]['spectrum_cost'] = 1e1

    assert calculate_tax(setup_region[0], setup_option['strategy'], setup_country_parameters) == 1e6 * (25/100)

    setup_region[0]['network_cost'] = 1e6
    setup_option['strategy'] = '4G_epc_wireless_baseline_baseline_baseline_high'

    answer = calculate_tax(setup_region[0], setup_option['strategy'], setup_country_parameters)

    assert answer == 1e6 * (40/100)

    setup_region[0]['network_cost'] = 1e6
    setup_option['strategy'] = '4G_epc_wireless_baseline_baseline_baseline_low'

    answer = calculate_tax(setup_region[0], setup_option['strategy'], setup_country_parameters)

    assert answer == 1e6 * (10/100)

    setup_region[0]['total_revenue'] = 1e7
    setup_region[0]['network_cost'] = 1e9
    setup_region[0]['spectrum_cost'] = 1e1

    assert calculate_tax(setup_region[0], setup_option['strategy'], setup_country_parameters) == 1e8


def test_calculate_profit(setup_region, setup_country_parameters):

    setup_region[0]['network_cost'] = 1e6
    setup_region[0]['spectrum_cost'] = 6e4
    setup_region[0]['tax'] = 265e3

    assert calculate_profit(setup_region[0], setup_country_parameters) == 265e3


def test_estimate_subsidies():

    region = {
            'GID_id': 'a',
            'total_revenue': 10000,
            'total_cost': 5000,
            'available_cross_subsidy': 5000,
            'deficit': 0,
        }

    answer, available_cross_subsidy = estimate_subsidies(region, 0)

    assert answer['available_cross_subsidy'] == 5000
    assert answer['used_cross_subsidy'] == 0
    assert answer['required_state_subsidy'] == 0
    assert available_cross_subsidy == 0

    region = {
            'GID_id': 'a',
            'total_revenue': 5000,
            'total_cost': 10000,
            'available_cross_subsidy': 0,
            'deficit': 5000,
        }

    answer, available_cross_subsidy = estimate_subsidies(region, 5000)

    assert answer['available_cross_subsidy'] == 0
    assert answer['used_cross_subsidy'] == 5000
    assert answer['required_state_subsidy'] == 0
    assert available_cross_subsidy == 0

    region = {
            'GID_id': 'a',
            'total_revenue': 5000,
            'total_cost': 10000,
            'available_cross_subsidy': 0,
            'deficit': 5000,
        }

    answer, available_cross_subsidy = estimate_subsidies(region, 0)

    assert answer['available_cross_subsidy'] == 0
    assert answer['used_cross_subsidy'] == 0
    assert answer['required_state_subsidy'] == 5000
    assert available_cross_subsidy == 0

    region = {
            'GID_id': 'a',
            'total_revenue': 5000,
            'total_cost': 10000,
            'available_cross_subsidy': 0,
            'deficit': 5000,
        }

    answer, available_cross_subsidy = estimate_subsidies(region, 2500)

    assert answer['available_cross_subsidy'] == 0
    assert answer['used_cross_subsidy'] == 2500
    assert answer['required_state_subsidy'] == 2500
    assert available_cross_subsidy == 0


def test_allocate_available_excess():

    region = {
            'total_revenue': 10000,
            'total_cost': 5000,
        }

    answer = allocate_available_excess(region)

    assert answer['available_cross_subsidy'] == 5000
    assert answer['deficit'] == 0

    regions = {
            'total_revenue': 5000,
            'total_cost': 10000,
        }

    answer = allocate_available_excess(regions)

    assert answer['available_cross_subsidy'] == 0
    assert answer['deficit'] == 5000
