###VISUALISE MODEL OUTPUTS###
# install.packages("tidyverse")
library(tidyverse)
library(ggpubr)

#get folder directory
folder <- dirname(rstudioapi::getSourceEditorContext()$path)
folder_inputs = file.path(folder, 'subscriptions', "data_inputs")

files = list.files(path=folder_inputs, pattern="*.csv")

data <- 
  do.call("rbind", 
          lapply(files, 
                 function(x) 
                   read.csv(file.path(folder_inputs, x), 
                            stringsAsFactors = FALSE)))

metro <- data[(data$category == "Metro"),]

metro = ggplot(metro, aes(x=year, y=penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=2.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2)) +
  geom_vline(xintercept=2020, linetype="dashed", color = "grey", size=.5) +
  annotate("text", x = 2018, y = 5, label = "Historical", angle = 0) +
  annotate("text", x = 2022, y = 5, label = "Forecast", angle = 0) +
  scale_x_continuous(expand = c(0, 0), limits = c(2010,2030), breaks = seq(2010,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), 
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(A) Subscriptions by Telecom Circle - Metro", 
       subtitle = "Historical: 2010-2020. Forecast: 2020-2030 ",
       x = NULL, y = "Unique Subscribers (%)") +
  guides(colour=guide_legend(ncol=3), shape=guide_legend(ncol=3)) +
  facet_grid(~category)

a <- data[(data$category == "A"),]

a = ggplot(a, aes(x=year, y=penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=2.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5)) +
  geom_vline(xintercept=2020, linetype="dashed", color = "grey", size=.5) +
  annotate("text", x = 2018, y = 5, label = "Historical", angle = 0) +
  annotate("text", x = 2022, y = 5, label = "Forecast", angle = 0) +
  scale_x_continuous(expand = c(0, 0), limits = c(2010,2030), breaks = seq(2010,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), 
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(B) Subscriptions by Telecom Circle - A", 
       subtitle = "Historical: 2010-2020. Forecast: 2020-2030 ",
       x = NULL, y = "Unique Subscribers (%)") +
  guides(colour=guide_legend(ncol=5), shape=guide_legend(ncol=5)) +
  facet_grid(~category)

b <- data[(data$category == "B"),]

b = ggplot(b, aes(x=year, y=penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=2.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5, 6, 7)) +
  geom_vline(xintercept=2020, linetype="dashed", color = "grey", size=.5) +
  annotate("text", x = 2018, y = 5, label = "Historical", angle = 0) +
  annotate("text", x = 2022, y = 5, label = "Forecast", angle = 0) +
  scale_x_continuous(expand = c(0, 0), limits = c(2010,2030), breaks = seq(2010,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), 
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(C) Subscriptions by Telecom Circle - B", 
       subtitle = "Historical: 2010-2020. Forecast: 2020-2030 ",
       x = NULL, y = "Unique Subscribers (%)") +
  guides(colour=guide_legend(ncol=7), shape=guide_legend(ncol=7)) +
  facet_grid(~category)

c <- data[(data$category == "C"),]

c = ggplot(c, aes(x=year, y=penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=2.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5, 6, 7)) +
  geom_vline(xintercept=2020, linetype="dashed", color = "grey", size=.5) +
  annotate("text", x = 2018, y = 5, label = "Historical", angle = 0) +
  annotate("text", x = 2022, y = 5, label = "Forecast", angle = 0) +
  scale_x_continuous(expand = c(0, 0), limits = c(2010,2030), breaks = seq(2010,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), 
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(C) Subscriptions by Telecom Circle - C", 
       subtitle = "Historical: 2010-2020. Forecast: 2020-2030 ",
       x = NULL, y = "Unique Subscribers (%)") +
  guides(colour=guide_legend(ncol=7), shape=guide_legend(ncol=7)) +
  facet_grid(~category)

combined <- ggarrange(metro, a, b, c,  
                      ncol = 2, nrow = 2)

path = file.path(folder, 'figures', 'a_subscriptions.png')
ggsave(path, units="in", width=10, height=10, dpi=300)
print(combined)
dev.off()

####################smartphones
folder <- dirname(rstudioapi::getSourceEditorContext()$path)

data <- read.csv(file.path(folder, '..', 'results', 'regional_annual_demand_technology_options.csv'))

data <- data[(data$confidence == 50),]

data = data[(
  data$scenario == 'S1_25_10_2' &
    data$strategy == '4G_epc_microwave_baseline_baseline_baseline_baseline'
),]

data <- select(data, tc_code, category, geotype, year, 
               population, total_population_with_smartphones)

