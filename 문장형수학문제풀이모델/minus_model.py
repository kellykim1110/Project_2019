# %%

import pandas as pd

df = pd.read_excel("../data/math_func_type.xlsx", sheet_name=1)
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

mdt = []

for i in range(0, len(df)):
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "MDT":
            mdt.append(df["kkma"][i][j][0])
            print(i, df["kkma"][i][j][0])
# 미지수 x

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

            # 상자문제
for i in range(0, len(df)):
    if re.compile("[\d]{1,4}['을,를'] 넣었더니 [\d]{1,4}").findall(df["질문"][i]) != []:
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

df.head()
df.to_excel("a2.xlsx", index=False)

# %%


