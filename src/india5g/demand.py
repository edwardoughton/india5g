"""
Estimate demand

Written by Ed Oughton.

Taken from the Python Telecommunication Assessment Library (pytal)

"""

def estimate_demand(regions, option, global_parameters,
    tc_parameters, timesteps, penetration_lut, smartphone_lut):
    """
    Estimate demand metrics including:
        - Total number of basic phone and smartphone users
        - Total data demand (in Mbps per square kilometer)
        - Total revenue (net present value over the assessment period in USD)

    Parameters
    ----------
    regions : list of dicts
        Data for all regions (one dict per region).
    option : dict
        Contains the scenario and strategy. The strategy string controls
        the strategy variants being tested in the model and is defined based
        on the type of technology generation, core and backhaul, and the
        strategy for infrastructure sharing, the number of networks in each
        geotype, spectrum and taxation.
    global_parameters : dict
        All global model parameters.
    country_parameters : dict
        All country specific parameters.
    timesteps : list
        All years for the assessment period.
    penetration_lut : list of dicts
        Contains annual cell phone penetration values.
    smartphone_lut : list of dicts
        Contains annual penetration values for smartphones.

    Returns
    -------
    regions : list of dicts
        Data for all regions (one dict per region).

    """
    output = []

    # generation_core_backhaul_sharing_networks_spectrum_tax
    network_strategy = option['strategy'].split('_')[4]

    for region in regions:

        if not region['area_km2'] > 0:
            continue

        geotype = region['geotype'].split(' ')[0]

        net_handle = network_strategy + '_' + geotype
        networks = tc_parameters['networks'][net_handle]

        if geotype == 'suburban':
            #smartphone lut only has urban-rural split, hence no suburban
            geotype_sps = 'urban'
        else:
            geotype_sps = geotype

        revenue = []
        demand_mbps_km2 = []

        scenario_per_user_capacity = get_per_user_capacity(region['geotype'], option)

        for timestep in timesteps:

            region['arpu_discounted'] = estimate_arpu(
                region,
                timestep,
                global_parameters,
                tc_parameters
            )

            region['penetration'] = penetration_lut[timestep]

            #cell_penetration : float
            #Number of cell phones per member of the population.
            region['population_with_phones'] = (
                region['population'] * (region['penetration'] / 100))

            #cell_penetration : float
            #Number of cell phones per member of the population.
            region['population_with_phones'] = (
                region['population'] * (region['penetration'] / 100))

            #phones : int
            #Total number of phones on the network being modeled.
            region['phones_on_network'] = (
                region['population_with_phones'] /
                networks)

            #get phone density
            region['phone_density_on_network_km2'] = (
                region['phones_on_network'] / region['area_km2']
            )

            #add regional smartphone penetration
            region['smartphone_penetration'] = smartphone_lut[geotype_sps][timestep]

            #phones : int
            #Total number of smartphones on the network being modeled.
            region['smartphones_on_network'] = (
                region['phones_on_network'] *
                (region['smartphone_penetration'] / 100)
            )

            #get smartphone density
            region['sp_density_on_network_km2'] = (
                region['smartphones_on_network'] / region['area_km2']
            )

            # demand_mbps_km2 : float
            # Total demand in mbps / km^2.
            demand_mbps_km2.append(
                (region['smartphones_on_network'] *
                scenario_per_user_capacity / #User demand in Mbps
                global_parameters['overbooking_factor'] /
                region['area_km2']
                ))

            annual_revenue = region['arpu_discounted'] * 12 * region['phones_on_network']

            revenue.append(annual_revenue)

        region['demand_mbps_km2'] = max(demand_mbps_km2)
        region['total_revenue'] = round(sum(revenue))
        region['revenue_km2'] = round(sum(revenue) / region['area_km2'])

        output.append(region)

    return output


def get_per_user_capacity(geotype, option):
    """

    """

    if geotype.split(' ')[0] == 'urban':

        return int(option['scenario'].split('_')[1])

    elif geotype.split(' ')[0] == 'suburban':

        return int(option['scenario'].split('_')[2])

    elif geotype.split(' ')[0] == 'rural':

        return int(option['scenario'].split('_')[3])

    else:
        return 'Did not recognise geotype'


def estimate_arpu(region, timestep, global_parameters, tc_parameters):
    """
    Allocate consumption category given a specific luminosity.

    """
    timestep = timestep - 2020

    if region['mean_luminosity_km2'] > tc_parameters['luminosity']['high']:
        arpu = tc_parameters['arpu']['high']
        return discount_arpu(arpu, timestep, global_parameters)

    elif region['mean_luminosity_km2'] > tc_parameters['luminosity']['medium']:
        arpu = tc_parameters['arpu']['medium']
        return discount_arpu(arpu, timestep, global_parameters)

    else:
        arpu = tc_parameters['arpu']['low']
        return discount_arpu(arpu, timestep, global_parameters)


def discount_arpu(arpu, timestep, global_parameters):
    """
    Discount arpu based on return period.

    192,744 = 23,773 / (1 + 0.05) ** (0:9)

    Parameters
    ----------
    arpu : float
        Average revenue per user.
    timestep : int
        Time period (year) to discount against.
    global_parameters : dict
        All global model parameters.

    Returns
    -------
    discounted_arpu : float
        The discounted revenue over the desired time period.

    """
    discount_rate = global_parameters['discount_rate'] / 100

    discounted_arpu = arpu / (1 + discount_rate) ** timestep

    return discounted_arpu
