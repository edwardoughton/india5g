"""
Options consisting of scenarios and strategies.

Country parameters consist of those parameters which are specific
to each country.

Written by Ed Oughton

January 2020

#strategy is defined based on generation_core_backhaul_sharing_networks_spectrum_tax

generation: technology generation, so 3G or 4G
core: type of core data transport network, eg. evolved packet core (4G)
backhaul: type of backhaul, so fiber or wireless
sharing: the type of infrastructure sharing, active, passive etc..
network: relates to the number of networks, as defined in country parameters
spectrum: type of spectrum strategy, so baseline, high or low
tax: type of taxation strategy, so baseline, high or low

"""
OPTIONS = {
    'technology_options': [
        {
            'scenario': 'S1_25_10_2',
            'strategy': '4G_epc_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '4G_epc_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '4G_epc_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '4G_epc_fiber_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '4G_epc_fiber_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '4G_epc_fiber_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_fiber_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_fiber_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_fiber_baseline_baseline_baseline_baseline',
        },
    ],
    'business_model_options': [
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_passive_baseline_baseline_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_passive_baseline_baseline_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_passive_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_active_baseline_baseline_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_active_baseline_baseline_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_active_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_shared_baseline_baseline_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_shared_baseline_baseline_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_shared_baseline_baseline_baseline',
        },
    ],
    'policy_options': [
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_baseline_baseline_low_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_baseline_baseline_low_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_baseline_baseline_low_baseline',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_baseline_baseline_high_baseline',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_baseline_baseline_high_baseline',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_baseline_baseline_high_baseline',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_low',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_low',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_low',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_high',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_high',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_baseline_baseline_baseline_high',
        },
    ],
    'mixed_options': [  #generation_core_backhaul_sharing_subsidy_spectrum_tax
        {
            'scenario': 'S1_25_10_2',
            'strategy': '4G_epc_wireless_shared_baseline_low_low',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '4G_epc_wireless_shared_baseline_low_low',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '4G_epc_wireless_shared_baseline_low_low',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '4G_epc_fiber_shared_baseline_low_low',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '4G_epc_fiber_shared_baseline_low_low',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '4G_epc_fiber_shared_baseline_low_low',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_nsa_wireless_shared_baseline_low_low',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_nsa_wireless_shared_baseline_low_low',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_nsa_wireless_shared_baseline_low_low',
        },
        {
            'scenario': 'S1_25_10_2',
            'strategy': '5G_sa_fiber_shared_baseline_low_low',
        },
        {
            'scenario': 'S2_50_20_5',
            'strategy': '5G_sa_fiber_shared_baseline_low_low',
        },
        {
            'scenario': 'S3_100_30_10',
            'strategy': '5G_sa_fiber_shared_baseline_low_low',
        },
    ]
}


