#경로지정
setwd("C:/Blood/R.Blood")
getwd()

#파일 불러오기
result<-read.csv("지역별헌혈특성.csv",header=TRUE)

#군집분석
install.packages("cluster")
library(cluster)
View(result)

result2<-hclust(dist(result),method="ave")
names(result2)
plot(result2)
plot(result2,hang=-1,labels=result2$ID)

#ctree를 이용하여 의사결정트리 생성
install.packages("party")
library(party)
#난수지정
set.seed(1234)
resultsplit<-sample(3,nrow(result),replace=TRUE,prob=c(0.4,0.3,0.3))
trainD<-result[resultsplit==1,]
testD<-result[resultsplit==2,]
rawD<-N3040~Jan+Feb+Mar+Apr+May+June+July+Aug+Set+Oct+Nov+Dec+place
trainModel<-ctree(rawD,data=trainD)
table(predict(trainModel),trainD$T)
print(trainModel)
