import pytest
from india5g.demand import estimate_demand
from india5g.supply import (
    estimate_supply,
    find_site_density,
    estimate_site_upgrades,
    estimate_backhaul_upgrades
    )


def test_find_site_density(
    setup_region,
    setup_option,
    setup_global_parameters,
    setup_country_parameters,
    setup_timesteps,
    setup_penetration_lut,
    setup_costs,
    setup_lookup,
    setup_ci
    ):

    #test demand being larger than max capacity
    answer = find_site_density(
        {'demand_mbps_km2': 100000,
        'geotype': 'urban'},
        setup_option,
        setup_country_parameters,
        setup_lookup,
        setup_ci
    )

    assert answer == 2

    answer = find_site_density(
        {'demand_mbps_km2': 0.005,
        'geotype': 'urban'},
        setup_option,
        setup_country_parameters,
        setup_lookup,
        setup_ci
    )

    assert answer == 0.01

    answer = find_site_density(
        {'demand_mbps_km2': 250,
        'geotype': 'urban'},
        setup_option,
        setup_country_parameters,
        setup_lookup,
        setup_ci
    )

    assert answer == 0.05

    answer = find_site_density(
        {'demand_mbps_km2': 120,
        'geotype': 'urban'},
        setup_option,
        setup_country_parameters,
        setup_lookup,
        setup_ci
    )

    assert answer == 0.02

    answer = find_site_density(
        {'demand_mbps_km2': 120,
        'geotype': 'urban'},
        setup_option,
        setup_country_parameters,
        setup_lookup,
        setup_ci
    )

    assert answer == 0.02

    answer = find_site_density(
        {'demand_mbps_km2': 200000, #OBF is high on this test, hence large demand.
        'geotype': 'urban'},
        { #generation_core_backhaul_sharing_networks_spectrum_tax
        'scenario': 'S1_50_5_1',
        'strategy': '5G_epc_microwave_baseline_baseline_high_high_high'
        },
        setup_country_parameters,
        setup_lookup,
        setup_ci
    )

    assert answer == 2

def test_estimate_site_upgrades(
    setup_region,
    setup_option,
    setup_country_parameters,
    ):

    #total sites across all opterators
    setup_region[0]['sites_estimated_total'] = 100
    setup_region[0]['sites_4G'] = 0

    #100 sites in total across two operators, hence 50 existing sites for this MNO
    answer = estimate_site_upgrades(
        setup_region[0],
        '4G_epc_wireless_baseline_baseline_baseline_baseline',
        100, #100 sites required for this MNO
        {'proportion_of_sites': 50}
    )

    assert answer['new_sites'] == 50
    assert answer['upgraded_sites'] == 50

    #total sites across all operators
    setup_region[0]['sites_estimated_total'] = 200
    setup_region[0]['sites_4G'] = 50

    #200 sites in total across two operators, hence 100 existing sites for this MNO
    #50 existing 4G sites, hence only 50 needing to be upgraded to 4G
    answer = estimate_site_upgrades(setup_region[0],
        '4G_epc_wireless_baseline_baseline_baseline_baseline',
        100, #100 sites required for this MNO
        {'proportion_of_sites': 50}
    )

    assert answer['new_sites'] == 0
    assert answer['upgraded_sites'] == 75

    #total sites across all operators
    setup_region[0]['sites_estimated_total'] = 0
    setup_region[0]['sites_4G'] = 0

    #100 sites in total across two operators, hence 50 existing sites for this MNO
    answer = estimate_site_upgrades(setup_region[0],
        '4G_epc_wireless_baseline_baseline_baseline_baseline',
        100, #100 sites required for this MNO
        {'proportion_of_sites': 50}
    )

    assert answer['new_sites'] == 100
    assert answer['upgraded_sites'] == 0

    #total sites across all operators
    setup_region[0]['sites_estimated_total'] = 100
    setup_region[0]['sites_4G'] = 0

    #100 sites in total across two operators, hence 50 existing sites for this MNO
    answer = estimate_site_upgrades(setup_region[0],
        '4G_epc_wireless_baseline_baseline_baseline_baseline',
        100, #100 sites required for this MNO
        {'proportion_of_sites': 10}
    )

    assert answer['new_sites'] == 90
    assert answer['upgraded_sites'] == 10

    #total sites across all operators
    setup_region[0]['sites_estimated_total'] = 100
    setup_region[0]['sites_4G'] = 50

    #100 sites in total across two operators, hence 50 existing sites for this MNO
    answer = estimate_site_upgrades(setup_region[0],
        '4G_epc_wireless_baseline_baseline_baseline_baseline',
        100, #100 sites required for this MNO
        {'proportion_of_sites': 50}
    )

    assert answer['new_sites'] == 50
    assert answer['upgraded_sites'] == 25

    #total sites across all operators
    setup_region[0]['sites_estimated_total'] = 100
    setup_region[0]['sites_4G'] = 100

    #100 sites in total across two operators, hence 50 existing sites for this MNO
    answer = estimate_site_upgrades(setup_region[0],
        '5g_nsa_wireless_baseline_baseline_baseline_baseline',
        50, #100 sites required for this MNO
        {'proportion_of_sites': 50}
    )

    assert answer['new_sites'] == 0
    assert answer['upgraded_sites'] == 50


def test_estimate_supply(
    setup_region,
    setup_lookup,
    setup_option,
    setup_global_parameters,
    setup_country_parameters,
    setup_costs,
    setup_core_lut,
    setup_ci
    ):

    #total sites across all operators
    setup_region[0]['sites_estimated_total'] = 100
    setup_region[0]['sites_4G'] = 0
    setup_region[0]['backhaul_fiber'] = 0
    setup_region[0]['backhaul_copper'] = 0
    setup_region[0]['backhaul_wireless'] = 0
    setup_region[0]['backhaul_satellite'] = 0

    answer = estimate_supply('MWI',
        setup_region,
        setup_lookup,
        setup_option,
        setup_global_parameters,
        setup_country_parameters,
        setup_costs,
        setup_core_lut,
        setup_ci
    )

    assert round(answer[0]['site_density'], 1) == 0.9


def test_estimate_backhaul_upgrades(
    setup_region
    ):

    setup_region[0]['new_sites'] = 50
    setup_region[0]['upgraded_sites'] = 50

    setup_region[0]['backhaul_fiber'] = 20
    setup_region[0]['backhaul_copper'] = 20
    setup_region[0]['backhaul_wireless'] = 50
    setup_region[0]['backhaul_satellite'] = 10

    answer = estimate_backhaul_upgrades(
        setup_region[0],
        '4G_epc_fiber_baseline_baseline_baseline_baseline',
    )

    assert answer['backhaul_new'] == 80

    answer = estimate_backhaul_upgrades(
        setup_region[0],
        '4G_epc_wireless_baseline_baseline_baseline_baseline',
    )

    assert answer['backhaul_new'] == 30

    setup_region[0]['backhaul_fiber'] = 100

    answer = estimate_backhaul_upgrades(
        setup_region[0],
        '4G_epc_fiber_baseline_baseline_baseline_baseline',
    )

    assert answer['backhaul_new'] == 0

    setup_region[0]['backhaul_fiber'] = 0
    setup_region[0]['backhaul_wireless'] = 100

    answer = estimate_backhaul_upgrades(
        setup_region[0],
        '4G_epc_wireless_baseline_baseline_baseline_baseline',
    )

    assert answer['backhaul_new'] == 0
