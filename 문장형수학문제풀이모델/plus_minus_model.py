# %%

import pandas as pd

df = pd.read_csv("../data/plus_minus1.csv")
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

#% matplotlib
#inline

# %%

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

import re

df["model"] = ''
df["model_answer"] = ''

for i in range(0, len(df)):
    if re.compile(
            "보다 [\w]{1,9} ['더 가지고 있습니다, 더 가지고 있습니까, 더 많이 가지고 있는지, 더 팔았습니까, 더 많았다고 합니다, 더 많습니까, 더 많은지, 더 많을까요, 더 많이 먹었습니까, 더 적게']").findall(
            df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("[\w]{1,9} ['더 많이 가지고 있는지,더 붙일 수 있습니까']").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("몇  [\w]{1,4}를 ['주었습니다. , 주었더니 ,줬습니다']").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("몇  [\w]{1,4}를 ['주었습니다. , 주었더니 ,줬습니다']").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("나누어").findall(df["질문"][i]) != []:
        if re.compile("['를 가졌다면, 를 주었다면, 먼저,  를 쥐었다면']").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("['주었더니, 하였더니']").findall(df["질문"][i]) != []:
        if re.compile("남았습니다.").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("에게  [\w]{1,10}['을,를'] 한 [\w]{1,4}씩").findall(df["질문"][i]) != []:
        if re.compile("몇  [\w]{1,4} 더 필요합니까").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("와 똑같은  [\w]{1,10} 가지려면").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("와 같아질까요").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("같은 수의  [\w]{1,10} 갖기 위하여").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("만큼  [\w]{1,10}을 가지려면").findall(df["질문"][i]) != []:
        if re.compile("만큼  [\w]{1,10}을 가지려면  [\w]{1,10} 몇 [\w]{1,4}가 더 있어야").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("['중 , 그중 , 그 중에서, 이 중, 이 중에서, 중에서']").findall(df["질문"][i]) != []:
        if re.compile("['남았습니다, 주었습니다, 남습니까, 잃었습니다, 남은,  나가서, 부러졌습니다, 몇 [\w]{1,4}입니까']").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("['잠시 후, 얼마 후, 잠시후, 며칠 후에, 며칠 후']").findall(df["질문"][i]) != []:
        if re.compile("['남아있는,  남았습니까, 날아갔습니다., 졌습니다, 돌아가서']").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

            # 더하기
p = ['줬습니다', '합', '더했더니']
xx = ['어떤', '얼마', '몇']

for i in range(0, len(df)):
    li = []
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "NR" and (
                (df["kkma"][i][j][0] != "이") and (df["kkma"][i][j][0] != "몇") and (df["kkma"][i][j][0] != "하나")):
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








    # 상자문제
    # for i in range(0,len(df)):
    elif re.compile("[\d]{1,4}['을,를'] 넣었더니 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0]), '+', int(a[2])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]) + int(a[2]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[2]), '-(', int(a[0]), '-', int(a[1]), ')']
            df["model_answer"][i] = (int(a[2]) - int(a[0]) + int(a[1]))
    elif re.compile("[\d]{1,4}['을,를'] 넣으면 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0]), '+', int(a[2])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]) + int(a[2]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[2]), '-(', int(a[0]), '-', int(a[1]), ')']
            df["model_answer"][i] = (int(a[2]) - int(a[0]) + int(a[1]))

# %%

# df.to_excel("a12.xlsx",index=False)
df.head()

# %%

# 덧셈부분이 변한다

'''
for i in range(0,len(df)):
    if re.compile('["합해, 합해서"] [\d]{1,4}').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))
    elif re.compile('["합해, 합해서"] 몇').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))
    elif re.compile('[\d]{1,4}와 어떤 수의 합은 [\d]{1,4}').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))
    elif re.compile('[\d]{1,4}[\w]{1,4}를 합하면 [\d]{1,4}').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))

    elif re.compile('보다 몇[\w]{1,4}  더 ["많을까요, 많습니까"]').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))
    elif re.compile('보다 [\d]{1,4}[\w]{1,5} 더 ').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))
    elif re.compile('똑같은 [\w]{1,10} 가지려면').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))
    elif re.compile('몇 [\w]{1,10} 더 [\w]{1,10}면 [\w]{1,10}와 같아질까요').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))
    elif re.compile('보다 [\w]{1,10} 몇 [\w]{1,5} 더 많이').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))

    elif re.compile('[\d]{1,4}[\w]{1,4}에게 [\w]{1,10}을 한 [\w]{1,5}씩 [\w]{0,10} ["주려고, 나누어"] [\w]{1,30} 몇 [\w]{1,5} 더 필요').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=['abs(',int(a[1]),'-',int(a[0]),')']
        df["model_answer"][i]=abs(int(a[1])-int(a[0]))

    elif re.compile('[\d]{1,4}[\w]{1,4}의 가족이 두 대의 차를 나누어 타고 놀이 공원에 가려고 합니다.  먼저 [\d]{1,4}[\w]{1,4}이 차에 타고 출발했습니다.  다른 차에 타고 출발해야 할 사람은 몇 [\w]{1,4}입니까?').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=[int(a[0]),'-',int(a[1])]
        df["model_answer"][i]=abs(int(a[0])-int(a[1]))

    elif re.compile('잠시 후 [\w]{1,10} [\d]{1,4}[\w]{1,4}가   ["떠났습니다., 날아갔습니다."]  남아 있는').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=[int(a[0]),'-',int(a[1])]
        df["model_answer"][i]=abs(int(a[0])-int(a[1]))
    elif re.compile('잠시 후  [\w]{1,10} [\d]{1,4}[\w]{1,4}가 ["떠났습니다., 날아갔습니다."]  [\w]{1,20}  몇 [\w]{1,5}  남았습니까').findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=[int(a[0]),'-',int(a[1])]
        df["model_answer"][i]=abs(int(a[0])-int(a[1]))
    elif re.compile("잠시 후 몇  [\w]{1,30}  [\d]{1,4}[\w]{1,20}  남았습니다").findall(df["질문"][i])!=[]:
        a=re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i]=[int(a[0]),'-',int(a[1])]
        df["model_answer"][i]=abs(int(a[0])-int(a[1]))
'''

# %%


# %% md

## Kmeans

# %%

for i in range(0, len(df)):
    df["키워드1"][i] = df["키워드1"][i].strip()
    df["키워드1"][i] = list(df["키워드1"][i].split(", "))
    print(df["키워드1"][i])

# %%

df2 = df.copy()
df2.head()

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
print("sequences2\t", sequences2)

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

elbow(data_points2)  # 더하기 빼기

# %%

kmeans = KMeans(n_clusters=6).fit(data_points2)
df2['kmeans'] = kmeans.labels_
df2.to_excel('k2.xlsx', index=False)

# %%


