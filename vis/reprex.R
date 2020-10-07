scenario = c('A','A','A','A','A','A','A','A','A','A','A','A')
strategy = c('A','A','A','A','A','A','A','A','A','A','A','A')
decile = c(0,0,0,0,0,0,10,10,10,10,10,10)
asset = c('A','A','A','B','B','B','A','A','A','B','B','B')
value = c(10,40,60,20,50,90,10,40,60,20,50,90)
confidence = c('lower','mean','upper','lower','mean','upper','lower','mean','upper','lower','mean','upper')

data = data.frame(scenario, strategy, decile, asset, value, confidence)







wide <- select(data, scenario, strategy, confidence, decile, asset, value)
wide <- spread(wide, confidence, value)

ggplot(wide, aes(x=decile, y=mean, fill=asset)) + 
  facet_grid(strategy~scenario)



scenario = c('A','A','A','A')
strategy = c('A','A','A','A')
decile = c(0,0,10,10)
asset = c('A','B','A','B')
mean = c(30,50,20,10)

data = data.frame(scenario, strategy, decile, asset, mean)

scenario = c('A','A','A','A')
strategy = c('A','A','A','A')
decile = c(0,10)
lower = c(10,10)
upper = c(100,100)

error_bars = unique(data.frame(scenario, strategy, decile, lower, upper))

merged = merge(data, error_bars, all.x=T)

ggplot(merged, aes(x=factor(decile), y=mean, fill=asset, group=scenario)) +    
  geom_bar(stat="identity") + facet_grid(strategy~scenario) +   
  geom_errorbar(aes(ymin = lower, ymax = upper), width = 0.25)





ggplot(merged, aes(x=decile, y=mean, fill=asset)) + 
  geom_bar(stat="identity") +
  facet_grid(strategy~scenario) +
  geom_errorbar(aes(ymin = lower, ymax = upper), width = 0.25)


scenario = c('A','A','A','A')
strategy = c('A','A','A','A')
decile = c(0,0,10,10)
asset = c('A','B','A','B')
lower = c(50,50,60, 60)
mean = c(30,30,50, 50)
upper = c(85,85,150, 150)
data = data.frame(scenario, strategy, decile, asset, lower, mean, upper)

ggplot(data, aes(x=factor(decile), y=mean, fill=asset, group=scenario)) +    
  geom_bar(stat="identity") + facet_grid(strategy~scenario) +   
  geom_errorbar(aes(ymin = lower, ymax = upper), width = 0.25)


















scenario = c('A','A','A','A')
strategy = c('A','A','A','A')
decile = c(0,0,10,10)
asset = c('A','B','A','B')
lower = c(10,20,10, 15)
mean = c(30,50,60, 70)
upper = c(70,90,86,90)
data = data.frame(scenario, strategy, decile, asset, lower, mean, upper)




library(ggplot2)
library(dplyr)

data %>% 
  mutate(lower = lower - mean, upper = upper - mean) %>%
  group_by(scenario, strategy, decile) %>% 
  arrange(rev(asset), by.group = TRUE) %>%
  mutate(mean2 = cumsum(mean), lower = lower + mean2, upper = upper + mean2) %>%
  ggplot(aes(x = decile, y = mean, fill = asset)) + 
  geom_bar(stat = "identity") +
  facet_grid(strategy ~ scenario) +
  geom_errorbar(aes(y = mean2, ymin = lower, ymax = upper), width = 2,
                position = position_dodge(width = 2)) +
  geom_point(aes(y = mean2), position = position_dodge(width = 2))








