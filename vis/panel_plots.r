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

metro_ph = ggplot(metro, aes(x=year, y=penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=1.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2)) +
  geom_vline(xintercept=2020, linetype="dashed", color = "grey", size=.5) +
  scale_x_continuous(expand = c(0, 0), limits = c(2010,2030), breaks = seq(2010,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100), breaks = seq(0,100,20)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=12),
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(A) Subscriptions by Telecom Circle - Metro", 
       x = NULL, y = "Unique Subscribers (%)") +
  guides(colour=guide_legend(ncol=3), shape=guide_legend(ncol=3)) 

a_ph <- data[(data$category == "A"),]

a_ph = ggplot(a_ph, aes(x=year, y=penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=1.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5)) +
  geom_vline(xintercept=2020, linetype="dashed", color = "grey", size=.5) +
  scale_x_continuous(expand = c(0, 0), limits = c(2010,2030), breaks = seq(2010,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100), breaks = seq(0,100,20)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=12),
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(C) Subscriptions by Telecom Circle - A", 
       x = NULL, y = "Unique Subscribers (%)") +
  guides(colour=guide_legend(ncol=5), shape=guide_legend(ncol=5)) 

b_ph <- data[(data$category == "B"),]

b_ph = ggplot(b_ph, aes(x=year, y=penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=1.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5, 6, 7)) +
  geom_vline(xintercept=2020, linetype="dashed", color = "grey", size=.5) +
  scale_x_continuous(expand = c(0, 0), limits = c(2010,2030), breaks = seq(2010,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100), breaks = seq(0,100,20)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=12),
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(E) Subscriptions by Telecom Circle - B", 
       x = NULL, y = "Unique Subscribers (%)") +
  guides(colour=guide_legend(ncol=7), shape=guide_legend(ncol=7)) 

c_ph <- data[(data$category == "C"),]

c_ph = ggplot(c_ph, aes(x=year, y=penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=1.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5, 6, 7)) +
  geom_vline(xintercept=2020, linetype="dashed", color = "grey", size=.5) +
  scale_x_continuous(expand = c(0, 0), limits = c(2010,2030), breaks = seq(2010,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100), breaks = seq(0,100,20)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=12),
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(G) Subscriptions by Telecom Circle - C", 
       x = NULL, y = "Unique Subscribers (%)") +
  guides(colour=guide_legend(ncol=7), shape=guide_legend(ncol=7)) 

####################smartphones
folder <- dirname(rstudioapi::getSourceEditorContext()$path)

data <- read.csv(file.path(folder, '..', 'results', 'regional_annual_demand_technology_options.csv'))

data <- data[(data$confidence == 50),]

data = data[(
  data$scenario == 'S1_25_10_2' &
    data$strategy == '4G_epc_wireless_baseline_baseline_baseline_baseline'
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

metro_sp <- data[(data$category == "Metro"),]

metro_sp = ggplot(metro_sp, aes(x=year, y=sp_penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=1.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2)) +
  scale_x_continuous(expand = c(0, 0.2), limits = c(2020,2030), breaks = seq(2020,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100), breaks = seq(0,100,20)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=12),
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(B) Smartphones by Telecom Circle - Metro", 
       x = NULL, y = "Smartphones (%)") +
  guides(colour=guide_legend(ncol=3), shape=guide_legend(ncol=3)) +
  facet_grid(~geotype)

a_sp <- data[(data$category == "A"),]

a_sp = ggplot(a_sp, aes(x=year, y=sp_penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=1.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5)) +
  scale_x_continuous(expand = c(0, 0.2), limits = c(2020,2030), breaks = seq(2020,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100), breaks = seq(0,100,20)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=12),
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(D) Smartphones by Telecom Circle - A", 
       x = NULL, y = "Smartphones (%)") +
  guides(colour=guide_legend(ncol=5), shape=guide_legend(ncol=5)) +
  facet_grid(~geotype)

b_sp <- data[(data$category == "B"),]

b_sp = ggplot(b_sp, aes(x=year, y=sp_penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=1.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5, 6, 7)) +
  scale_x_continuous(expand = c(0, 0.2), limits = c(2020,2030), breaks = seq(2020,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100), breaks = seq(0,100,20)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=12),
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(F) Smartphones by Telecom Circle - B", 
       x = NULL, y = "Smartphones (%)") +
  guides(colour=guide_legend(ncol=7), shape=guide_legend(ncol=7)) +
  facet_grid(~geotype)

