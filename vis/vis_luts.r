###plot capacity lookup tables
# install.packages("tidyverse")
library(tidyverse)
library(plyr)
library(ggpubr)
#####################

#get folder directory
folder <- dirname(rstudioapi::getSourceEditorContext()$path)

#get path to full tables via the data folder
full_tables <- file.path(folder, '..', 'data', 'intermediate', 'luts', 'full_tables')

#get a list of all files in the folder ending in .csv
myfiles = list.files(path=full_tables, pattern="*.csv", full.names=TRUE)

#import data for all files in file list
data = ldply(myfiles, read_csv)

#select the ISD of 10000m to plot
data = data[data$inter_site_distance_m == 8800,]

# data = data[!(data$environment == 'urban' & data$r_distance > 10000),]

data = data[!(data$sinr_dB > 50),]

#turn env into factor and relabel
data$environment = factor(data$environment, levels=c("urban",
                                                     "suburban",
                                                     "rural"),
                          labels=c("Urban",
                                   "Suburban",
                                   "Rural"))

data$generation = factor(data$generation, levels=c("5G",
                                                   "4G"),
                         labels=c("5G (4x4 MIMO)", 
                                  "4G (2x2 MIMO)"
                         ))

data$frequency_GHz = factor(data$frequency_GHz, 
                            levels=c(0.7, 
                                     0.8, 
                                     # 0.85, 
                                     # 1.70, 
                                     1.80, 
                                     # 1.90, 
                                     # 2.30, 
                                     2.50, 
                                     # 2.60, 
                                     3.5),
                            labels=c("0.7 GHZ",
                                     "0.8 GHZ",
                                     # "0.85 GHZ",
                                     # "1.7 GHZ",
                                     "1.8 GHZ",
                                     # "1.9 GHZ",
                                     # "2.3 GHZ",
                                     "2.5 GHZ",
                                     # "2.6 GHZ",
                                     "3.5 GHZ"))

data = data[complete.cases(data),]

#subset the data for plotting
data = select(data, environment, generation, frequency_GHz, sinr_dB,
              r_distance, spectral_efficiency_bps_hz)

test = data

test$r_distance <- 
  cut(test$r_distance, 
      breaks = c(0, 1000, 2000, 3000, 4000, 5000),
      labels = c("<1 km", "1-2 km", "2-3 km", "3-4 km", "4-5 km"),
      include.lowest = TRUE)

sinr = ggplot(test, aes(x=r_distance, y=sinr_dB, colour=factor(frequency_GHz))) + 
  geom_boxplot() + 
  theme(legend.position="bottom") + guides(colour=guide_legend(ncol=5)) +
  labs(title = '(A) SINR vs User Distance From the Cell Site (n=1776)', 
       subtitle = 'Results reported by settlement type and cellular generation (10 km ISD)',
       x = 'Distance (km)', y='SINR (dB)', colour='Frequency') +
  facet_grid(generation~environment)

spectral_efficiency = ggplot(test, 
   aes(x=r_distance, y=spectral_efficiency_bps_hz, colour=factor(frequency_GHz))) + 
  geom_boxplot() + 
  # scale_x_continuous(expand = c(0, 0)) + scale_y_continuous(expand = c(0, 0)) +
  theme(legend.position="bottom") + guides(colour=guide_legend(ncol=7)) +
  labs(title = '(B) Spectral Efficiency vs User Distance From the Cell Site (n=1776)', 
       subtitle = 'Results reported by settlement type and cellular generation (10 km ISD)',
       x = 'Distance (km)', y='Spectral Efficiency (Bps/Hz)', colour='Frequency') +
  facet_grid(generation~environment)

combined <- ggarrange(sinr, spectral_efficiency, 
                      ncol = 1, nrow = 2,
                      common.legend = TRUE, 
                      legend='bottom' 
                      # heights=c(3.5, 5)
)

path = file.path(folder, 'figures', 'tukey.png')
ggsave(path, units="in", width=8, height=10, dpi=300)
print(combined)
dev.off()




# sinr = ggplot(data, aes(x=r_distance/1000, 
#                         y=sinr_dB, 
#                         colour=factor(frequency_GHz))) + 
#   geom_point(size=0.2) +
#   geom_smooth(formula=y~x, method='loess', size=.5) +
#   scale_x_continuous(expand = c(0, 0)) + scale_y_continuous(expand = c(0, 0)) +
#   theme(legend.position="bottom") + guides(colour=guide_legend(ncol=7)) +
#   labs(title = '(A) SINR vs User Distance From the Cell Site', 
#        subtitle = 'Results reported by settlement type and cellular generation',
#        x = 'Distance (km)', y='SINR (dB)', colour='Frequency') +
#   facet_grid(generation~environment)
# 
# spectral_efficiency = ggplot(data, aes(x=r_distance/1000, 
#                                        y=spectral_efficiency_bps_hz, 
#                                        colour=factor(frequency_GHz))) + 
#   geom_point(size=0.2) +
#   geom_smooth(formula=y~x, method='loess', size=.5) +
#   scale_x_continuous(expand = c(0, 0)) + scale_y_continuous(expand = c(0, 0)) +
#   theme(legend.position="bottom") + guides(colour=guide_legend(ncol=7)) +
#   labs(title = '(B) Spectral Efficiency vs User Distance From the Cell Site', 
#        subtitle = 'Results reported by settlement type and cellular generation',
#        x = 'Distance (km)', y='Spectral Efficiency (Bps/Hz)', colour='Frequency') +
#   facet_grid(generation~environment)
# 
# combined <- ggarrange(sinr, spectral_efficiency, 
#                       ncol = 1, nrow = 2,
#                       common.legend = TRUE, 
#                       legend='bottom' 
#                       # heights=c(3.5, 5)
# )
# 
# path = file.path(folder, 'figures', 'panel.png')
# ggsave(path, units="in", width=8, height=10, dpi=300)
# print(combined)
# dev.off()
# 
# 
# #get folder directory
# folder <- dirname(rstudioapi::getSourceEditorContext()$path)
# 
# #get path to lut 
# lut <- read.csv(file.path(folder, 'modulation_and_coding_lut.csv'))
# 
# #select variables
# lut = select(lut, generation, spectral.efficiency, sinr)
# 
# lut$generation = factor(lut$generation, levels=c("5G",
#                                                  "4G"),
#                         labels=c("5G (4x4 MIMO)", 
#                                  "4G (2x2 MIMO)"
#                         ))
# 
# lut = lut[complete.cases(lut),]
# 
# #plot
# spectral_efficiency = ggplot(lut, aes(x=sinr, y=spectral.efficiency, 
#                                       colour=factor(generation))) +
#   geom_line() +
#   scale_x_continuous(expand = c(0, 0)) + 
#   scale_y_continuous(expand = c(0, 0)) +
#   theme(legend.position="bottom") + guides(colour=guide_legend(ncol=4)) +
#   labs(title = 'Spectral Efficiency vs Signal-to-Interference-plus-Noise Ratio (SINR)', 
#        subtitle = 'Results reported by for each cellular generation',
#        x = 'Signal-to-Interference-plus-Noise Ratio (dB)', y='Bps/Hz', colour='Frequency') 
# 
# path = file.path(folder, 'figures', 'panel.png')
# ggsave(path, units="in", width=7, height=8, dpi=300)
# print(spectral_efficiency)
# dev.off()