TELECOM_CIRCLE_PARAMETERS = {
    'AP': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.9,
                'medium': 1.2,
                'low': 0.6,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 30, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 2.22, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.54, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 110390000,
                'spectrum_baseline_cap_usd_mhz': 27206667,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    'GJ': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.6,
                'medium': 1,
                'low': 0.5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 1.11, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.32, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 86590000,
                'spectrum_baseline_cap_usd_mhz': 24966667,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    'KA': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.8,
                'medium': 1.2,
                'low': 0.6,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 1.19, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.46, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 73010000,
                'spectrum_baseline_cap_usd_mhz': 28513333,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    'MH': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.7,
                'medium': 1.1,
                'low': 0.6,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 1.27, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.29, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 144970000,
                'spectrum_baseline_cap_usd_mhz': 33460000,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    'TN': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.9,
                'medium': 1.3,
                'low': 0.6,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x1.25',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 1.22, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.89, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'spectrum_baseline_cov_usd_mhz': 88200000,
                'spectrum_baseline_cap_usd_mhz': 64213333,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    # Category B Telecom Circles
    'HR': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.13,
                'medium': 0.8,
                'low': 0.4,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.67, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.28, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 17010000,
                'spectrum_baseline_cap_usd_mhz': 7140000,
              	'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    'KL': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.9,
                'medium': 1.3,
                'low': 0.6,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 1.20, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.38, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 40390000,
                'spectrum_baseline_cap_usd_mhz': 12880000,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    'MP': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.4,
                'medium': 1.0,
                'low': 0.5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.712, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.137, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 51730000,
                'spectrum_baseline_cap_usd_mhz': 9986667,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    'PB': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.6,
                'medium': 1.1,
                'low': 0.5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 1.077, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.423, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 29890000,
                'spectrum_baseline_cap_usd_mhz': 11760000,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    'RJ': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.5,
                'medium': 1.1,
                'low': 0.5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.580, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.235, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 39760000,
                'spectrum_baseline_cap_usd_mhz': 16170000,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    'UE': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.1,
                'medium': 0.7,
                'low': 0.4,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.237, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.007, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 47460000,
                'spectrum_baseline_cap_usd_mhz': 15750000,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    'UW': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.2,
                'medium': 0.8,
                'low': 0.4,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 3.92, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 1.43, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 39620000,
                'spectrum_baseline_cap_usd_mhz': 14490000,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 30, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    'WB': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.4,
                'medium': 0.9,
                'low': 0.5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.213, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.055, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 18550000,
                'spectrum_baseline_cap_usd_mhz': 4806667,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    # Cateogry C telecom circles

    'HP': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 6,
                'medium': 3,
                'low': 2,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.897, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.251, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 6160000,
                'spectrum_baseline_cap_usd_mhz': 1726667,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    'JK': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.5,
                'medium': 1,
                'low': .5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.593, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.133, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 7280000,
                'spectrum_baseline_cap_usd_mhz': 1633333,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    'NE': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.6,
                'medium': 1.1,
                'low': 0.5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.501, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.091, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
             	'spectrum_baseline_cov_usd_mhz': 6160000,
                'spectrum_baseline_cap_usd_mhz': 1120000,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    'AS': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.6,
                'medium': 1.0,
                'low': 0.5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.708, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.131, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
             	'spectrum_baseline_cov_usd_mhz': 22120000,
                'spectrum_baseline_cap_usd_mhz': 4106667,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    'BR': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.2,
                'medium': 0.8,
                'low': 0.4,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.196, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.052, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 26880000,
                'spectrum_baseline_cap_usd_mhz': 7186667,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    'OR': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.4,
                'medium': 0.9,
                'low': 0.5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 0.348, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 0.088, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 14630000,
                'spectrum_baseline_cap_usd_mhz': 3733333,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },

    # Metros Telecom Circles

    'DL': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.5,
                'medium': 1.0,
                'low': 0.5,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 10.18, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 3.04, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 171010000,
                'spectrum_baseline_cap_usd_mhz': 51146667,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    'MU': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.9,
                'medium': 1.2,
                'low': 0.6,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 7.39, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 2.29, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 134330000,
                'spectrum_baseline_cap_usd_mhz': 42233333,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    'KO': {
            'luminosity': {
                'high': 3,
                'medium': 1,
            },
            'arpu': {
                'high': 1.3,
                'medium': 0.9,
                'low': 0.4,
            },
            'networks': {
                'baseline_urban': 4,
                'baseline_suburban': 4,
                'baseline_rural': 4,
            },
            'proportion_of_sites': 20, #what proportion of total sites does an MNO have access to?
            'frequencies': {
                '4G': [
                    {
                        'frequency': 850,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 1800,
                        'bandwidth': '2x2.5',
                    },
                    {
                        'frequency': 2300,
                        'bandwidth': '2x15',
                    },
                    # {
                    #     'frequency': 2500,
                    #     'bandwidth': '2x10',
                    # },
                ],
                '5G': [
                    {
                        'frequency': 700,
                        'bandwidth': '2x5',
                    },
                    {
                        'frequency': 3500,
                        'bandwidth': '1x40',
                    },
                ]
            },
            'financials': {
                'wacc': 10.4, #<- what is the weighted average cost of capital for india? I'm assuming closer to 10% than 15%?
                'profit_margin': 10, # what is the profit margin for an MNO?
                'spectrum_coverage_baseline_usd_mhz_pop': 11.76, #what is the cost in USD per MHz per member of the population for coverage spectrum (<1GHz)?
                'spectrum_capacity_baseline_usd_mhz_pop': 3.09, #what is the cost in USD per MHz per member of the population for capacity spectrum (>1GHz)?
                'spectrum_baseline_cov_usd_mhz': 52920000,
                'spectrum_baseline_cap_usd_mhz': 13906667,
                'spectrum_cost_low': 50,
                'spectrum_cost_high': 50,
                'tax_low': 10,
                'tax_baseline': 22, #what is the baseline corporate tax rate in india?
                'tax_high': 40,
                'ops_and_acquisition_per_subscriber': 2, # what is the subscriber acquisition cost in India? Might be easier to just use 30% of the RAN annually for total operations costs?
                'administration_percentage_of_network_cost': 20
                },
            },
    }