c_sp <- data[(data$category == "C"),]

c_sp = ggplot(c_sp, aes(x=year, y=sp_penetration, group=tc_code)) +
  geom_point(aes(shape=tc_code, color=tc_code), size=1.5) +
  geom_line(aes(color=tc_code)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4, 5, 6, 7)) +
  scale_x_continuous(expand = c(0, 0.2), limits = c(2020,2030), breaks = seq(2020,2030,2)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0,100), breaks = seq(0,100,20)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=12),
        legend.position = "bottom", legend.title=element_blank()) +
  labs(title = "(H) Smartphones by Telecom Circle - C", 
       x = NULL, y = "Smartphones (%)") +
  guides(colour=guide_legend(ncol=7), shape=guide_legend(ncol=7)) +
  facet_grid(~geotype)

####################

combined <- ggarrange(metro_ph, metro_sp, a_ph, a_sp, b_ph, b_sp, c_ph, c_sp,  
                      ncol = 2, nrow = 4)

path = file.path(folder, 'figures', 'a_forecasts.png')
ggsave(path, units="in", width=8, height=11, dpi=300)
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
               # total_phone_density_km2, total_sp_density_km2,
               mno_phone_density_on_network_km2, mno_sp_density_on_network_km2,
               total_revenue, total_cost, cost_per_network_user,
               )

data <- data[(data$confidence == 50),]

demand = data[(
  data$scenario == 'S1_25_10_2' &
  data$strategy == '4G_epc_wireless_baseline_baseline_baseline_baseline'
    ),]

demand <- select(demand, decile, population_km2,
                 # total_phone_density_km2, total_sp_density_km2,
                 mno_phone_density_on_network_km2, mno_sp_density_on_network_km2)

demand <- gather(demand, metric, value, population_km2:mno_sp_density_on_network_km2)

demand$metric = factor(demand$metric,
                     levels=c("population_km2",
                             'mno_phone_density_on_network_km2',
                             "mno_sp_density_on_network_km2"),
                       labels=c("Population\nDensity",
                                "MNO\nPhone\nDensity",
                                "MNO\nSmart-\nphone\nDensity"))

demand <- demand[complete.cases(demand),]

demand_densities <- ggplot(demand, aes(x=decile, y=value, group=metric)) +
  geom_point(aes(shape=metric, color=metric), size=1.5) +
  geom_line(aes(color=metric)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4)) +
  scale_fill_brewer(palette="Spectral", direction=1) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=7),
        legend.position = "bottom", legend.title=element_blank(), text = element_text(size=6)) +
  labs(title = "(A) Demand-Side Density Metrics by \nPopulation Decile (2020)",
       x = "Population Decile", y = "Density (per km^2)") + expand_limits(y=0) +
  guides(colour=guide_legend(ncol=3), shape=guide_legend(ncol=3)) +
  scale_x_continuous(expand = c(0, 0.5), breaks = seq(0,100,10)) +
  scale_y_continuous(expand = c(0, 0))

supply = data[(
  data$scenario == 'S1_25_10_2' &
    data$strategy == '4G_epc_wireless_baseline_baseline_baseline_baseline'
),]

supply <- select(supply, decile, sites_estimated_total_km2, existing_network_sites_km2)

supply <- gather(supply, metric, value, sites_estimated_total_km2:existing_network_sites_km2)

supply$metric = factor(supply$metric,
                       levels=c("sites_estimated_total_km2",
                                "existing_network_sites_km2"),
                       labels=c("Total\nSite\nDensity",
                                "Modeled\nMNO\nSite Density"))

supply <- supply[complete.cases(supply),]

supply_densities <- ggplot(supply, aes(x=decile, y=value, group=metric)) +
  geom_point(aes(shape=metric, color=metric), size=1.5) +
  geom_line(aes(color=metric)) +
  scale_shape_manual(values=c(0, 1)) +
  scale_fill_brewer(palette="Spectral", direction=1) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title = element_text(size=7),
        legend.position = "bottom", legend.title=element_blank(), text = element_text(size=6)) +
  labs(title = "(B) Supply-Side Density Metrics by \nPopulation Decile (2020)",
       x = "Population Decile", y = "Density (per km^2)") +
  guides(colour=guide_legend(ncol=2), shape=guide_legend(ncol=2)) +
  scale_x_continuous(expand = c(0, 0.5), breaks = seq(0,100,10)) +
  scale_y_continuous(expand = c(0, 0))