data$geotype[data$geotype == 'suburban'] <- 'urban'
  
data = data %>%
  group_by(tc_code, category, geotype, year) %>%
  summarize(population = sum(population),
            smartphones = sum(total_population_with_smartphones))

data$geotype = factor(data$geotype,
                       levels=c("urban",
                                "rural"),
                       labels=c("Urban",
                                "Rural"))

data$sp_penetration = round(data$smartphones /
                              data$population * 100, 2) 

metro <- data[(data$category == "Metro"),]

metro = ggplot(metro, aes(x=year, y=sp_penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=2.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2)) +
  scale_x_continuous(expand = c(0, 0.2), limits = c(2020,2030), breaks = seq(2020,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), 
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(A) Smartphones by Telecom Circle - Metro", 
       subtitle = "Forecast: 2020-2030 ",
       x = NULL, y = "Smartphones (%)") +
  guides(colour=guide_legend(ncol=3), shape=guide_legend(ncol=3)) +
  facet_grid(~geotype)

a <- data[(data$category == "A"),]

a = ggplot(a, aes(x=year, y=sp_penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=2.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5)) +
  scale_x_continuous(expand = c(0, 0.2), limits = c(2020,2030), breaks = seq(2020,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), 
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(B) Smartphones by Telecom Circle - A", 
       subtitle = "Forecast: 2020-2030 ",
       x = NULL, y = "Smartphones (%)") +
  guides(colour=guide_legend(ncol=5), shape=guide_legend(ncol=5))+
  facet_grid(~geotype)

b <- data[(data$category == "B"),]

b = ggplot(b, aes(x=year, y=sp_penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=2.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5, 6, 7)) +
  scale_x_continuous(expand = c(0, 0.2), limits = c(2020,2030), breaks = seq(2020,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), 
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(C) Smartphones by Telecom Circle - B", 
       subtitle = "Forecast: 2020-2030 ",
       x = NULL, y = "Smartphones (%)") +
  guides(colour=guide_legend(ncol=7), shape=guide_legend(ncol=7)) +
  facet_grid(~geotype)

c <- data[(data$category == "C"),]

c = ggplot(c, aes(x=year, y=sp_penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=2.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5, 6, 7)) +
  scale_x_continuous(expand = c(0, 0.2), limits = c(2020,2030), breaks = seq(2020,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), 
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(C) Smartphones by Telecom Circle - C", 
       subtitle = "Forecast: 2020-2030 ",
       x = NULL, y = "Smartphones (%)") +
  guides(colour=guide_legend(ncol=7), shape=guide_legend(ncol=7)) +
  facet_grid(~geotype)

combined <- ggarrange(metro, a, b, c,  
                      ncol = 2, nrow = 2)

path = file.path(folder, 'figures', 'b_smartphones.png')
ggsave(path, units="in", width=10, height=10, dpi=300)
print(combined)
dev.off()

####################SUPPLY-DEMAND METRICS
folder <- dirname(rstudioapi::getSourceEditorContext()$path)

data <- read.csv(file.path(folder, '..', 'results', 'decile_results_technology_options.csv'))

data <- data[!(data$total_cost == "NA"),]

names(data)[names(data) == 'GID_0'] <- 'country'

#select desired columns
data <- select(data, scenario, strategy, confidence, decile, #population, area_km2,
               population_km2, sites_estimated_total, existing_network_sites,
               sites_estimated_total_km2, existing_network_sites_km2,
               total_phone_density_km2, total_sp_density_km2,
               mno_phone_density_on_network_km2, mno_sp_density_on_network_km2,
               total_revenue, total_cost, cost_per_network_user,
               # cost_per_sp_user
               )

data <- data[(data$confidence == 50),]

demand = data[(
  data$scenario == 'S1_25_10_2' &
  data$strategy == '4G_epc_microwave_baseline_baseline_baseline_baseline'
    ),]

demand <- select(demand, decile, population_km2,
                 total_phone_density_km2, mno_phone_density_on_network_km2, 
                 total_sp_density_km2, mno_sp_density_on_network_km2)

demand <- gather(demand, metric, value, population_km2:mno_sp_density_on_network_km2)

demand$metric = factor(demand$metric,
                     levels=c("population_km2",
                              "total_phone_density_km2",
                             "mno_phone_density_on_network_km2",
                             'total_sp_density_km2',
                             "mno_sp_density_on_network_km2"),
                       labels=c("Population\nDensity",
                                "Total\nPhone\nDensity",
                                "MNO\nPhone\nDensity",
                                "Total\nSmartphone\nDensity",
                                "MNO\nSmartphone\nDensity"))

