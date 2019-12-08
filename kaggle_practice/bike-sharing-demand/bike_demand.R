#데이터 불러오기
df<-read.csv("C:\\Users\\cloud\\OneDrive\\바탕 화면\\2019_What_I_Do\\2019_R\\Rproject2019\\Bike_Sharing_Demand\\train.csv")

#for mutate() : 조건문을 가진 새로운 컬럼을 생성할 때 
install.packages("dplyr")
library(dplyr)

#컬럼명
names(df)
#빈도확인
table(df$datetime)


#그래프를 이용하여 어떤 상황에서 사용자가 많은지를 도출
##휴일이 자전거 수요에 미치는 영향
###새로운 컬럼 생성
df<-df%>%mutate(work=ifelse(workingday==0,0,
                              ifelse(holiday==1,0,1
                                     )))
df<-df%>%mutate(rest=ifelse(workingday==0,1,
                              ifelse(holiday==1,1,0
                              )))
###그래프 그리기
install.packages("ggplot2")
library(ggplot2)

p11=ggplot(data = df, aes(x = work, y = count,fill=casual)) + geom_col()+
  ggtitle("노동과 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p12=ggplot(data = df, aes(x = rest, y = count,fill=casual)) + geom_col()+
  ggtitle("휴일과 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))
#일을 하지 않는 휴일이 일하는 날보다 자전거 수요가 적었다.
#휴일에 비등록자의 자전거 수요량이 더 많다.



##기온이 자전거 수요에 미치는 영향
#(1)
p21=ggplot(data = df, aes(x = atemp, y = count,fill=season)) + geom_col()+
  ggtitle("체감기온과 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))


p22=ggplot(data = df, aes(x = temp, y = count, fill=season)) + geom_col()+
  ggtitle("기온과 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

#실제 기온과 체감기온 모두 30도 초반대가 수요가 제일 높았다.
#하지만 14~30도 사이의 체감기온이 30대 초반과 큰 차이가 있는 반면에
#14~30도 사이의 실제기온은 온도가 증가할수록 수요도 증가하지만 체감기온만큼 큰 폭의 차이는 없다.


#(2)
p23=ggplot(data = df, aes(x = atemp, y = count, fill=casual)) + geom_col()+
  ggtitle("체감기온과 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p24=ggplot(data = df, aes(x = temp, y = count, fill=casual)) + geom_col()+
  ggtitle("기온과 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))
#20도에서 30도사이에 비등록자들이 자전거 수요가 늘었다


#(3)
p25=ggplot(data = df, aes(y =casual, x = temp)) + geom_point()+
  ggtitle("기온과 비등록자 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p26=ggplot(data = df, aes(y =registered, x= temp)) + geom_point()+
  ggtitle("기온과 등록자 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))



p27=ggplot(data = df, aes(y=casual, x = atemp)) + geom_point()+
  ggtitle("체감기온과 비등록자 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p28=ggplot(data = df, aes(y =registered, x = atemp)) + geom_point()+
  ggtitle("체감기온과 등록자 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))


##계절이 자전거 수요에 미치는 영향
p3=ggplot(data = df, aes(x = season, y = count,fill=casual)) + geom_col()+
  ggtitle("계절과 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))
#봄에 자전거 수요가 가장적고 가을에 자전거 수요가 가장 많다

##습도가 자전거 수요에 미치는 영향
p4=ggplot(data = df, aes(x = humidity , y = count)) + geom_point()+
  ggtitle("습도와 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))
#습도와 자전거 수요는 관계가 없다.

##풍속이 자전거 수요에 미치는 영향
p51=ggplot(data = df, aes(x = windspeed, y = count,fill=casual)) + geom_col()+
  ggtitle("풍속과 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p52=ggplot(data = df, aes(x = windspeed, y = casual)) + geom_col()+
  ggtitle("풍속과 비등록자자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))
#풍속이 낮을수록 자전거 수요가 많다.
#풍속이 낮을수록 비등록자 자전거 수요가 많다.


##날씨가 자전거 수요에 미치는 영향

p6=ggplot(data = df,aes(x = weather, y = count,fill=casual)) + geom_col()+
  ggtitle("날씨와 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))
#날씨가 맑으면 자전거 수요가 많다



##시간이 자전거 수요에 미치는 영향

###for substr() : 문자 일부만 읽어주기 위해
install.packages("stringr")  
library(stringr)

df<-df%>%mutate(time=substr(df$datetime,11,13),
                month=substr(df$datetime,6,8),
                day=substr(df$datetime,9,11),
                Date=substr(df$datetime,0,10))

#날짜를 요일로 읽어주기
df$date<-weekdays(as.Date(df$Date))
table(df$date)

p71=ggplot(data = df,aes(x = time, y = count,fill=casual)) + geom_col()+
  ggtitle("시간대와 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p72=ggplot(data = df,aes(x = month, y = count,fill=casual)) + geom_col()+
  ggtitle("월별 자전거 수요")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p73=ggplot(data = df,aes(x = day, y = count,fill=casual)) + geom_col()+
  ggtitle("날짜와 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p77=ggplot(data = df,aes(x = date, y = count,fill=casual)) + geom_col()+
  ggtitle("요일과 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

#17일마다,6월마다, 17:00~18:00,토요일 자전거 수요 많아
#8일마다,1월마다, 2:00~5:00 , 일요일 자전거 수요 적어


p74=ggplot(data = df,aes(x = time, y = casual)) + geom_col()+
  ggtitle("시간대와 비등록자 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p75=ggplot(data = df,aes(x = month, y =casual)) + geom_col()+
  ggtitle("월별 비등록자 자전거 수요")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p76=ggplot(data = df,aes(x = day, y =casual)) + geom_col()+
  ggtitle("날짜와 비등록자 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))

p78=ggplot(data = df,aes(x = date, y =casual)) + geom_col()+
  ggtitle("요일과 비등록자 자전거 수요의 상관관계")+theme(plot.title=element_text( face="bold", size=10, vjust=2 ))


#4일마다, 7월마다, 14:00~17:00 토요일 자전거 수요 많아
#1일마다, 1월마다, 3:00~5:00 화,수요일 자전거 수요 적어


###for grid.arrange() : 그래프를 한번에 모아서 보여주기
install.packages('gridExtra')  
library(gridExtra)


grid.arrange(p11,p12, p21,p22,p23,p24,p25,p26,p27,p28, p3, p4,p51,p52,p6,p71,p72,p73,p74,p75,p76,p77,p78,
             ncol = 5, nrow = 5, top = "Bike_Sharing_Demand")

grid.arrange(p12, p21,p22,p23,p24, p3,p51,p6,p77,
            ncol = 3, nrow = 3, top = "Bike_Sharing_Demand")

###의미있는 데이터
grid.arrange(p12,p3,p51,p6,p71,p72,p73,p77, ncol = 2, nrow = 4, 
             top = "Bike_Sharing_Demand")


grid.arrange(p21,p23,p52,p74,p75,p76,p78, ncol = 2, nrow = 4, 
             top = "Bike_Sharing_Demand of non-registered user")


#자전거 수요는 
#사람들이 일을 할 때
#실제기온,체감기온이 30도 초반일때
#가을일때
#풍속이 낮을 때
#날씨가 맑을때 많다
#17일마다,6월마다, 17:00~18:00 자전거 수요 많아




###이용자 수를 비교하여 어떤 상황에서 사용자가 많은지를 도출


summary(df$count)    
#평균이상을 많다고 표현하자.

df<-df%>%mutate(users=ifelse(count>191.6,1,0))


#실제온도, 체감온도,풍속의 범위가 넓으므로 구간을 나누어 보자 
df<-df%>%mutate(tem=ifelse(temp<20,0,
                           ifelse(temp<25,1,
                                  ifelse(temp<34,2,3))))

df<-df%>%mutate(atem=ifelse(atemp<20,0,
                            ifelse(atemp<25,1,
                                   ifelse(atemp<30,2,
                                          ifelse(atemp<35,3,4)))))

df<-df%>%mutate(Wind=ifelse(windspeed<10,0,
                            ifelse(windspeed<20,1,
                                   ifelse(windspeed<30,2,3))))

names(df)


##어떤 상황에 전체 사용자가 많은 지를 알아보기 위해 
##전체 사용자가 평균이상일 때를 먼저 설정 
D<-df%>%filter(users==1)
###조건유무에 대한 빈도
dim(D)
###조건에 맞는 데이터의 날짜컬럼 선택
d<-D%>%select(date)
###빈도 확인
table(d)

D<-D%>%filter(date=='금요일')
dim(D)

d<-D%>%select(rest)
table(d)

D<-D%>%filter(rest==0)
dim(D)

d<-D%>%select(season)
table(d)

D<-D%>%filter(season==3)
dim(D)

d<-D%>%select(tem)
table(d)


D<-D%>%filter(tem==2)
dim(D)


d<-D%>%select(atem)
table(d)

D<-D%>%filter(atem==3)
dim(D)

d<-D%>%select(weather)
table(d)

D<-D%>%filter(weather==1)
dim(D)

d<-D%>%select(Wind)
table(d)

##총 이용자 수, 등록된 이용자 수, 비등록된 이용자 수로 나누어 비교
summary(df$count)
#summary(df$casual)
#summary(df$registered)


##다른 조건들에 비해 계절 같은 경우 
#봄일 때가 가을을 제외한 여름, 겨울보다 이용자가 훨씬 적었다.


#가을을 기준으로
D<-df%>%mutate(situation=ifelse(date!='금요일',0,
                                ifelse(rest!=0,0,
                                       ifelse(season==1,0,
                                              ifelse(tem!=2,0,
                                                     ifelse(atem!=3,0,
                                                            ifelse(weather!=1,0,
                                                                   ifelse(Wind!=1,0,1))))))),
               unregister=ifelse(casual<4,"1.more less",
                                 ifelse(casual<36,"2.less",
                                        ifelse(casual<49,"3.more","4.too more"))),
               register=ifelse(registered<36,"1.more less",
                               ifelse(registered<156,"2.less",
                                      ifelse(registered<222,"3.more","4.too more"))),
               people=ifelse(count<42,"1.more less",
                             ifelse(count<192,"2.less",
                                    ifelse(count<284,"3.more","4.too more"))))
summary(D)


D1=ggplot(D,aes(x=people,y=situation))+geom_col()+
  ggtitle("A relationship of number of total rentals and the situation")+theme(plot.title=element_text( face="bold", size=10, vjust=2,colour = "blue" ))


#D2=ggplot(D,aes(x=unregister,y=situation))+geom_col()+ggtitle("A relationship of number of registered non-user rentals initiated and the situation")+theme(plot.title=element_text( face="bold", size=10, vjust=2,colour = "blue" ))


#D3=ggplot(D,aes(x=register,y=situation))+geom_col()+ggtitle("A relationship of number of registered user rentals initiated and the situation")+theme(plot.title=element_text( face="bold", size=10, vjust=2,colour = "blue" ))



#봄을 기준으로
d<-df%>%mutate(situation=ifelse(date!='금요일',0,
                                ifelse(rest!=0,0,
                                       ifelse(season==1,0,
                                              ifelse(tem!=2,0,
                                                     ifelse(atem!=3,0,
                                                            ifelse(weather!=1,0,
                                                                   ifelse(Wind!=1,0,1))))))),
               unregister=ifelse(casual<4,"1.more less",
                                 ifelse(casual<36,"2.less",
                                        ifelse(casual<49,"3.more","4.too more"))),
               register=ifelse(registered<36,"1.more less",
                               ifelse(registered<156,"2.less",
                                      ifelse(registered<222,"3.more","4.too more"))),
               people=ifelse(count<42,"1.more less",
                             ifelse(count<192,"2.less",
                                    ifelse(count<284,"3.more","4.too more"))))


summary(d)


d1=ggplot(d,aes(x=people,y=situation))+geom_col()+
  ggtitle("A relationship of number of total rentals and the situation")+theme(plot.title=element_text( face="bold", size=10, vjust=2,colour = "red" ))


#d2=ggplot(d,aes(x=unregister,y=situation))+geom_col()+ggtitle("A relationship of number of registered non-user rentals initiated and the situation")+theme(plot.title=element_text( face="bold", size=10, vjust=2,colour = "red" ))



#d3=ggplot(d,aes(x=register,y=situation))+geom_col()+ggtitle("A relationship of number of registered user rentals initiated and the situation")+theme(plot.title=element_text( face="bold", size=10, vjust=2,colour = "red" ))




###결과

grid.arrange(D1,d1, ncol = 2, nrow = 1, 
             top = "Bike_Sharing_Demand of number of total rentals")

#grid.arrange(D2,d2, ncol = 1, nrow = 2, top = "Bike_Sharing_Demand of number of registered non-user rentals initiated")

#grid.arrange(D3,d3, ncol = 1, nrow = 2, top = "Bike_Sharing_Demand of number of registered user rentals initiated")

#결론 : 봄을 기준으로 잡았을 때 더 확연한 차이를 볼 수 있다.