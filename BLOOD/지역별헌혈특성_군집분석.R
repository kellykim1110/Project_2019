setwd("C:\\Users\\cloud\\OneDrive\\바탕 화면\\2019_What_I_Do\\Blood\\R.Blood")
getwd()
result<-read.csv("지역별헌혈특성.csv",header=TRUE)
install.packages("cluster")
library(cluster)
View(result)

result2<-hclust(dist(result),method="ave")
names(result2)
plot(result2)
plot(result2,hang=-1,labels=result2$ID)

install.packages("party")
library(party)
set.seed(1234)
resultsplit<-sample(3,nrow(result),replace=TRUE,prob=c(0.4,0.3,0.3))
trainD<-result[resultsplit==1,]
testD<-result[resultsplit==2,]
rawD<-N3040~Jan+Feb+Mar+Apr+May+June+July+Aug+Set+Oct+Nov+Dec+place
trainModel<-ctree(rawD,data=trainD)
table(predict(trainModel),trainD$T)
print(trainModel)
