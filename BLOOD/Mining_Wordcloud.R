#경로지정
getwd()
setwd("C:/Blood/R.Blood")

#KoNLP 생성
install.packages("KoNLP")
library(KoNLP)

#워드 클라우드
install.packages("wordcloud")
library(wordcloud)

#사전 생성
useSejongDic()
user_d<-data.frame("혈소판 성분헌혈","ncn")
buildDictionary(ext_dic="sejong",user_dic=user_d)

#파일불러오기
txt<-file("blood.txt",blocking=F)
text<-readLines(txt)
close(txt)
blood<-sapply(text,extractNoun,USE.NAMES=F)
blood
head(unlist(blood),30)
f<-unlist(blood)
blood<-Filter(function(x){nchar(x)>=2},f)
textcount<-table(blood)
head(sort(textcount,decreasing=T),30)
palete<-brewer.pal(9,"Set1")
x11()
wordcloud(names(textcount),freq=textcount,scale=c(5,1),rot.per=0.25,min.freq=56,random.order=F,random.color=T,colors=palete)