demand <- demand[complete.cases(demand),]

demand_densities <- ggplot(demand, aes(x=decile, y=value, colour=metric, group=metric)) +
  geom_line() +
  scale_fill_brewer(palette="Spectral", name = expression('Cost Type'), direction=1) +
  theme( legend.position = "bottom") + #axis.text.x = element_text(angle = 45, hjust = 1),
  labs(colour=NULL,
       title = "(A) Demand-Side Density Metrics by Population Decile (2020)",
       # subtitle = "Population and user densities",
       x = "Population Decile", y = "Density (per km^2)") +
  scale_x_continuous(expand = c(0, 0.5), breaks = seq(0,100,20)) +
  scale_y_continuous(expand = c(0, 0)) + #, limits = c(0,20)) +
  theme(panel.spacing = unit(0.6, "lines"), plot.title = element_text(size=10)) + 
  expand_limits(y=0) +
  guides(colour=guide_legend(ncol=5)) #+
  # facet_wrap(~tc_code, scales = "free", ncol=5)

supply = data[(
  data$scenario == 'S1_25_10_2' &
    data$strategy == '4G_epc_microwave_baseline_baseline_baseline_baseline'
),]

supply <- select(supply, decile, sites_estimated_total_km2, existing_network_sites_km2)

supply <- gather(supply, metric, value, sites_estimated_total_km2:existing_network_sites_km2)

supply$metric = factor(supply$metric,
                       levels=c("sites_estimated_total_km2",
                                "existing_network_sites_km2"),
                       labels=c("Total\nSite\nDensity",
                                "Modeled\nMNO\nSite Density"))

supply <- supply[complete.cases(supply),]

supply_densities <- ggplot(supply, aes(x=decile, y=value, colour=metric, group=metric)) +
  geom_line() +
  scale_fill_brewer(palette="Spectral", name = expression('Cost Type'), direction=1) +
  theme( legend.position = "bottom") + #axis.text.x = element_text(angle = 45, hjust = 1),
  labs(colour=NULL,
       title = "(B) Supply-Side Density Metrics by Population Decile (2020)",
       # subtitle = "Cumulative cost reported by percentage of population covered",
       x = "Population decile", y = "Density (per km^2)") +
  scale_x_continuous(expand = c(0, 0.5), breaks = seq(0,100,20)) +
  scale_y_continuous(expand = c(0, 0)) + #, limits = c(0,20)) +
  theme(panel.spacing = unit(0.6, "lines"), plot.title = element_text(size=10)) + expand_limits(y=0) +
  guides(colour=guide_legend(ncol=2)) #+
  # facet_wrap(~tc_code, scales = "free", ncol=5)

demand_supply <- ggarrange(
  demand_densities, supply_densities, ncol = 1, nrow = 2, align = c("hv"))

#export to folder
path = file.path(folder, 'figures', 'c_demand_supply_panel.png')
ggsave(path,  units="in", width=5.4, height=6, dpi=300)
print(demand_supply)
dev.off()

####################TECHNOLOGIES BY DECILE
folder <- dirname(rstudioapi::getSourceEditorContext()$path)

data <- read.csv(file.path(folder, '..', 'results', 'decile_results_technology_options.csv'))

data <- data[!(data$total_cost == "NA"),]

data <- data[(data$confidence == 50),]

#select desired columns
data <- select(data, scenario, strategy, decile, area_km2, population, total_cost, total_revenue)

data$scenario = factor(data$scenario, levels=c("S1_25_10_2",
                                               "S2_200_50_5",
                                               "S3_400_100_10"),
                       labels=c("S1 (25 Mbps)",
                                "S2 (200 Mbps)",
                                "S3 (400 Mbps)"))

data <- data[order(data$scenario, data$strategy, data$decile),]

data1 <- select(data, scenario, strategy, decile, total_revenue)
data1 <- data1[(data1$strategy == "4G_epc_microwave_baseline_baseline_baseline_baseline"),]
data1$strategy <- "Revenue" 
names(data1)[names(data1) == 'total_revenue'] <- 'value'
data2 <- select(data, scenario, strategy, decile, total_cost)
names(data2)[names(data2) == 'total_cost'] <- 'value'
data <- rbind(data1, data2)
remove(data1, data2)

