"""
Optimize supply

Written by Ed Oughton.

Taken from the Python Telecommunication Assessment Library (pytal)

"""
import math
from itertools import tee
from operator import itemgetter

from india5g.costs import find_single_network_cost


def estimate_supply(telecom_circle, regions, lookup, option, global_parameters,
    tc_parameters, costs, core_lut, ci):
    """
    For each region, optimize the network design and estimate
    the financial cost.

    Parameters
    ----------
    regions : dataframe
        Geopandas dataframe of all regions.
    lookup : dict
        A dictionary containing the lookup capacities.
    option : dict
        Contains the scenario and strategy. The strategy string controls
        the strategy variants being testes in the model and is defined based
        on the type of technology generation, core and backhaul, and the level
        of sharing, subsidy, spectrum and tax.
    global_parameters : dict
        All global model parameters.
    tc_parameters : dict
        All telecom circle specific parameters.
    costs : dict
        All equipment costs.
    core_lut : ???
        ???
    ci : int
        Confidence interval.

    """
    output_regions = []

    for region in regions:

        if math.isnan(region['demand_mbps_km2']):
            continue

        region['site_density'] = find_site_density(region, option,
            tc_parameters, lookup, ci)

        total_sites_required = math.ceil(region['site_density'] * region['area_km2'])

        region = estimate_site_upgrades(
            region,
            option['strategy'],
            total_sites_required,
            tc_parameters
        )

        region = estimate_backhaul_upgrades(region, option['strategy'])

        region = find_single_network_cost(
            region,
            option,
            costs,
            global_parameters,
            tc_parameters,
            core_lut,
        )

        region['scenario'] = option['scenario']
        region['strategy'] = option['strategy']
        region['confidence'] = ci

        output_regions.append(region)

    return output_regions


def find_site_density(region, option, tc_parameters, lookup, ci):
    """
    For a given region, provide an optmized network.

    """
    demand = region['demand_mbps_km2']
    geotype = region['geotype'].split(' ')[0]
    ant_type = 'macro'
    generation = option['strategy'].split('_')[0]
    frequencies = tc_parameters['frequencies']
    frequencies = frequencies[generation]
    ci = str(ci)
    unique_densities = set()

    capacity = 0

    for item in frequencies:

        frequency = str(item['frequency'])
        bandwidth = str(item['bandwidth'].split('x')[1])

        density_capacities = lookup_capacity(
            lookup,
            geotype,
            ant_type,
            frequency,
            generation,
            ci
            )

        for item in density_capacities:
            site_density, capacity = item
            unique_densities.add(site_density)

    density_lut = []

    for density in list(unique_densities):
        capacity = 0
        for item in frequencies:

            frequency = str(item['frequency'])
            bandwidth = float(item['bandwidth'].split('x')[1])

            density_capacities = lookup_capacity(
                lookup,
                geotype,
                ant_type,
                frequency,
                generation,
                ci
            )

            for density_capacity in density_capacities:

                if density_capacity[0] == density:
                    capacity += density_capacity[1]

        density_lut.append((density, capacity))

    density_lut = sorted(density_lut, key=lambda tup: tup[0])

    max_density, max_capacity = density_lut[-1]
    min_density, min_capacity = density_lut[0]

    max_capacity = max_capacity * bandwidth
    min_capacity = min_capacity * bandwidth

    if demand > max_capacity:

        return max_density

    elif demand < min_capacity:

        return min_density

    else:

        for a, b in pairwise(density_lut):

            lower_density, lower_capacity  = a
            upper_density, upper_capacity  = b

            lower_capacity = lower_capacity * bandwidth
            upper_capacity = upper_capacity * bandwidth

            if lower_capacity <= demand < upper_capacity:

                site_density = interpolate(
                    lower_capacity, lower_density,
                    upper_capacity, upper_density,
                    demand
                )
                return site_density


def lookup_capacity(lookup, environment, ant_type, frequency,
    generation, ci):
    """
    Use lookup table to find the combination of spectrum bands
    which meets capacity by clutter environment geotype, frequency,
    bandwidth, technology generation and site density.

    """
    if (environment, ant_type, frequency, generation, ci) not in lookup:
        raise KeyError("Combination %s not found in lookup table",
                       (environment, ant_type, frequency, generation, ci))

    density_capacities = lookup[
        (environment, ant_type,  frequency, generation, ci)
    ]

    return density_capacities


def interpolate(x0, y0, x1, y1, x):
    """
    Linear interpolation between two values.

    """
    y = (y0 * (x1 - x) + y1 * (x - x0)) / (x1 - x0)

    return y


def pairwise(iterable):
    """
    Return iterable of 2-tuples in a sliding window.
    >>> list(pairwise([1,2,3,4]))
    [(1,2),(2,3),(3,4)]
    """
    a, b = tee(iterable)
    next(b, None)

    return zip(a, b)


def estimate_site_upgrades(region, strategy, total_sites_required, tc_parameters):
    """
    Estimate the number of greenfield sites and brownfield upgrades.

    Parameters
    ----------
    region : dict
        Contains all regional data.
    strategy : dict
        The strategy string controls the strategy variants being tested in the
        model and is defined based on the type of technology generation, core
        and backhaul, and the level of sharing, subsidy, spectrum and tax.
    total_sites_required : int
        Number of sites needed to meet demand.
    tc_parameters : dict
        All telecom circle specific parameters.

    Returns
    -------
    region : dict
        Contains all regional data.

    """
    generation = strategy.split('_')[0]

    region['existing_network_sites'] = (
        region['sites_estimated_total'] *
        (tc_parameters['proportion_of_sites'] / 100)
    )

    existing_4G_sites = math.ceil(
        region['sites_4G'] *
        (tc_parameters['proportion_of_sites'] / 100)
    )

    if total_sites_required > region['existing_network_sites']:

        region['new_sites'] = int(
            round(total_sites_required - region['existing_network_sites']))

        if region['existing_network_sites'] > 0:
            if generation == '4G' and existing_4G_sites > 0 :
                region['upgraded_sites'] = (
                    region['existing_network_sites'] - existing_4G_sites)
            else:
                region['upgraded_sites'] = region['existing_network_sites']
        else:
            region['upgraded_sites'] = 0

    else:
        region['new_sites'] = 0

        if generation == '4G' and existing_4G_sites > 0 :
            to_upgrade = total_sites_required - existing_4G_sites
            region['upgraded_sites'] = to_upgrade if to_upgrade >= 0 else 0
        else:
            region['upgraded_sites'] = total_sites_required

    return region


def estimate_backhaul_upgrades(region, strategy):
    """
    Estimates the number of backhaul links needing to be upgraded.

    Parameters
    ----------
    region : dict
        Contains all regional data.
    strategy : dict
        The strategy string controls the strategy variants being tested in the
        model and is defined based on the type of technology generation, core
        and backhaul, and the level of sharing, subsidy, spectrum and tax.
    tc_parameters : dict
        All telecom circle specific parameters.

    Returns
    -------
    region : dict
        Contains all regional data.

    """
    backhaul = strategy.split('_')[2]

    all_sites = region['new_sites'] + region['upgraded_sites']

    if backhaul == 'fiber':

        existing_fiber = region['backhaul_fiber']

        if existing_fiber < all_sites:
            region['backhaul_new'] = all_sites - existing_fiber
        else:
            region['backhaul_new'] = 0

    elif backhaul == 'wireless':

        existing_backhaul = region['backhaul_wireless'] + region['backhaul_fiber']

        if existing_backhaul < all_sites:
            region['backhaul_new'] = all_sites - existing_backhaul
        else:
            region['backhaul_new'] = 0

    return region
