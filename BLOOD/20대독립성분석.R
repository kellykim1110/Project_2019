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
## 범주형 자료 분석 (categorical data test) 
## (1) 적합도 검정(goodness of fit test) : 관측값들이 어떤 이론적 분포를 따르고 있는지를 검정. 한 개의 요인을 대상으로 함 
## (2) 독립성 검정(test of independence) : 서로 다른 요인들에 의해 분할되어 있는 경우 그 요인들이 관찰값에 영향을 주고 있는지 아닌지, 요인들이 서로 연관이 있는지 없는지를 검정. 두 개의 요인을 대상으로 함.
## (3) 동질성 검정(test of homogeneity) : 관측값들이 정해진 범주 내에서 서로 비슷하게 나타나고 있는지를 검정. 속성 A, B를 가진 부모집단(subpopulation) 각각으로부터 정해진 표본의 크기만큼 자료를 추출하는 경우에 분할표에서 부모집단의 비율이 동일한가를 검정. 두 개의 요인을 대상으로 함.
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