demand_supply <- ggarrange(
  demand_densities, supply_densities, ncol = 2, nrow = 1, align = c("hv"))

#export to folder
path = file.path(folder, 'figures', 'b_baseline.png')
ggsave(path,  units="in", width=5, height=2.5, dpi=300)
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
                                               "S2_50_20_5",
                                               "S3_100_30_10"),
                       labels=c("S1 (2-25 Mbps)",
                                "S2 (5-50 Mbps)",
                                "S3 (10-100 Mbps)"))

data <- data[order(data$scenario, data$strategy, data$decile),]

data1 <- select(data, scenario, strategy, decile, total_revenue)
data1 <- data1[(data1$strategy == "4G_epc_wireless_baseline_baseline_baseline_baseline"),]
data1$strategy <- "Revenue" 
names(data1)[names(data1) == 'total_revenue'] <- 'value'
data2 <- select(data, scenario, strategy, decile, total_cost)
names(data2)[names(data2) == 'total_cost'] <- 'value'
data <- rbind(data1, data2)
remove(data1, data2)
unique(data$strategy)
data$strategy = factor(data$strategy, levels=c("Revenue",
                       "4G_epc_wireless_baseline_baseline_baseline_baseline",
                       "4G_epc_fiber_baseline_baseline_baseline_baseline",
                       "5G_nsa_wireless_baseline_baseline_baseline_baseline",
                       "5G_nsa_fiber_baseline_baseline_baseline_baseline"),
                       labels=c("Revenue",
                                "4G (Wireless)",
                                "4G (Fiber)",
                                "5G NSA (Wireless)",
                                "5G NSA (Fiber)"))

data <- data[order(data$scenario, data$strategy, data$decile),]

data <- data %>%
  group_by(scenario, strategy) %>%
  mutate(cumulative_value_bn = cumsum(round(value / 1e9, 3)))

panel <- ggplot(data, aes(x=decile, y=cumulative_value_bn, group=strategy)) + 
  geom_point(aes(shape=strategy, color=strategy), size=1.5) +
  geom_line(aes(color=strategy)) +
  scale_shape_manual(values=c(0, 1, 2, 3, 4)) +
  scale_fill_brewer(palette="Spectral", direction=1) +
  theme(legend.position = "bottom") +
  labs(title = "Viability of Technology Decisions",
       subtitle = "Cumulative cost and revenue reported by percentage of population covered",
       x = "Population Covered (%)", y = "Cumulative Cost (Billions $USD)") +
  scale_x_continuous(expand = c(0, 0.75), breaks = seq(0,100,10)) +
  scale_y_continuous(expand = c(0, 0), limits = c(0, 108), breaks = seq(0,108,20)) +
  theme(panel.spacing = unit(0.6, "lines"), legend.title=element_blank(),
        axis.text.x = element_text(angle = 45, vjust = 1, hjust=1)) + expand_limits(y=0) +
  guides(shape=guide_legend(ncol=5), colour=guide_legend(ncol=5)) +
  facet_wrap(~scenario, scales = "free", ncol=3)

path = file.path(folder, 'figures', 'c_technology_viability.png')
ggsave(path, units="in", width=8, height=4, dpi=300)
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
                                               "S2_50_20_5",
                                               "S3_100_30_10"),
                       labels=c("S1 (2-25 Mbps)",
                                "S2 (5-50 Mbps)",
                                "S3 (10-100 Mbps)"))

data$strategy = factor(data$strategy, levels=c(
  "4G_epc_wireless_baseline_baseline_baseline_baseline",
  "4G_epc_fiber_baseline_baseline_baseline_baseline",
  "5G_nsa_wireless_baseline_baseline_baseline_baseline",
  "5G_nsa_fiber_baseline_baseline_baseline_baseline"),
  labels=c(
    "4G (Wireless)",
    "4G (Fiber)",
    "5G NSA (Wireless)",
    "5G NSA (Fiber)"))

data$combined <- paste(data$scenario, data$strategy, sep=": ")

