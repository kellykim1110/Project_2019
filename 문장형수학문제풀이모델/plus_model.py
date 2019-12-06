# %%

import pandas as pd

df = pd.read_csv("../data/math_func_type.csv")
df.head()

# %%

import platform

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()

from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    print("It's unknown system. Hangul fonts are not supported!")

# plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["figure.figsize"] = [12, 6]

# % matplotlib
# inline

# %%

df = df.iloc[:120, :]
df.tail()

# %%

from konlpy.tag import Kkma

kkma = Kkma()

from konlpy.tag import Okt

okt = Okt()

df["kkma"] = ''
df["okt"] = ''

for i in range(0, len(df)):
    # df['kkma'][i] = kkma.morphs(df["질문"][i])
    # df['okt'][i] = okt.morphs(df["질문"][i])
    df['kkma'][i] = kkma.pos(df["질문"][i])
    df['okt'][i] = okt.pos(df["질문"][i])

df.head()

# %%

nnm = []

for i in range(0, len(df)):
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "NNM":
            nnm.append(df["kkma"][i][j][0])
nnm  # 단위

# %%

mag = []

for i in range(0, len(df)):
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "MAG":
            mag.append(df["kkma"][i][j][0])
mag  # 모두 더 이런 +로 나타낼 것들

# %%

ma = []  # mag의 인덱스 번호

for i in range(0, len(df)):
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "MAG":
            ma.append(i)

ma  # 14, 55, 65, 67, 68, 75, 76, 77, 78, 90, 93, 96, 97, 98, 99, 100, 101, 102, 107, 108, 109, 110, 111, 112, 113

# %%

li = [14, 55, 65, 67, 68, 75, 76, 77, 78, 90, 93, 96, 97, 98, 99, 100, 101, 102, 107, 108, 109, 110, 111, 112, 113]

for i in li:
    print(df["질문"][i])
    # 줬습니다, 합해, 합하면, 합, 더했더니, 합해서
##67은 빼기 문제  #철수와 영수는 28개의 사탕을 갖고 있습니다. 철수가 13개의 사탕을 갖고 있다면 영수가 갖고 있는 사탕은 몇 개인가요?
### ["NR"]['를,을'] ['넣으면, 넣었더니'] ["NR"]["가, 이"] 나오는 상자

# %%

df["okt"][78]  # '줬습니다','합','더했더니'

# %%

df["질문"][99]

# %%

# 연산자 +
### 줬습니다, 합해, 합하면, 합, 더했더니, 합해서
###if df["kkma"][i][j][1]=="MAG" for j in range(0,len(df["kkma"][i])) for i in range(0, len(df))  #list.remove("같이")

# %%

### ["NR"]['를,을'] ['넣으면, 넣었더니'] ["NR"]["가, 이"] 나오는 상자

# %%


# %%

mdt = []

for i in range(0, len(df)):
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "MDT":
            mdt.append(df["kkma"][i][j][0])
mdt  # 연산자 =

# %%

df["kkma"][27][3]

# %%

md = []

for i in range(0, len(df)):
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "MDT":
            md.append(i)
md[29]  #

# %%

md[-25]

# %%

df["질문"][27]  # 새

# %%

df["질문"][34]  # 온

# %%

df["질문"][39]  # 이 #이

# %%

df["kkma"][39]  # 이 #이 ##내비게이션

# %%

df["질문"][66]  # 그

# %%

md  # 76,78, 90~

# %%

df["질문"][76]  # 어떤 수

# %%

df["okt"][76]  # 어떤

# %%

df["질문"][78]  # 어떤 수

# %%

df["질문"][90]  # 얼마

# %%

df["okt"][90]  # 얼마

# %%

df["질문"][107]  # 몇

# %%

df['okt'][107]  # 몇

# %%

# 미지수 x
###어떤 수, 얼마, 몇
###if df["kkma"][i][j][1]=="MDT" for j in range(0,len(df["kkma"][i])) for i in range(0, len(df))

# %%


# %%

# 연산자 +
### '줬습니다','합','더했더니'
###if df["kkma"][i][j][1]=="MAG" for j in range(0,len(df["kkma"][i])) for i in range(0, len(df))  #list.remove("같이")