data$strategy = factor(data$strategy, levels=c("Revenue",
                                               "4G_epc_microwave_baseline_baseline_baseline_baseline",
                                               "4G_epc_fiber_baseline_baseline_baseline_baseline",
                                               "5G_nsa_microwave_baseline_baseline_baseline_baseline",
                                               "5G_sa_fiber_baseline_baseline_baseline_baseline"),
                       labels=c("Revenue",
                                "4G (Wireless)",
                                "4G (Fiber)",
                                "5G NSA (Wireless)",
                                "5G SA (Fiber)"))

data <- data[order(data$scenario, data$strategy, data$decile),]

data <- data %>%
  group_by(scenario, strategy) %>%
  mutate(cumulative_value_bn = cumsum(round(value / 1e9, 3)))

panel <- ggplot(data, aes(x=decile, y=cumulative_value_bn, colour=strategy, group=strategy)) + 
  geom_line() +
  scale_fill_brewer(palette="Spectral", name = expression('Cost Type'), direction=1) +
  theme(legend.position = "bottom") + #axis.text.x = element_text(angle = 45, hjust = 1), 
  labs(colour=NULL,
       title = "Viability of Technology Decisions (4G vs 5G & Fiber vs Microwave)",
       subtitle = "Cumulative cost reported by percentage of population covered",
       x = "Population Covered (%)", y = "Cumulative Cost (Billions $USD)") + 
  scale_x_continuous(expand = c(0, 0.75), breaks = seq(0,100,10)) + 
  scale_y_continuous(expand = c(0, 0)) + #, limits = c(0,20)) +  
  theme(panel.spacing = unit(0.6, "lines"), 
        axis.text.x = element_text(angle = 45, vjust = 1, hjust=1)) + expand_limits(y=0) +
  guides(colour=guide_legend(ncol=5)) +
  facet_wrap(~scenario, scales = "free", ncol=3)

path = file.path(folder, 'figures', 'd_results_technology_options_wrap.png')
ggsave(path, units="in", width=8, height=6, dpi=300)
print(panel)
dev.off()


####################TECHNOLOGIES BY DECILE
folder <- dirname(rstudioapi::getSourceEditorContext()$path)

data <- read.csv(file.path(folder, '..', 'results', 'decile_cost_results_technology_options.csv'))

data <- data[!(data$total_cost == "NA"),]
data <- data[(data$confidence == 50),]

#select desired columns
data <- select(data, scenario, strategy, confidence, decile, ran,
               backhaul_fronthaul, civils, core_network,
               ops_and_acquisition, spectrum_cost, tax)

data <- gather(data, asset, value, ran:tax)

data$scenario = factor(data$scenario, levels=c("S1_25_10_2",
                                               "S2_200_50_5",
                                               "S3_400_100_10"),
                       labels=c("S1",
                                "S2",
                                "S3"))

data$strategy = factor(data$strategy, levels=c(
                                               "4G_epc_microwave_baseline_baseline_baseline_baseline",
                                               "4G_epc_fiber_baseline_baseline_baseline_baseline",
                                               "5G_nsa_microwave_baseline_baseline_baseline_baseline",
                                               "5G_sa_fiber_baseline_baseline_baseline_baseline"),
                       labels=c(
                                "4G (Wireless)",
                                "4G (Fiber)",
                                "5G NSA (Wireless)",
                                "5G SA (Fiber)"))

data$combined <- paste(data$scenario, data$strategy, sep=": ")
unique(data$combined)
data$combined = factor(data$combined, levels=c(
  "S1: 4G (Wireless)",
  "S2: 4G (Wireless)",
  "S3: 4G (Wireless)",
  "S1: 4G (Fiber)",
  "S2: 4G (Fiber)",
  "S3: 4G (Fiber)",
  "S1: 5G NSA (Wireless)",
  "S2: 5G NSA (Wireless)",
  "S3: 5G NSA (Wireless)",
  "S1: 5G SA (Fiber)",
  "S2: 5G SA (Fiber)",
  "S3: 5G SA (Fiber)"
  ))

data$asset = factor(data$asset, levels=c(
   'tax', 'spectrum_cost', 'ops_and_acquisition', 'core_network',
   'civils', 'backhaul_fronthaul', 'ran'),
labels=c('Tax', 'Spectrum', 'Ops', 'Core', 'Civils', 'Backhaul', "RAN"))

