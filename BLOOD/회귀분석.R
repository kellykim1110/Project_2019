#경로지정
setwd("C:/Blood/R.Blood")
getwd()
#파일불러오기
##peoplearea.csv : 지역별 특정헌혈자&헌혈의집 특징 
result<-read.csv("peoplearea.csv",header=TRUE)
View(result)

#회귀분석
##지역별 헌혈의 집 수에 대해 지역별 면적과 총인구수 회귀분석
result1<-lm(place~total_people+area,data=result)
result1
summary(result1)

##지역별 헌혈의 집 수에 대해 지역별 30,40대 헌혈자의 수(B34)와 인구수(P34) 회귀분석
result2<-lm(place~B34+P34,data=result)
result2
summary(result2)

##지역별 30,40대 헌혈자의 수(B34)에 대해 지역별 헌혈의 집 수와 지역별 30,40대 인구수(P34) 회귀분석
result3<-lm(B34~area+P34,data=result)
result3
summary(result3)

##지역별 헌혈의 집 수에 대해 지역별 10대의 헌혈자의 수(Teens)와 인구수(P10) 회귀분석
result4<-lm(place~Teens+P10,data=result)
result4
summary(result4)

##지역별 헌혈의 집 수에 대해 지역별 20대의 헌혈자의 수(Twenties)와 인구수(P20) 회귀분석
result5<-lm(place~Twenties+P20,data=result)
summary(result5)

