#경로지정
setwd("C:/Blood/R.Blood")
getwd()
#파일불러오기
##give : 헌혈
##take : 수헐
Givetake<-read.csv("월별헌혈수혈실적.csv",header=TRUE)

#시각화
qplot(month,give,data=g,size=1)+geom_smooth()

#데이터프레임설정
g<-data.frame(month=c(1,2,3,4,5,6,7,8,9,10,11,12),give=c(221066,193180 ,241362 ,221319,246117 ,211546 ,228749 ,215089 ,212804 ,224639 ,248903 ,216837))
g
t<-data.frame(month=c(1,2,3,4,5,6,7,8,9,10,11,12),take=c(380232,318059,363517,351250,361018,347549,362276,357887,337155,366077,368834,363908
))
t

#시각화
install.packages("ggplot2")
library(ggplot2)
qplot(month,give,data=g,shape=factor(cyl))+geom_smooth()   #?
qplot(month,take,data=t,size=1)+geom_smooth()