technology_costs = ggplot(data, aes(x=decile, y=value/1e9, fill=asset)) +
  geom_bar(stat="identity") +
  theme(legend.position = 'right') +
  scale_x_continuous(expand = c(0, 0), breaks = seq(0,100,10)) +
  scale_y_continuous(expand = c(0, 0)) + #, limits = c(0, 29.9)
  labs(colour=NULL,
       title = "Cost Performance of Universal Broadband Strategies in India",
       subtitle = "Results reported by scenario, strategy and population decile",
       x = 'Population Decile', y = "Investment Cost ($USD Billions)", fill='Cost Type') +
  theme(panel.spacing = unit(0.6, "lines"), axis.text.x = element_text(angle = 45)) +
  expand_limits(y=0) +
  guides() +
  facet_wrap(~combined, scales = "free", ncol=3)

path = file.path(folder, 'figures', 'e_technology_cost_composition.png')
ggsave(path, units="in", width=10, height=10, dpi=300)
print(technology_costs)
dev.off()

####################TECHNOLOGIES PER USER COST
folder <- dirname(rstudioapi::getSourceEditorContext()$path)

data <- read.csv(file.path(folder, '..', 'results', 'decile_cost_results_technology_options.csv'))

data <- data[!(data$total_cost == "NA"),]
data <- data[(data$confidence == 50),]

data$ran = round(data$ran / data$mno_smartphones_on_network, 2)
data$backhaul_fronthaul = round(data$backhaul_fronthaul / data$mno_smartphones_on_network, 2)
data$civils = round(data$civils / data$mno_smartphones_on_network, 2)
data$core_network = round(data$core_network / data$mno_smartphones_on_network, 2)
data$ops_and_acquisition = round(data$ops_and_acquisition / data$mno_smartphones_on_network, 2)
data$spectrum_cost = round(data$spectrum_cost / data$mno_smartphones_on_network, 2)
data$tax = round(data$tax / data$mno_smartphones_on_network, 2)

#select desired columns
data <- select(data, scenario, strategy, confidence, decile, ran,
               backhaul_fronthaul, civils, core_network,
               ops_and_acquisition, spectrum_cost, tax)

data <- gather(data, asset, value, ran:tax)

data$scenario = factor(data$scenario, levels=c("S1_25_10_2",
                                               "S2_200_50_5",
                                               "S3_400_100_10"),
                       labels=c("S1",
                                "S2",
                                "S3"))

data$strategy = factor(data$strategy, levels=c(
  "4G_epc_microwave_baseline_baseline_baseline_baseline",
  "4G_epc_fiber_baseline_baseline_baseline_baseline",
  "5G_nsa_microwave_baseline_baseline_baseline_baseline",
  "5G_sa_fiber_baseline_baseline_baseline_baseline"),
  labels=c(
    "4G (Wireless)",
    "4G (Fiber)",
    "5G NSA (Wireless)",
    "5G SA (Fiber)"))

data$combined <- paste(data$scenario, data$strategy, sep=": ")

data$combined = factor(data$combined, levels=c(
  "S1: 4G (Wireless)",
  "S2: 4G (Wireless)",
  "S3: 4G (Wireless)",
  "S1: 4G (Fiber)",
  "S2: 4G (Fiber)",
  "S3: 4G (Fiber)",
  "S1: 5G NSA (Wireless)",
  "S2: 5G NSA (Wireless)",
  "S3: 5G NSA (Wireless)",
  "S1: 5G SA (Fiber)",
  "S2: 5G SA (Fiber)",
  "S3: 5G SA (Fiber)"
))

data$asset = factor(data$asset, levels=c(
  'tax', 'spectrum_cost', 'ops_and_acquisition', 'core_network',
  'civils', 'backhaul_fronthaul', 'ran'),
  labels=c('Tax', 'Spectrum', 'Ops', 'Core', 'Civils', 'Backhaul', "RAN"))

technology_costs = ggplot(data, aes(x=decile, y=value, fill=asset)) +
  geom_bar(stat="identity") +
  theme(legend.position = 'right') +
  scale_x_continuous(expand = c(0, 0), breaks = seq(0,100,10)) +
  scale_y_continuous(expand = c(0, 0)) + #, limits = c(0, 29.9)
  labs(colour=NULL,
       title = "Cost per Smartphone User for Universal Broadband in India",
       subtitle = "Results reported by scenario, strategy and population decile",
       x = 'Population Decile', y = "Per Smartphone Cost ($USD)", fill='Cost Type') +
  theme(panel.spacing = unit(0.6, "lines"), axis.text.x = element_text(angle = 45)) +
  expand_limits(y=0) +
  guides() +
  facet_wrap(~combined, scales = "free", ncol=3)

path = file.path(folder, 'figures', 'f_per_user_technology_cost_composition.png')
ggsave(path, units="in", width=10, height=10, dpi=300)
print(technology_costs)
dev.off()