# 미지수 x
###어떤 수, 얼마, 몇
###if df["kkma"][i][j][1]=="MDT" for j in range(0,len(df["kkma"][i])) for i in range(0, len(df))

# %%

p = ['줬습니다', '합', '더했더니']
xx = ['어떤', '얼마', '몇']
import re

df["model"] = ''
for i in range(0, len(df)):
    li = []
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "NR" and ((df["kkma"][i][j][0] != "이") and (df["kkma"][i][j][0] != "몇")):
            li.append(int(df["kkma"][i][j][0]))
        elif (df["kkma"][i][j][1] == "MAG") and (df["okt"][i][j][0] == h for h in p):
            li.append('+')

        elif (df["kkma"][i][j][1] == "MDT") and (df["okt"][i][k][0] == x for x in xx):
            li.append('x')
    df["model"][i] = li

# %%

df.head()

# %%

### ["NR"]['를,을'] ['넣으면, 넣었더니'] ["NR"]["가, 이"] 나오는 상자
##그림과 같이 상자에 ["NR"]['를,을'] 넣었더니 ["NR"]

# %%

df["질문"].tail(20)

# %%

df["질문"][105]

# %%

pattern = re.compile("[\d]{1,4}['을,를'] 넣었더니 [\d]{1,4}")
pattern.findall(df["질문"][105])

# %%

pattern = re.compile("[\d]{1,4}['을,를'] 넣으면 [\d]{1,4}")
pattern.findall(df["질문"][110])

# %%

a = re.compile("[\d]{1,4}").findall(df["질문"][105])
if int(a[0]) < int(a[1]):
    print(int(a[1]) - int(a[0]) + int(a[2]))

# %%

df["model_answer"] = ''

for i in range(0, len(df)):
    if re.compile("[\d]{1,4}['을,를'] 넣었더니 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0]), '+', int(a[2])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]) + int(a[2]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[2]), '-(', int(a[0]), '-', int(a[1]), ')']
            df["model_answer"][i] = (int(a[2]) - (int(a[0]) - int(a[1])))
    elif re.compile("[\d]{1,4}['을,를'] 넣으면 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0]), '+', int(a[2])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]) + int(a[2]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[2]), '-(', int(a[0]), '-', int(a[1]), ')']
            df["model_answer"][i] = (int(a[2]) - (int(a[0]) - int(a[1])))

# %%

df.tail(31)

# %%

p = ['줬습니다', '합', '더했더니']
xx = ['어떤', '얼마', '몇']
import re

df["model"] = ''
df["model_answer"] = ''

for i in range(0, len(df)):
    li = []
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "NR" and ((df["kkma"][i][j][0] != "이") and (df["kkma"][i][j][0] != "몇")):
            li.append(int(df["kkma"][i][j][0]))
        elif (df["kkma"][i][j][1] == "MAG") and (df["okt"][i][j][0] == h for h in p):
            li.append('+')
        elif (df["kkma"][i][j][1] == "MDT") and (df["okt"][i][k][0] == x for x in xx):
            li.append('x')
    df["model"][i] = li
    a1 = []
    for k in df["model"][i]:
        if type(k) == int:
            a1.append(k)
    if "+" in df["model"][i]:
        res = 0
        for g in a1:
            res += g
        df["model_answer"][i] = res

    # 예외처리
    if type(df["model"][i][-1]) == int:
        a = []
        for k in df["model"][i]:
            if type(k) == int:
                a.append(k)
        df["model"][i] = [a[1], '-', a[0]]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))

    # 상자문제
