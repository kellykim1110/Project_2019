#경로지정
setwd("C:/Blood/R.Blood")
getwd()

#파일 불러오기
result<-read.csv("until20.csv",header=TRUE)

#빈도확인
table(result$winter,result$T)

#이름지정
result$winter2[result$winter==3]<-"many"
result$winter2[result$winter==2]<-"middle"
result$winter2[result$winter==1]<-"few"
result$T2[result$T==3]<-"from160,000"
result$T2[result$T==2]<-"from90,000"
result$T2[result$T==1]<-"to90,000"

table(result$winter2,result$T2)

#독립성분석
chisq.test(result$T2,result$winter2)

table(result$winter2,result$N3040)
chisq.test(result$winter2,result$N3040)
