#참고한 블로그 https://coding-law.tistory.com/30


df<-read.csv("C:\\Users\\cloud\\Downloads\\6_si.xlsx_190925\\dd.csv")
df<-as.data.frame(df)

install.packages("ggmap") 
library(ggmap)
install.packages("ggplot2")
library(ggplot2)
install.packages("raster")
library(raster)
install.packages("rgeos")
library(rgeos)
install.packages("maptools")
library(maptools)
install.packages("rgdal")
library(rgdal)

korea<-shapefile("TL_SCCO_CTPRVN.shp")
korea<-spTransform(korea,CRS("+proj=longlat"))
korea
korea_map<-fortify(korea)
library(dplyr)
korea_map$id%>%tail()
colnames(korea_map)
merge_result<-merge(korea_map,df,by="id")
merge_result
merge_result$시도별%>%head()

g1<-ggplot() + geom_polygon(data=merge_result, aes(x=long, y=lat, group=group, fill=X2014))
g2<-ggplot() + geom_polygon(data=merge_result, aes(x=long, y=lat, group=group, fill=X2015))
g3<-ggplot() + geom_polygon(data=merge_result, aes(x=long, y=lat, group=group, fill=X2016))
g4<-ggplot() + geom_polygon(data=merge_result, aes(x=long, y=lat, group=group, fill=X2017))

g1+scale_fill_gradient(low="green",high = "red")
g2+scale_fill_gradient(low="green",high = "red")
g3+scale_fill_gradient(low="green",high = "red")
g4+scale_fill_gradient(low="green",high = "red")