data$combined = factor(data$combined, levels=c(
  "S1 (2-25 Mbps): 4G (Wireless)",
  "S2 (5-50 Mbps): 4G (Wireless)",
  "S3 (10-100 Mbps): 4G (Wireless)",
  "S1 (2-25 Mbps): 4G (Fiber)",
  "S2 (5-50 Mbps): 4G (Fiber)",
  "S3 (10-100 Mbps): 4G (Fiber)",
  "S1 (2-25 Mbps): 5G NSA (Wireless)",
  "S2 (5-50 Mbps): 5G NSA (Wireless)",
  "S3 (10-100 Mbps): 5G NSA (Wireless)",
  "S1 (2-25 Mbps): 5G NSA (Fiber)",
  "S2 (5-50 Mbps): 5G NSA (Fiber)",
  "S3 (10-100 Mbps): 5G NSA (Fiber)"
))

data$asset = factor(data$asset, levels=c(
  'tax', 'spectrum_cost', 'ops_and_acquisition', 'core_network',
  'civils', 'backhaul_fronthaul', 'ran'),
  labels=c('Tax', 'Spectrum', 'Ops', 'Core', 'Civils', 'Backhaul', "RAN"))

totals <- data %>%
  select(combined, decile, value) %>%
  group_by(combined, decile) %>%
  summarize(total = round(sum(value)/1e9, 1))

technology_costs = ggplot(data, aes(x=decile, y=value/1e9, fill=asset)) +
  geom_bar(stat="identity") +
  theme(legend.position = 'right') +
  scale_x_continuous(expand = c(0, 0), breaks = seq(0,100,10)) +
  scale_y_continuous(expand = c(0, 0), breaks = seq(0,30,5), limits = c(0, 30)) +
  labs(colour=NULL,
       title = "Cost Performance of Universal Broadband Strategies",
       subtitle = "Results reported by scenario, strategy and population decile",
       x = 'Population Decile', y = "Investment Cost ($USD Billions)", fill='Cost Type') +
  theme(panel.spacing = unit(0.6, "lines"), axis.text.x = element_text(angle = 45)) +
  expand_limits(y=0) +
  guides() +
  geom_text(
    aes(decile, total + 2, label = total, fill = NULL), 
    size=2.5, data = totals) + 
  facet_wrap(~combined, scales = "free", ncol=3) 

path = file.path(folder, 'figures', 'd_technology_cost_composition.png')
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
                                               "S2_50_20_5",
                                               "S3_100_30_10"),
                       labels=c("S1 (2-25 Mbps)",
                                "S2 (5-50 Mbps)",
                                "S3 (10-100 Mbps)"))

data$strategy = factor(data$strategy, levels=c(
  "4G_epc_wireless_baseline_baseline_baseline_baseline",
  "4G_epc_fiber_baseline_baseline_baseline_baseline",
  "5G_nsa_wireless_baseline_baseline_baseline_baseline",
  "5G_nsa_fiber_baseline_baseline_baseline_baseline"),
  labels=c(
    "4G (Wireless)",
    "4G (Fiber)",
    "5G NSA (Wireless)",
    "5G NSA (Fiber)"))

data$combined <- paste(data$scenario, data$strategy, sep=": ")

data$combined = factor(data$combined, levels=c(
  "S1 (2-25 Mbps): 4G (Wireless)",
  "S2 (5-50 Mbps): 4G (Wireless)",
  "S3 (10-100 Mbps): 4G (Wireless)",
  "S1 (2-25 Mbps): 4G (Fiber)",
  "S2 (5-50 Mbps): 4G (Fiber)",
  "S3 (10-100 Mbps): 4G (Fiber)",
  "S1 (2-25 Mbps): 5G NSA (Wireless)",
  "S2 (5-50 Mbps): 5G NSA (Wireless)",
  "S3 (10-100 Mbps): 5G NSA (Wireless)",
  "S1 (2-25 Mbps): 5G NSA (Fiber)",
  "S2 (5-50 Mbps): 5G NSA (Fiber)",
  "S3 (10-100 Mbps): 5G NSA (Fiber)"
))

data$asset = factor(data$asset, levels=c(
  'tax', 'spectrum_cost', 'ops_and_acquisition', 'core_network',
  'civils', 'backhaul_fronthaul', 'ran'),
  labels=c('Tax', 'Spectrum', 'Ops', 'Core', 'Civils', 'Backhaul', "RAN"))


