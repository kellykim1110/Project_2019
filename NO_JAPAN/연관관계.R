install.packages("readxl")
library(readxl)

#파일읽기
df<-read_excel("C:\\Users\\cloud\\Anaconda_src\\No_Japan\\id_and_nouns_twitter_data_2019-07-01_to_2019-09-09.xlsx")
library(dplyr)
df%>%head()

install.packages("arules")
library(arules)
str(df)
table(df$id)

df_list<-split(df$noun,df$id)
df_transaction<-as(df_list,"transactions")
df_transaction

summary(df_transaction)
#image(df_transaction) 

rules<-apriori(df_transaction,parameter = list(supp=0.03,conf=0.6))
summary(rules) #189개의 규칙생성

rule_list<-as.data.frame(inspect(rules))
rule_list<-rule_list[order(rule_list$lift, decreasing=TRUE), ]
rule_list  ###

install.packages("arulesViz")
library(arulesViz)
plot(rules)

###지지도(SUPPORT)
#전체 거래에서 특정 물품 A와 B가 동시에 거래되는 비중으로,
#해당 규칙이 얼마나 의미가 있는 규칙인지를 보여줍니다.

###신뢰도(CONFIDENCE)
#A를 포함하는 거래 중 A와 B가 동시에 거래되는 비중으로,
#A라는 사건이 발생했을 때 B가 발생할 확률이 얼마나 높은지를 말해줍니다.

###향상도(LIFT)
#A와 B가 동시에 거래된 비중을 A와B가 서로 독립된 사건일때 동시에 거래된 비중으로 나눈 값입니다.  
#즉, A와 B가 우연에 의해서 같이 거래된 확률보다 A와 B 사이의 관계가 얼마나 더 끈끈한지(?)를 보는 지표입니다.


plot(rules,method="grouped")
plot(rules,method="graph",interactive=TRUE,control=list(type="items"))
