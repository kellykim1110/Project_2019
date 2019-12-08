install.packages("dplyr")
library(dplyr)
titanic<-read.csv("C:\\R\\RBasic-master\\RBasic-master\\R_Data\\train.csv")

Dat<-titanic%>%select(-Name,-Parch,-Ticket,-Fare,-Cabin,-PassengerId)
names(Dat)
table(Dat)

w<-Dat%>%filter(Sex=='female')
dim(w)
m<-Dat%>%filter(Sex=='male')
dim(m)
W<-w%>%select(Survived)
M<-m%>%select(Survived)
table(W)
table(M)

w<-w%>%filter(Sex=='female',Survived==1)
dim(w)
m<-m%>%filter(Sex=='male',Survived==1)
dim(m)

W<-w%>%select(Pclass)
M<-m%>%select(Pclass)
table(W)

table(M)


W1<-w%>%filter(Pclass==1)
M3<-m%>%filter(Pclass==3)
W<-W1%>%select(SibSp)
M<-M3%>%select(SibSp)
table(W)
table(M)


W1<-M3%>%filter(SibSp==0)
W<-W1%>%select(Embarked)
table(W)
W1<-W1%>%filter(Embarked=="S")
W<-ifelse(W1$Age<20,"1",
          ifelse(W1$Age<30,"2",
                 ifelse(W1$Age<40,"3","4")))
table(W)



install.packages(ggplot2)
library(ggplot2)
Dat<-titanic%>%mutate(Final_Most_Alive=ifelse(Embarked!='S',"Died",                             
                                            ifelse(SibSp!=0,"Died",                          
                                                     ifelse(Pclass!=1,"Died",                          
                                                              ifelse(Survived!=1,"Died",            
                                                                     ifelse(Sex=='male',"Died","Alive"))))),
                      Age_class=ifelse(Age<10,0,
                                       ifelse(Age<20,1,
                                              ifelse(Age<30,2,
                                                     ifelse(Age<40,3,
                                                            ifelse(Age<50,4,
                                                                   ifelse(Age<60,5,6)))))) )
Dat
ggplot(Dat,aes(x=Age_class,fill=Final_Most_Alive))+geom_bar()
table(Dat$Age_class)                          
table(Dat$Final_Most_Alive)