totals <- data %>%
  select(combined, decile, value) %>%
  group_by(combined, decile) %>%
  summarize(total = round(sum(value)))

technology_costs = ggplot(data, aes(x=decile, y=value, fill=asset)) +
  geom_bar(stat="identity") +
  theme(legend.position = 'right') +
  scale_x_continuous(expand = c(0, 0), breaks = seq(0,100,10)) +
  scale_y_continuous(expand = c(0, 0), breaks = seq(0,3500,500), limits = c(0, 3500)) + 
  labs(colour=NULL,
       title = "Cost per Smartphone User for Universal Broadband",
       subtitle = "Results reported by scenario, strategy and population decile",
       x = 'Population Decile', y = "Per Smartphone Cost ($USD)", fill='Cost Type') +
  theme(panel.spacing = unit(0.6, "lines"), axis.text.x = element_text(angle = 45)) +
  expand_limits(y=0) +
  guides() +
  geom_text(
    aes(decile, total + 225, label = total, fill = NULL), 
    size=2.5, data = totals) + 
  facet_wrap(~combined, scales = "free", ncol=3)

path = file.path(folder, 'figures', 'e_per_user_technology_cost_composition.png')
ggsave(path, units="in", width=10, height=10, dpi=300)
print(technology_costs)
dev.off()


####################TECHNOLOGIES PER USER COST
folder <- dirname(rstudioapi::getSourceEditorContext()$path)

data <- read.csv(file.path(folder, '..', 'results', 'decile_cost_results_policy_options.csv'))

data <- data[!(data$total_cost == "NA"),]

data <- data[(data$confidence == 50),]

#select desired columns
data <- select(data, scenario, strategy, decile, area_km2, population, total_cost, total_revenue)

data$scenario = factor(data$scenario, levels=c("S1_25_10_2",
                                               "S2_50_20_5",
                                               "S3_100_30_10"),
                       labels=c("S1 (2-25 Mbps)",
                                "S2 (5-50 Mbps)",
                                "S3 (10-100 Mbps)"))

data$strategy_tech <- ifelse(grepl("4G_epc_wireless", data$strategy, ignore.case = T), "4G (Wireless)",
                             ifelse(grepl("4G_epc_fiber", data$strategy, ignore.case = T), "4G (Fiber)",
                                    ifelse(grepl("5G_nsa_wireless", data$strategy, ignore.case = T), "5G NSA (Wireless)",
                                           ifelse(grepl("5G_nsa_fiber", data$strategy, ignore.case = T), "5G NSA (Fiber)", "NA"))))

data$combined <- paste(data$scenario, data$strategy_tech, sep=": ")

data$combined = factor(data$combined, levels=c(
  "S1 (2-25 Mbps): 4G (Wireless)",
  "S2 (5-50 Mbps): 4G (Wireless)",
  "S3 (10-100 Mbps): 4G (Wireless)",
  "S1 (2-25 Mbps): 4G (Fiber)",
  "S2 (5-50 Mbps): 4G (Fiber)",
  "S3 (10-100 Mbps): 4G (Fiber)",
  "S1 (2-25 Mbps): 5G NSA (Wireless)",
  "S2 (5-50 Mbps): 5G NSA (Wireless)",
  "S3 (10-100 Mbps): 5G NSA (Wireless)",
  "S1 (2-25 Mbps): 5G NSA (Fiber)",
  "S2 (5-50 Mbps): 5G NSA (Fiber)",
  "S3 (10-100 Mbps): 5G NSA (Fiber)"
))

data <- data[order(data$scenario, data$strategy, data$decile),]

