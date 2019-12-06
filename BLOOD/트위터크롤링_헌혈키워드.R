getwd()
setwd("C:/Blood/R.Blood")
getwd()
install.packages(c("twitteR","ROAuth", "base64enc"))
library(twitteR)
library(ROAuth)
library(base64enc)

#트위터의 키번호와 토큰번호를 넣어주세요
consumerKey <- "    트위터 가입후 받아서 넣어야함   "
consumerSecret <- "    트위터 가입후 받아서 넣어야함   "
accessToken <- "    트위터 가입후 받아서 넣어야함   "
accessTokenSecret <- "    트위터 가입후 받아서 넣어야함   "

setup_twitter_oauth(consumerKey, consumerSecret, accessToken, accessTokenSecret)

#키워드 지정
keyword <- enc2utf8("헌혈")

#크롤링할 트위터 수와 언어 설정
blood <- searchTwitter(keyword, n=500, lang="ko")
length(blood)
head(blood)
#기간 설정
blood2 <- searchTwitter(keyword, since='2016-01-01', until='2016-11-02', lang="ko")
length(blood2)
head(blood2)

blood3 <- searchTwitter(keyword, since='2016-01-01', until='2016-11-02', lang="ko", n=500)
length(blood3)
head(blood3)