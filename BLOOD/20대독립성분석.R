#경로지정
setwd("C:/Blood/R.Blood")
getwd()

#파일불러오기
result<-read.csv("until20.csv",header=TRUE)

#빈도확인
table(result$number,result$place)

#이름지정
result$number2[result$number==4]<-"from 250,000"
result$number2[result$number==3]<-"from 200,000"
result$number2[result$number==2]<-"from 100,000"
result$number2[result$number==1]<-"to 100,000"
result$place2[result$place==3]<-"from 12"
result$place2[result$place==2]<-"from 7"
result$place2[result$place==1]<-"to 6"
table(result$number2,result$place2)

#독립성분석
chisq.test(result$number2,result$place2)


result$T2[result$T==3]<-"from160,000"
result$T2[result$T==2]<-"from90,000"
result$T2[result$T==1]<-"to90,000"
table(result$T2,result$place2)
chisq.test(result$T2,result$place2)


result$n3040[result$N3040==3]<-"from650,000"
result$n3040[result$N3040==2]<-"from450,000"
result$n3040[result$N3040==1]<-"to450,000"
table(result$n3040,result$place2)
chisq.test(result$n3040,result$place2)