data1 <- select(data, combined, scenario, strategy, decile, total_revenue)
data1 <- data1[(
  data1$strategy == "4G_epc_fiber_baseline_baseline_0_baseline" & data1$scenario == "S1 (2-25 Mbps)" | 
    data1$strategy == "4G_epc_fiber_baseline_baseline_0_baseline" & data1$scenario == "S2 (5-50 Mbps)" | 
    data1$strategy == "4G_epc_fiber_baseline_baseline_0_baseline" & data1$scenario == "S3 (10-100 Mbps)" | 
    data1$strategy == "4G_epc_wireless_baseline_baseline_0_baseline" & data1$scenario == "S1 (2-25 Mbps)" | 
    data1$strategy == "4G_epc_wireless_baseline_baseline_0_baseline" & data1$scenario == "S2 (5-50 Mbps)" | 
    data1$strategy == "4G_epc_wireless_baseline_baseline_0_baseline" & data1$scenario == "S3 (10-100 Mbps)" | 
    data1$strategy == "5G_nsa_fiber_baseline_baseline_0_baseline" & data1$scenario == "S1 (2-25 Mbps)" | 
    data1$strategy == "5G_nsa_fiber_baseline_baseline_0_baseline" & data1$scenario == "S2 (5-50 Mbps)" | 
    data1$strategy == "5G_nsa_fiber_baseline_baseline_0_baseline" & data1$scenario == "S3 (10-100 Mbps)" | 
    data1$strategy == "5G_nsa_wireless_baseline_baseline_0_baseline" & data1$scenario == "S1 (2-25 Mbps)" | 
    data1$strategy == "5G_nsa_wireless_baseline_baseline_0_baseline" & data1$scenario == "S2 (5-50 Mbps)" | 
    data1$strategy == "5G_nsa_wireless_baseline_baseline_0_baseline" & data1$scenario == "S3 (10-100 Mbps)" 
),]
data1$strategy <- "Revenue"
names(data1)[names(data1) == 'total_revenue'] <- 'value'
data2 <- select(data, combined, scenario, strategy, decile, total_cost)
names(data2)[names(data2) == 'total_cost'] <- 'value'
data <- rbind(data1, data2)
remove(data1, data2)

data$strategy_var <- ifelse(grepl("Revenue", data$strategy, ignore.case = T), 'Revenue',
                            ifelse(grepl("_0_", data$strategy, ignore.case = T), 'Baseline',
                                   ifelse(grepl("_20_", data$strategy, ignore.case = T), '-20%',
                                          ifelse(grepl("_40_", data$strategy, ignore.case = T), '-40%',
                                                 ifelse(grepl("_60_", data$strategy, ignore.case = T), '-60%',
                                                        ifelse(grepl("_80_", data$strategy, ignore.case = T), '-80%',
                                                               ifelse(grepl("_100_", data$strategy, ignore.case = T), '-100%',"NA")))))))

data = subset(data, subset = strategy_var %in% c(
  'Revenue',
  'Baseline', 
  '-20%',
  '-40%',
  '-60%',
  '-80%',
  '-100%'
))

data$strategy_var = factor(data$strategy_var, levels=c(
  'Revenue',
  'Baseline', 
  '-20%',
  '-40%',
  '-60%',
  '-80%',
  '-100%'
))

data = select(data, combined, strategy_var, decile, value)

data <- data %>%
  group_by(combined, strategy_var) %>%
  mutate(cumulative_value_bn = cumsum(round(value / 1e9, 3)))

data$linestyle = '1'
data$linestyle[data$strategy_var == 'Revenue'] <- '2'

panel = ggplot(data, aes(decile, cumulative_value_bn, colour=strategy_var, 
                          linetype=strategy_var, shape=strategy_var)) +
  geom_point(size=1) + geom_line() +
  scale_linetype_manual("", values=c(1,20,20,20,20,20,20)) +
  scale_shape_manual("", values=c(17,16,16,16,16,16,16)) + 
  scale_colour_discrete("") +
  theme(legend.position = "right") +
  labs(title = "Sensitivity Analysis of Spectrum Costs and Universal Broadband Viability",
       subtitle = "Cumulative cost and revenue reported by percentage of population covered",
       x = "Population Covered (%)",
       y = "Cumulative Cost (Billions $USD)",
       color='Decrease', shape='Decrease') +
  scale_x_continuous(expand = c(0, 0), breaks = seq(0,100,10)) +
  scale_y_continuous(expand = c(0, 0), breaks = seq(0,108,10)) + #limits = c(0, 108), 
  theme(panel.spacing = unit(0.6, "lines"), 
        axis.text.x = element_text(angle = 45, vjust = 1, hjust=1)) + 
  guides(shape=guide_legend(ncol=1), colour=guide_legend(ncol=1), linetype=guide_legend(ncol=1)) +
  facet_wrap(~combined, scales = "free", ncol=3)

path = file.path(folder, 'figures', 'f_spectrum_sensitivity.png')
ggsave(path, units="in", width=10, height=10, dpi=300)
print(panel)
dev.off()
