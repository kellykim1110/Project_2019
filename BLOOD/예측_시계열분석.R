#경로설정
setwd("C:/Blood/R.Blood")
getwd()

#파일불러오기
##2015년부터 2018년까지 월별헌혈실적을 시간순으로 표기
##참조 : Month.csv
month<-read.csv("mon.csv",header=TRUE)

#ts함수를 이용하여 시계열자료 생성
mon<-ts(month,frequency=12,start=c(2005,1))
mon
#시각화
plot.ts(mon,main="Monthly Donors of Blood")

#decompose()함수를 이용하여 복합적인 이동평균을 사용하여 Tt(추세), St(신호,계절성), at(잡음)를 분리
mon_comp<-decompose(mon)
plot(mon_comp)

#계절성조절
plot.ts(mon-mon_comp$seasonal,main="Monthly Donors of Blood")

#auto.arima() 함수로 상수를 포함하는 과정을 자동화
auto.arima(mon)

#arima함수
mon_arima<-arima(mon,order=c(1,0,2),seasonal=list(order=c(0,1,1),period=12))
mon_arima

#패캐지 설정
install.packages("forecast")
library(forecast)

#예측하기
mon_fcast<-forecast(mon_arima)
mon_fcast
plot(mon_fcast,main="forecasts 2019&2020")
