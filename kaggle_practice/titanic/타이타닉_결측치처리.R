##결측치 처리
#데이터 불러오기
titanic<-read.csv("C:\\Users\\Desktop\\RBasic-master\\R_Data\\train.csv")

#is.na(데이터 셋)
is.na(titanic)

#결측치 개수 확인
table(is.na(titanic))

table(is.na(titanic$Pclass))
table(is.na(titanic$Emabrked))
table(is.na(titanic$Fare))

##결측치가 포함되면 정상적인 연산
mean(titanic$Pclass)

library(dplyr)

titanic

titanic%>%filter(!is.na(Pclass))
titanic%>%filter(!is.na(Embarked))
titanic%>%filter(!is.na(Fare))
titanic%>%filter(!is.na(Cabin))
titanic%>%filter(!is.na(Pclass),!is.na(Embarked),!is.na(Fare),!is.na(Cabin))

###
mean(df$Fare,na.rm=T)
min(df$Fare,na.rm=T)

###이상치 찾고 처리
outlier<-data.frame(Pclass=c(1,2,3,4,55,4,1,1,2),family=c(1,2,3,1,2,3,1,1,1))
outlier

library(ggplot2)
p1<-ggplot(outlier,aes(x=Pclass))+geom_bar()
p2<-ggplot(outlier,aes(x=family))+geom_bar()

install.packages("gridExtra")
library(gridExtra)
grid.arrange(p1,p2,ncol=2,nrow=1)

##범주형은 히스토그램
##수치형은 막대그래프

#Pclass안에서 데이터 값이 1,2,3인 것을 논리형으로 나타내기
outlier$Pclass%in%c(1,2,3)  

install.packages("Hmisc")
library(Hmisc)

`%notin%`<-Negate(`%in%`)
outlier$Pclass%in%c(1,2,3)
outlier$Pclass

outlier$family
outlier[(outlier$Pclass%in%c(1,2,3)),]
outlier[!(outlier$Pclass%in%c(1,2,3)),]
outlier[outlier$Pclass%notin%c(1,2,3),]

outlier$family
outlier$family%in%c(1,2)
outlier[!(outlier$family%in%c(1,2)),]
outlier[outlier$family%notin%c(1,2),]

table(outlier$Pclass)
outlier[!(outlier$Pclass%in%c(1,2,3)),'Pclass']=1
outlier[c(4,5),]
outlier