# 더하기 빼기 모두 포함
for i in range(0, len(df)):
    if re.compile("[\d]{1,4}['을,를'] 넣었더니 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0]), '+', int(a[2])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]) + int(a[2]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[2]), '-(', int(a[0]), '-', int(a[1]), ')']
            df["model_answer"][i] = (int(a[2]) - (int(a[0]) - int(a[1])))
    elif re.compile("[\d]{1,4}['을,를'] 넣으면 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0]), '+', int(a[2])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]) + int(a[2]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[2]), '-(', int(a[0]), '-', int(a[1]), ')']
            df["model_answer"][i] = (int(a[2]) - (int(a[0]) - int(a[1])))


    # 예외처리
    ##어떤 수와 15의 합은 51
    ##어떤 수에 1을 더했더니 10
    elif re.compile("어떤 수와 [\d]{1,4}의 합은 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i] = [int(a[1]), '-', int(a[0])]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))
    elif re.compile("[\d]{1,4}와 어떤 수의 합은 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i] = [int(a[1]), '-', int(a[0])]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))
    elif re.compile("어떤 수에 [\d]{1,4}을 더했더니 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i] = [int(a[1]), '-', int(a[0])]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))

    elif re.compile("몇 [\w]{1,2} 더").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i] = [int(a[1]), '-', int(a[0])]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))

    # %%

# %% md

### Kmeans()

# %%

for i in range(0, len(df)):
    df["키워드1"][i] = df["키워드1"][i].strip()
    df["키워드1"][i] = list(df["키워드1"][i].split(", "))
    print(df["키워드1"][i])

# %%

df2 = df.copy()
df2.head()

# %%

# !pip
# install
# tensorflow

# %%

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from tensorflow.keras.utils import to_categorical

# %%

len_df = len(df2)

plus2 = df2['키워드1'].values
# 정제와 단어 토큰화
vocab2 = {}  # 파이썬의 dictionary 자료형
sentences2 = []

for i in range(len(plus2)):
    result2 = df2['키워드1'][i]
    for word in result2:
        if word not in vocab2:
            vocab2[word] = 0
        vocab2[word] += 1
    sentences2.append(result2)
print("vocab2\n", vocab2)

vocab_sorted2 = sorted(vocab2.items(), key=lambda x: x[1], reverse=True)
print("\n\nvocab_sorted2\n", vocab_sorted2)

word_to_index2 = {}
i = 0
for (word, frequency) in vocab_sorted2:
    if frequency > 0:  # 정제(Cleaning) 챕터에서 언급했듯이 빈도수가 적은 단어는 제외한다.
        i = i + 1
        word_to_index2[word] = i
print("\n\n word_to_index2\n", word_to_index2)

word_to_index2['OOV'] = len(word_to_index2) + 1

encoded2 = []
for s in sentences2:
    temp2 = []
    for w in s:
        try:
            temp2.append(word_to_index2[w])
        except KeyError:
            temp2.append(word_to_index2['OOV'])
    encoded2.append(temp2)
print("\n\nencoded2\n", encoded2)

max_len2 = max(len(l) for l in encoded2)  # 모든 샘플에서 길이가 가장 긴 샘플의 길이 출력
print('df2의 샘플의 최대 길이 : {}'.format(max_len2))

min_len2 = min(len(l) for l in encoded2)  # 모든 샘플에서 길이가 가장 긴 샘플의 길이 출력
print('df2_샘플의 최소 길이 : {}'.format(min_len2))

sequences2 = pad_sequences(encoded2, maxlen=max_len2, padding='pre')
print("sentence2\t", sentence2)

col_ = []
for i in range(1, 1 + int(max_len2)):
    col_.append(str(i))
col_ = set(col_)

df2 = pd.DataFrame(columns=col_)

for i in range(len_df):
    df2.loc[i] = sequences2[i]

data_points2 = df2.values

print("df")
df2.head()

# %%

# kmeans클러스터링은 클러스터 내 오차제곱합(SSE)의 값이 최소가 되도록 클러스터의 중심으로 결정해 나가는 방법

# SSE가 급격히 작아지는 부분이 최적의 클러스터 개수

# %%

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


# %%

def elbow(X):
    sse = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i, init="k-means++", random_state=0)
        km.fit(X)
        sse.append(km.inertia_)
    plt.plot(range(1, 11), sse, marker="o")
    plt.show()


# %%

elbow(data_points2)  # 더하기

# %%

kmeans = KMeans(n_clusters=5).fit(data_points2)
df2['kmeans'] = kmeans.labels_
# df2.to_excel('k.xlsx',index=False)

# %%
