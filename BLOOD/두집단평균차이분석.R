#경로지정
setwd("C:/Blood/R.Blood")
getwd()

#파일불러오기
number<-read.csv("헌혈률과실제헌혈률.csv",header=TRUE)
number

number$percentage
number$real

p<-c(number$percentage)
r<-c(number$real)

#두 집단 평균차이 분석
wilcox.test(p,r,paired=TRUE,alter="greater",conf.int=TRUE,conf.level=0.95)

#조건에 맞는 데이터 추출
numbers<-subset(number,real!=99,c(percentage,real))
numbers
#데이터 개수
length(numbers$percentage)
length(numbers$real)

#평균
mean(numbers$percentage)
mean(numbers$real)

#F-검정
var.test(numbers$percentage,numbers$real,paired=TRUE)
