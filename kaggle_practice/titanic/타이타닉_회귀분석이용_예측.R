install.packages("Amelia")
library(Amelia)
## 팩캐지 설치 안될때  .libpath("C:\\Program Files\\R\\R-3.6.1\\library")

#stringsAsFactors  범주형 결정 유무

titanic_train<-read.csv("C:\\Users\\202-006\\Desktop\\RBasic-master\\R_Data\\titanic\\train.csv",na.strings=c("NA",""),stringsAsFactors = F)
titanic_test<-read.csv("C:\\Users\\202-006\\Desktop\\RBasic-master\\R_Data\\titanic\\test.csv",na.strings=c("NA",""),stringsAsFactors = F)
titanic_gender<-read.csv("C:\\Users\\202-006\\Desktop\\RBasic-master\\R_Data\\titanic\\gender_submission.csv",na.strings=c("NA",""),stringsAsFactors = F)
dim(titanic_train);dim(titanic_test);dim(titanic_gender)
names(titanic_train)
names(titanic_test)


missmap(titanic_train)
missmap(titanic_test)
colSums(is.na(titanic_train))
colSums(is.na(titanic_test))

quantile(titanic_train$Age)  #만약 'na.rm'이 FALSE라면 결측값들과 NaN은 허용되지 않습니다
quantile(titanic_train$Age,na.rm = T)
#중앙값 28


##'Age'결측치 없애기
titanic_train[ is.na(titanic_train$Age),'Age']=median(titanic_train$Age, na.rm = T)
titanic_test[ is.na(titanic_test$Age),"Age" ]=median(titanic_test$Age, na.rm = T)
#detach(titanic_train)

colSums(is.na(titanic_train))
colSums(is.na(titanic_test))


##'Embarked'결측치 수정
table(titanic_train$Embarked,useNA = "always")
table(titanic_test$Embarked,useNA = "always")
#가장 큰 값으로 대체
titanic_train[ is.na(titanic_train$Embarked),'Embarked']="S"

##Fare결측치 제거
titanic_test[ is.na(titanic_test$Fare),'Fare']=median(titanic_test$Fare, na.rm = T)

colSums(is.na(titanic_train))
colSums(is.na(titanic_test))

##모델 만들기
m<-glm(Survived~Pclass+Age+SibSp,family = binomial,data=titanic_train)
summary(m)

pred<-predict(m,newdata = titanic_test,type="response")
pred
##범주형으로 수정
pred<-as.integer(pred>0.5)
pred

names(titanic_gender)
titanic_gender["Survived"]=pred

#파일로 만들기
write.csv(titanic_gender,file="first_gender.csv",row.names=F)
list.files(path=".")

####실습####
m1<-glm(Survived~Age+Embarked+SibSp+Sex,family = binomial,data=titanic_train)
summary(m)

pred<-predict(m,newdata = titanic_test,type="response")
pred
##범주형으로 수정
pred<-as.integer(pred>0.5)
pred

names(titanic_gender)
titanic_gender["Survived"]=pred

#파일로 만들기
write.csv(titanic_gender,file="Second_gender.csv",row.names=F)
list.files(path=".")


#######################################################################

###우리가 임의로 예측하기
##입력데이터가 100일 때 
##입력테이터를 70만 해주고 나머지 30을 출력데이터로 넣어줘서 예측시키기, 예측 정확도 측정


install.packages("caret")
install.packages("randomForest")

library(Amelia)
library(caret)
library(dplyr)
library(randomForest)


titanic_train<-read.csv("C:\\Users\\202-006\\Desktop\\RBasic-master\\R_Data\\titanic\\train.csv",na.strings=c("NA",""),stringsAsFactors = F)
titanic_test<-read.csv("C:\\Users\\202-006\\Desktop\\RBasic-master\\R_Data\\titanic\\test.csv",na.strings=c("NA",""),stringsAsFactors = F)
titanic_gender<-read.csv("C:\\Users\\202-006\\Desktop\\RBasic-master\\R_Data\\titanic\\gender_submission.csv",na.strings=c("NA",""),stringsAsFactors = F)

###데이터 처리
names(titanic_test)
titanic_test$Survived<-NA
all<-rbind(titanic_train,titanic_test)
dim(all)
colSums(is.na(all))


##범주형 변환
all$Sex<-as.factor(all$Sex)
all$Survived<-as.factor(all$Survived)
all$Pclass<-as.factor(all$Pclass)
str(all)

##추가 파생변수
all$PclassSex[all$Pclass=='1'&all$Sex=="male"]<-'P1$Male'
all$PclassSex[all$Pclass=='2'&all$Sex=="male"]<-'P2$Male'
all$PclassSex[all$Pclass=='3'&all$Sex=="male"]<-'P3$Male'
all$PclassSex[all$Pclass=='1'&all$Sex=="female"]<-'P1$Female'
all$PclassSex[all$Pclass=='2'&all$Sex=="female"]<-'P2$Female'
all$PclassSex[all$Pclass=='3'&all$Sex=="female"]<-'P3$Female'

all%>%group_by(PclassSex)%>%summarise(n=n(), mean_Age=mean(Age,na.rm=T), median_Age=median(Age,na.rm=T))

all[is.na(all$Embarked),"Embarked"]="s"
all[is.na(all$Fare),"Fare"]=median(all$Fare,na.rm=T)

#만든 파생변수를 중앙값으로 치환하자
all[is.na(all$Age)&all$PclassSex=='P1Female',"Age"]=36
all[is.na(all$Age)&all$PclassSex=='P2Female',"Age"]=28
all[is.na(all$Age)&all$PclassSex=='P3Female',"Age"]=22
all[is.na(all$Age)&all$PclassSex=='P1Male',"Age"]=42
all[is.na(all$Age)&all$PclassSex=='P1Male',"Age"]=29.5
all[is.na(all$Age)&all$PclassSex=='P1Male',"Age"]=25
colSums(is.na(all))

##'Age'결측치 없애기
all[ is.na(all$Age),'Age']=median(all$Age, na.rm = T)
colSums(is.na(all))

##데이터 나누기(일반)
all$Embarked<-as.factor(all$Embarked)
trainclean<-all[!is.na(all$Survived), ]
testclean<-all[!is.na(all$Survived), ]

#데이터 나누기(출력데이터 만들기)
#7:3
idx<-sample(1:nrow(trainclean),
            size=nrow(trainclean)*0.7,replace=F)
train_tr<-trainclean[idx, ]
train_test<-trainclean[-idx, ]

#testclean:
M<-glm(Survived~Pclass+Sex,family=binomial,data=train_tr)
pred<-predict(M,newdata = train_test,type="response")
pred<-as.integer(pred>0.5)
pred

real<-train_test[ ,'Survived']
#pred
xt=xtabs(~pred+real)
xt



install.packages("e1071")
library(caret)
library(e1071)


pred<-as.factor(pred)
real<-as.factor(real)

confusionMatrix(pred,real)
str(train_tr)
train_tr$PclassSex<-as.factor(train_tr$PclassSex)
train_test$PclassSex<-as.factor(train_test$PclassSex)

library(randomForest)

M1<-randomForest(Survived~Pclass+Sex+PclassSex+SibSp+Age+Fare+Embarked, data=train_tr)
summary(M1)

#수치형
# rf_pred<-predict(M1,newdata = train_test,type = c("prob")) 
rf_pred<-predict(M1,newdata = train_test,type = c("class")) #범주형
rf_pred[0:15]

rf_pred<-as.factor(rf_pred)
real<-as.factor(real)
confusionMatrix(pred,real) #Accuracy : 0.7724  

########################################################################