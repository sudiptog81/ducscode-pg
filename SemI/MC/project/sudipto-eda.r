# install.packages(c('readxl'))

library(readxl)

data <- read_excel("NFHS_5_Factsheets_Data.xlsx")
total_data <- data[data$Area == 'Total',]
total_data <- data[data$`States/UTs` != 'India',]
total_data <- subset(total_data, select=-c(Area))
#ibrary(dplyr)
#library(tidyr)
#total_data %>% 
#  mutate_if(is.numeric, ~replace_na(.,mean(., na.rm = TRUE)))

View(total_data)

delivery_care_data <- subset(total_data, select=c(1, 54:60))
delivery_care_data[c(2:8)] <- sapply(delivery_care_data[c(2:8)], as.numeric)

View(delivery_care_data)
summary(delivery_care_data)

library(ggplot2)
library(maptools)
library(rgeos)
library(ggmap)

shp <- readShapeSpatial('India_State_Boundary.shp')
plot(shp)
shp$Name

shp.f <- fortify(shp, region="Name")
delivery_care_data$id = delivery_care_data$`States/UTs`
delivery_care_data$id[delivery_care_data$id == 'Tamil Nadu'] <- 'Tamilnadu'
delivery_care_data$id[delivery_care_data$id == 'Maharastra'] <- 'Maharashtra'
delivery_care_data$id[delivery_care_data$id == 'Chhattisgarh'] <- 'Chhattishgarh'
delivery_care_data$id[delivery_care_data$id == 'Telangana'] <- 'Telengana'
delivery_care_data$id[delivery_care_data$id == 'Andaman & Nicobar Islands'] <- 'Andaman & Nicobar'

merge.shp.coef <- merge(shp.f, delivery_care_data, by="id")
d <- merge.shp.coef[order(merge.shp.coef$order), ]

library(pracma)
library(stringr)
ctr <- 0
for (col in names(delivery_care_data)[2:8]) {
    ctr <- ctr + 1
  
    ggplot() +
      geom_polygon(data = shp.f,
                   aes(x = long, y = lat, group = group), 
                   color = "black", size = 0.25) + 
      geom_polygon(data = d,
                   aes(x = long, y = lat, group = group, fill = d[[col]]), 
                   color = "black", size = 0.25) + 
      coord_map()+
      scale_fill_viridis_c(name='', option = "magma") +
      labs(title=str_glue('{col}'))
    ggsave(str_glue('map-{ctr}.png'))
}

ctr <- 0
for (col in names(delivery_care_data)[2:8]) {
ctr <- ctr + 1
ggplot(delivery_care_data, aes(x=.data[[col]])) + ggtitle(col) + 
geom_histogram(aes(y = ..density..), colour = 1, fill = "#FF6666") +
  geom_density(lwd = 1.2,
               linetype = 2,
               colour = 1)
ggsave(str_glue('hist-{ctr}.png'))
}

library(ggplot2)
library(GGally)
ggpairs(delivery_care_data[2:8], cardinality_threshold = 37)
ggsave('correlations.png')

ctr <- 0
for (col in names(delivery_care_data)[2:8]) {
ctr <- ctr + 1
ggplot(data=delivery_care_data, aes(x=.data[[col]], y=id)) +
  geom_bar(stat="identity", width=0.5)
ggsave(str_glue('bar-{ctr}.png'))
}

