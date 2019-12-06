# %%

import pandas as pd

df = pd.read_excel("./data/math_func_type.xlsx", sheet_name=2)
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

df.to_excel("a3.xlsx", index=False)

# %%

import re

df["model"] = ''
df["model_answer"] = ''

for i in range(0, len(df)):
    if re.compile("[\d]{1,2}월 [\d]{1,2}일입니다. [\d]{1}주일 후는 몇 월 ['몇 일, 며칠']").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        k = int(a[2]) * 7 + int(a[1])
        if a[0] in [1, 3, 5, 7, 8, 10]:
            if int(k) > 31:
                df['model_answer'][i] = str(int(a[0]) + 1) + "월" + str(int(k) - 31) + "일"
            else:
                df['model_answer'][i] = str(a[0]) + "월" + str(k) + "일"
        elif a[0] == 2:
            if int(k) > 28:
                df['model_answer'][i] = str(int(a[0]) + 1) + "월" + str(int(k) - 28) + "일"
            else:
                df['model_answer'][i] = str(a[0]) + "월" + str(k) + "일"
        elif a[0] == 12:
            if int(k) > 31:
                df['model_answer'][i] = "1월" + str(int(k) - 31) + "일"
            else:
                df['model_answer'][i] = str(a[0]) + "월" + str(k) + "일"
        else:
            if int(k) > 30:
                df['model_answer'][i] = str(int(a[0]) + 1) + "월" + str(int(k) - 30) + "일"
            else:
                df['model_answer'][i] = str(a[0]) + "월" + str(k) + "일"

df['model_answer'][31]

# %%

for i in range(0, len(df)):
    if re.compile("[\d]{1,2}주일입니다.").findall(df["질문"][i]) and re.compile("모두 며칠").findall(df["질문"][i]):
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        df['model'][i] = a
        df['model_answer'][i] = str(int(a[0]) * 7) + "일"

df['model_answer'][21]

# %%

for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile("씩").findall(df["질문"][i]) != []) and (re.compile("모두").findall(df["질문"][i]) != []) and (len(a) == 2):
        df['model_answer'][i] = int(a[0]) * int(a[1])
    elif (re.compile("[\d]{1,2}[\w]{1,3}에 [\d]{1,2}[\w]{1,3}씩").findall(df["질문"][i]) != []) and (
            re.compile("모두").findall(df["질문"][i]) != []) and (len(a) == 2):
        df['model_answer'][i] = int(a[0]) * int(a[1])

    elif (re.compile("씩").findall(df["질문"][i]) != []) and (re.compile("모두").findall(df["질문"][i]) != []) and (
            len(a) == 4):
        df['model_answer'][i] = int(a[0]) * int(a[1]) + int(a[2]) * int(a[3])
    elif (re.compile("[\d]{1,2}[\w]{1,3}에 [\d]{1,2}[\w]{1,3}씩").findall(df["질문"][i]) != []) and (
            re.compile("모두").findall(df["질문"][i]) != []) and (len(a) == 4):
        df['model_answer'][i] = int(a[0]) * int(a[1]) + int(a[2]) * int(a[3])

    elif (re.compile("씩").findall(df["질문"][i]) != []) and (
            re.compile("[\d]{1,4}[\w]{1,4}씩 몇").findall(df["질문"][i]) != []) and (
            re.compile("['모두,묶으면, 묶는다면, 포장한다면, 포장하면']").findall(df["질문"][i]) != []) and (len(a) == 3):
        df['model_answer'][i] = (int(a[0]) * int(a[1])) / int(a[2])
    elif (re.compile("씩").findall(df["질문"][i]) != []) and (
            re.compile("몇[\w]{1,4}씩 [\d]{1,4}").findall(df["질문"][i]) != []) and (
            re.compile("['모두,묶으면, 묶는다면, 포장한다면, 포장하면']").findall(df["질문"][i]) != []) and (len(a) == 3):
        df['model_answer'][i] = (int(a[0]) * int(a[1])) / int(a[2])


    elif (re.compile("['중 , 그중 , 그 중에서, 이 중, 이 중에서, 중에서']").findall(df["질문"][i]) != []) and (
            re.compile("[\d]{1,2}[\w]{1,3}씩 [\d]{1,2}[\w]{1,15} 나누어").findall(df["질문"][i]) != []) and (
            re.compile("남은").findall(df["질문"][i]) != []) and (len(a) == 3):
        k = max(a)
        del a[a.index(max(a))]
        if int(k) > (int(a[0]) * int(a[1])):
            df['model_answer'][i] = int(k) - int(a[0]) * int(a[1])


    elif (re.compile("[\d]{1,2}[\w]{1,3}씩[\w]{0,20} [\d]{1,2}").findall(df["질문"][i]) != []) and (
            re.compile("모두 몇").findall(df["질문"][i]) != []) and (
            re.compile("의 [\d]{1,2}배만큼").findall(df["질문"][i]) != []) and (len(a) == 3):
        df['model_answer'][i] = int(a[0]) * int(a[1]) * int(a[2])

df['model_answer'][0]

# %%

for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile("['중 , 그중 , 그 중에서, 이 중, 이 중에서, 중에서']").findall(df["질문"][i]) != []) and (
            re.compile("[\d]{1,2}[\w]{1,3}씩 [\d]{1,2}[\w]{1,15} 나누어").findall(df["질문"][i]) != []) and (
            re.compile("남은").findall(df["질문"][i]) != []) and (len(a) == 3):
        k = max(a)
        del a[a.index(max(a))]
        if int(k) > (int(a[0]) * int(a[1])):
            df['model_answer'][i] = int(k) - int(a[0]) * int(a[1])


    elif (re.compile("[\d]{1,2}[\w]{1,3}씩[\w]{0,20} [\d]{1,2}").findall(df["질문"][i]) != []) and (
            re.compile("모두 몇").findall(df["질문"][i]) != []) and (
            re.compile("의 [\d]{1,2}배만큼").findall(df["질문"][i]) != []) and (len(a) == 3):
        df['model_answer'][i] = int(a[0]) * int(a[1]) * int(a[2])

# %%

for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile("[\d]{1,2}[\w]{1,4}씩[\w]{0,20} [\d]{1,2}[\w]{1,4}").findall(df["질문"][i]) != []) and (
            re.compile("[나머지, 남은]").findall(df["질문"][i]) != []) and (
            re.compile("모두 몇").findall(df["질문"][i]) != []) and (
            re.compile("1[\w]{1,4}씩").findall(df["질문"][i]) != []) and (len(a) == 4):
        del a[a.index("1")]
        for d in range(0, len(a)):
            a[d] = int(a[d])
        k = max(a)
        del a[a.index(max(a))]
        if int(k) > (int(a[0]) * int(a[1])):
            df['model_answer'][i] = int(k) - (int(a[0]) * int(a[1]))
        else:
            df['model_answer'][i] = (int(a[0]) * int(a[1])) - int(k)

df['model_answer'][33]
# df['질문'][33]

# %%

for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile("씩").findall(df["질문"][i]) != []) and (len(a) == 3) and (
            re.compile("[\d]{1,4}[\w]{1,4}씩 ['묶으면, 묶는다면, 포장한다면, 포장하면']몇").findall(df["질문"][i]) != []) and (
            re.compile("['모두, 묶으면, 묶는다면, 포장한다면, 포장하면']").findall(df["질문"][i]) != []):
        df['model_answer'][i] = (int(a[0]) * int(a[1])) / int(a[2])
    elif (re.compile("씩").findall(df["질문"][i]) != []) and (len(a) == 3) and (
            re.compile("[\d]{1,4}[\w]{1,4}씩 몇[\w]{1,4}").findall(df["질문"][i]) != []):
        df['model_answer'][i] = (int(a[0]) * int(a[1])) / int(a[2])
    elif (re.compile("씩").findall(df["질문"][i]) != []) and (len(a) == 3) and (
            re.compile("몇[\w]{1,4}씩").findall(df["질문"][i]) != []) and (
            re.compile("['라면, 모두, 묶으면, 묶는다면, 포장한다면, 포장하면']").findall(df["질문"][i]) != []):
        df['model_answer'][i] = (int(a[0]) * int(a[1])) / int(a[2])
df['model_answer'][27]
# df['질문'][20]

# %%

for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile(" [\d]{1,2}[\w]{1,3}씩 [\d]{1,2}[\w]{1,3}").findall(df["질문"][i]) != []) and (len(a) == 4) and (
            re.compile("[\d]{1,4}[\w]{1,4}씩 한 [\w]{1,4}").findall(df["질문"][i]) != []):
        df['model_answer'][i] = (int(a[0]) * int(a[1])) / int(a[2])

df['model_answer'][19]

# %%

for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile("[\d]{1,2}명씩 앉을 수 있는 의자가 [\d]{1,2}개, [\d]{1,2}명씩 앉을 수 있는 의자가 [\d]{1,2}개").findall(
            df["질문"][i]) != []) and (re.compile("1명씩 앉을 수 있는 의자는 몇 개").findall(df["질문"][i]) != []):
        del a[a.index("1")]
        for d in range(0, len(a)):
            a[d] = int(a[d])
        k = max(a)
        del a[a.index(max(a))]
        if int(k) > (int(a[0]) * int(a[1]) + int(a[2]) * int(a[3])):
            df['model_answer'][i] = int(k) - (int(a[0]) * int(a[1]) + int(a[2]) * int(a[3]))

    elif (re.compile("[\d]{1,2}명씩 앉을 수 있는 의자가 [\d]{1,2}개, [\d]{1,2}명씩 앉을 수 있는 의자가 [\d]{1,2}개").findall(
            df["질문"][i]) != []) and (re.compile("한명씩 앉을 수 있는 의자는 몇 개").findall(df["질문"][i]) != []):
        for d in range(0, len(a)):
            a[d] = int(a[d])
        k = max(a)
        del a[a.index(max(a))]
        if int(k) > (int(a[0]) * int(a[1]) + int(a[2]) * int(a[3])):
            df['model_answer'][i] = int(k) - (int(a[0]) * int(a[1]) + int(a[2]) * int(a[3]))

df['model_answer'][34]
# df['질문'][34]

# %%

for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile("1등은 [\d]{1}점, 2등은 [\d]{1}점, 3등은 [\d]{1}점").findall(df["질문"][i]) != []) and (
            re.compile('1등이 [\d]{1,2}명, 2등이 [\d]{1,2}명, 3등이 [\d]{1,2}명').findall(df["질문"][i]) != []) and (
            re.compile("모두 몇").findall(df["질문"][i]) != []):
        df['model_answer'][i] = int(a[1]) * int(a[-5]) + int(a[2]) * int(a[-3]) + int(a[3]) * int(a[-1])
    elif (re.compile("[\d]{1}점짜리 공 [\d]{1}개").findall(df["질문"][i]) != []):
        b = re.compile("[\d]{1}점짜리 공 [\d]{1}개").findall(df["질문"][i])
        for j in range(0, len(b)):
            c1 = []
            c2 = []
            d1 = re.compile("[\d]{1}점짜리").findall(b[j])
            d2 = re.compile("공 [\d]{1}개").findall(b[j])
            c1.append(int(d1[0][0]))
            c2.append(int(d2[0][-2]))
        df['model_answer'][i] = 0
        if len(c1) == len(c2):
            for q in range(0, len(c1)):
                df['model_answer'][i] = df['model_answer'][i] + (c1[q] * c2[q])
    elif (re.compile("[\d]{1}점을 [\d]{1}번").findall(df["질문"][i]) != []):
        b = re.compile("[\d]{1}점을 [\d]{1}번").findall(df["질문"][i])
        for j in range(0, len(b)):
            c1 = []
            c2 = []
            d1 = re.compile("[\d]{1}점을").findall(b[j])
            d2 = re.compile("[\d]{1}번").findall(b[j])
            c1.append(int(d1[0][0]))
            c2.append(int(d2[0][0]))
        df['model_answer'][i] = 0
        if len(c1) == len(c2):
            for q in range(0, len(c1)):
                df['model_answer'][i] = df['model_answer'][i] + (c1[q] * c2[q])

df['model_answer'][42]
# df['질문'][42]

# %%

re.compile("[\d]{1}점짜리 공 [\d]{1}개").findall(df["질문"][47])

# %%

for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile("[\w]{1,2}각형[\w]{0,3} [\d]{1,2}개").findall(df["질문"][i])) and (
    re.compile("['변, 꼭지점, 각']의 수").findall(df["질문"][i])) and (re.compile("어느 도형이 몇 개").findall(df["질문"][i])):
        r1 = ["삼각형", "사각형", "오각형", "육각형", "칠각형", "팔각형", "구각형", "십각형", "십이각형", "십오각형", "십육각형", "십팔각형", "이십각형"]
        r2 = [3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 18, 20]
        b = re.compile("[\w]{1,2}각형[\w]{0,3} [\d]{1,2}개").findall(df["질문"][i])
        c1 = []
        c2 = []
        for j in range(0, len(b)):
            d1 = re.compile("[\d]{1,2}개").findall(b[j])
            c1.append(int(d1[0][0]))
            d2 = re.compile("[\w]{1,2}각형").findall(b[j])
            c2.append(r2[r1.index(d2[0])])
        df['model_answer'][i] = c1[0] * c2[0]
        for q in range(1, len(c1)):
            if df['model_answer'][i] < c1[q] * c2[q]:
                df['model_answer'][i] = c1[q] * c2[q]

    elif (re.compile("[\w]{1,2}각형[\w]{0,3} [\d]{1,2}개").findall(df["질문"][i])) and (
    re.compile("['변, 꼭지점, 각']의 수의 합은").findall(df["질문"][i])) and (re.compile("모두 몇 개").findall(df["질문"][i])):
        r1 = ["삼각형", "사각형", "오각형", "육각형", "칠각형", "팔각형", "구각형", "십각형", "십이각형", "십오각형", "십육각형", "십팔각형", "이십각형"]
        r2 = [3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 18, 20]
        b = re.compile("[\w]{1,2}각형[\w]{0,3} [\d]{1,2}개").findall(df["질문"][i])
        c1 = []
        c2 = []
        for j in range(0, len(b)):
            d1 = re.compile("[\d]{1,2}개").findall(b[j])
            c1.append(int(d1[0][0]))
            d2 = re.compile("[\w]{1,2}각형").findall(b[j])
            c2.append(r2[r1.index(d2[0])])
        df['model_answer'][i] = 0
        for q in range(0, len(c1)):
            df['model_answer'][i] = df['model_answer'][i] + (c1[q] * c2[q])

    elif (re.compile("[\w]{1,10} [\d]{1,2}대").findall(df["질문"][i])) and (re.compile("바퀴").findall(df["질문"][i])):
        r1 = ["오토바이", "오토바이가", "승용차", '자동차', '승용차가', '자동차가', '세발자전거', '두발자전거']
        r2 = [2, 2, 4, 4, 4, 4, 3, 2]
        b = re.compile("[\w]{1,10} [\d]{1,2}대").findall(df["질문"][i])
        c1 = []
        c2 = []
        for j in range(0, len(b)):
            d1 = re.compile("[\d]{1,2}대").findall(b[j])
            c1.append(int(d1[0][0]))
            d2 = re.compile("[\w]{1,10}").findall(b[j])
            c2.append(r2[r1.index(d2[0])])
        df['model_answer'][i] = 0
        for q in range(0, len(c1)):
            df['model_answer'][i] = df['model_answer'][i] + (c1[q] * c2[q])



    elif (re.compile("[\w]{1,4} [\d]{1,2}마리의 다리는 모두 몇 개").findall(df["질문"][i])):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b = re.compile("[\w]{1,4} [\d]{1,2}마리의 다리는 모두 몇 개").findall(df["질문"][i])
        c1 = []
        c2 = []
        for j in range(0, len(b)):
            d1 = re.compile("[\d]{1,2}마리의 다리").findall(b[j])
            d11 = re.compile("[\d]{1,2}").findall(d1[0])
            c1.append(int(d11[0]))
            d2 = re.compile("[\w]{1,4}").findall(b[j])
            c2.append(r2[r1.index(d2[0])])
        print(i, c1, c2)
        for q in range(0, len(c1)):
            df['model_answer'][i] = (c1[q] * c2[q])

    elif (re.compile("[\w]{1,4}의 다리를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])) and (
    (re.compile(" [\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i]))):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b = re.compile("[\w]{1,4}의 다리를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])
        c1 = []
        c2 = []
        for j in range(0, len(b)):
            d1 = re.compile("[\d]{1,3}개").findall(b[j])
            d11 = re.compile("[\d]{1,3}").findall(d1[0])
            c1.append(int(d11[0]))
            d2 = re.compile("[\w]{1,4}").findall(b[j])
            c2.append(r2[r1.index(d2[0])])
        print(i, c1, c2)

        for q in range(0, len(c1)):
            df['model_answer'][i] = (c1[q] // c2[q])

    elif (re.compile("[\w]{1,4} [\d]{1,2}마리").findall(df["질문"][i])) and (
    (re.compile("[\w]{1,3}와 [\w]{1,3}의 다리 [\w]{0,2}를 ['세어 보니, 세었더니'] 모두 [\d]{1,3}개").findall(df["질문"][i]))) and (
    re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b1 = re.compile("[\w]{1,4} [\d]{1,2}마리").findall(df["질문"][i])
        b2 = re.compile("[\w]{1,4}와 [\w]{1,3}의 다리 [\w]{0,2}를 ['세어 보니, 세었더니'] 모두 [\d]{1,3}개").findall(df["질문"][i])
        b3 = re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])
        c1 = []  # 각 동물의 마리수
        c11 = []  # 모든 다리수
        c2 = []  # 동물의 다리수
        c22 = []  # 구하려는 동물의 다리수
        for j in range(0, len(b1)):
            d1 = re.compile("[\d]{1,2}마리").findall(b1[j])
            d11 = re.compile("[\d]{1,2}").findall(d1[0])
            c1.append(int(d11[0]))
            d2 = re.compile("[\w]{1,4}").findall(b1[j])
            c2.append(r2[r1.index(d2[0])])
        d111 = re.compile("[\d]{1,3}개").findall(b2)
        d1111 = re.compile("[\d]{1,3}").findall(d111[0])
        c11.append(int(d1111[0]))
        d22 = re.compile("[\w]{1,4}").findall(b3)
        c22.append(r2[r1.index(d22[0])])
        print(i, c1, c2, c11, c22)
        qq = 0
        for q in range(0, len(c1)):
            qq = qq + (c1[q] * c2[q])
        df['model_answer'][i] = ((c11[0] - qq) // c22[0])


    elif (re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])) and (
    (re.compile("[\w]{1,3}가 모두 [\d]{1,3}마리라면").findall(df["질문"][i]))) and (
    re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b1 = re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])
        b2 = re.compile("[\w]{1,3}가 모두 [\d]{1,3}마리라면").findall(df["질문"][i])
        b3 = re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])
        c1 = []  # 각 동물의 마리수
        c11 = []  # 모든 다리수
        c2 = []  # 동물의 다리수
        c22 = []  # 구하려는 동물의 다리수
        for j in range(0, len(b2)):
            d1 = re.compile("[\d]{1,2}마리").findall(b2[j])
            d11 = re.compile("[\d]{1,2}").findall(d1[0])
            c1.append(int(d11[0]))
            d2 = re.compile("[\w]{1,3}").findall(b2[j])
            c2.append(r2[r1.index(d2[0])])
        d111 = re.compile("[\d]{1,3}개").findall(b1)
        d1111 = re.compile("[\d]{1,3}").findall(d111[0])
        c11.append(int(d1111[0]))
        d22 = re.compile("[\w]{1,4}").findall(b3)
        c22.append(r2[r1.index(d22[0])])
        print(i, c1, c2, c11, c22)
        qq = 0
        for q in range(0, len(c1)):
            qq = qq + (c1[q] * c2[q])
        df['model_answer'][i] = ((c11[0] - qq) // c22[0])

    elif (re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])) and (
    (re.compile("[\w]{1,3}['는,은'] [\d]{1,3}마리라면").findall(df["질문"][i]))) and (
    re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b1 = re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])
        b2 = re.compile("[\w]{1,3}['는, 은'] [\d]{1,3}마리").findall(df["질문"][i])
        b3 = re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])
        c1 = []  # 각 동물의 마리수
        c11 = []  # 모든 다리수
        c2 = []  # 동물의 다리수
        c22 = []  # 구하려는 동물의 다리수
        for j in range(0, len(b2)):
            d1 = re.compile("[\d]{1,2}마리").findall(b2[j])
            d11 = re.compile("[\d]{1,2}").findall(d1[0])
            c1.append(int(d11[0]))
            d2 = re.compile("[\w]{1,3}").findall(b2[j])
            c2.append(r2[r1.index(d2[0])])
        d111 = re.compile("[\d]{1,3}개").findall(b1)
        d1111 = re.compile("[\d]{1,3}").findall(d111[0])
        c11.append(int(d1111[0]))
        d22 = re.compile("[\w]{1,4}").findall(b3)
        c22.append(r2[r1.index(d22[0])])
        print(i, c1, c2, c11, c22)
        qq = 0
        for q in range(0, len(c1)):
            qq = qq + (c1[q] * c2[q])
        df['model_answer'][i] = ((c11[0] - qq) // c22[0])

    elif (re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])) and (
    (re.compile("[\w]{1,3}와 [\w]{1,3}가 [\d]{1,3}, [\d]{1,3}마리라면").findall(df["질문"][i]))) and (
    re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b1 = re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])
        b2 = re.compile("[\w]{1,3}와 [\w]{1,3}가 [\d]{1,3}, [\d]{1,3}마리라면").findall(df["질문"][i])
        b3 = re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])
        c1 = []  # 각 동물의 마리수
        c11 = []  # 모든 다리수
        c2 = []  # 동물의 다리수
        c22 = []  # 구하려는 동물의 다리수

        d1 = re.compile("[\d]{1,2}").findall(b2)
        for o in range(0, len(d1)):
            c1.append(int(d1[o]))
        d2 = re.compile("[\w]{1,3}").findall(b2)
        for o in range(0, len(d2)):
            c2.append(r2[r1.index(d2[o])])

        d111 = re.compile("[\d]{1,3}개").findall(b1)
        d1111 = re.compile("[\d]{1,3}").findall(d111[0])
        c11.append(int(d1111[0]))
        d22 = re.compile("[\w]{1,4}").findall(b3)
        c22.append(r2[r1.index(d22[0])])
        print(i, c1, c2, c11, c22)
        qq = 0
        for q in range(0, len(c1)):
            qq = qq + (c1[q] * c2[q])
        df['model_answer'][i] = ((c11[0] - qq) // c22[0])

print(df['질문'][40], df['model_answer'][40])
print(df['질문'][71], df['model_answer'][71])
print(df['질문'][74], df['model_answer'][74])
print(df['질문'][76], df['model_answer'][76])
print(df['질문'][85], df['model_answer'][85])

# %%

df22 = df.copy()
df22.head()

# %%

# 다리 개수

df = pd.read_excel("math_func_q_k_k1.xlsx")
df['model_answer'] = ''

for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile("[\w]{1,4} [\d]{1,2}마리의 다리는 모두 몇 개").findall(df["질문"][i])):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b = re.compile("[\w]{1,4} [\d]{1,2}마리의 다리는 모두 몇 개").findall(df["질문"][i])
        c1 = []
        c2 = []
        for j in range(0, len(b)):
            d1 = re.compile("[\d]{1,2}마리의 다리").findall(b[j])
            d11 = re.compile("[\d]{1,2}").findall(d1[0])
            c1.append(int(d11[0]))
            d2 = re.compile("[\w]{1,4}").findall(b[j])
            c2.append(r2[r1.index(d2[0])])
        print(i, c1, c2)
        for q in range(0, len(c1)):
            df['model_answer'][i] = (c1[q] * c2[q])

    elif (re.compile("[\w]{1,4}의 다리를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])) and (
    (re.compile(" [\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i]))):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b = re.compile("[\w]{1,4}의 다리를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])
        c1 = []
        c2 = []
        for j in range(0, len(b)):
            d1 = re.compile("[\d]{1,3}개").findall(b[j])
            d11 = re.compile("[\d]{1,3}").findall(d1[0])
            c1.append(int(d11[0]))
            d2 = re.compile("[\w]{1,4}").findall(b[j])
            c2.append(r2[r1.index(d2[0])])
        print(i, c1, c2)

        for q in range(0, len(c1)):
            df['model_answer'][i] = (c1[q] // c2[q])

    elif (re.compile("[\w]{1,4} [\d]{1,2}마리").findall(df["질문"][i])) and (
    (re.compile("[\w]{1,3}와 [\w]{1,3}의 다리 [\w]{0,2}를 ['세어 보니, 세었더니'] 모두 [\d]{1,3}개").findall(df["질문"][i]))) and (
    re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b1 = re.compile("[\w]{1,4} [\d]{1,2}마리").findall(df["질문"][i])
        b2 = re.compile("[\w]{1,4}와 [\w]{1,3}의 다리 [\w]{0,2}를 ['세어 보니, 세었더니'] 모두 [\d]{1,3}개").findall(df["질문"][i])
        b3 = re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])
        c1 = []  # 각 동물의 마리수
        c11 = []  # 모든 다리수
        c2 = []  # 동물의 다리수
        c22 = []  # 구하려는 동물의 다리수
        for j in range(0, len(b1)):
            d1 = re.compile("[\d]{1,2}마리").findall(b1[j])
            d11 = re.compile("[\d]{1,2}").findall(d1[0])
            c1.append(int(d11))
            d2 = re.compile("[\w]{1,4}").findall(b1[j])
            c2.append(r2[r1.index(d2[0])])
        d111 = re.compile("[\d]{1,3}개").findall(b2)
        d1111 = re.compile("[\d]{1,3}").findall(d111[0])
        c11.append(int(d1111))
        d22 = re.compile("[\w]{1,4}").findall(b3)
        c22.append(r2[r1.index(d22[0])])
        print(i, c1, c2, c11, c22)
        qq = 0
        for q in range(0, len(c1)):
            qq = qq + (c1[q] * c2[q])
        df['model_answer'][i] = ((c11[0] - qq) // c22[0])


    elif (re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])) and (
    (re.compile("[\w]{1,3}가 모두 [\d]{1,3}마리라면").findall(df["질문"][i]))) and (
    re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])):
        r1 = ['문어가', '강아지가', '오리가', '염소가', '닭이', '문어', '강아지', '오리', '염소', '닭', '토끼', '문어', '강아지는', '오리는', '염소는', '닭은',
              '토끼는', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b1 = re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])
        b2 = re.compile("[\w]{1,3}가 모두 [\d]{1,3}마리라면").findall(df["질문"][i])
        b3 = re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])
        c1 = []  # 각 동물의 마리수
        c11 = []  # 모든 다리수
        c2 = []  # 동물의 다리수
        c22 = []  # 구하려는 동물의 다리수
        for j in range(0, len(b2)):
            d1 = re.compile("[\d]{1,2}마리").findall(b2[j])
            d11 = re.compile("[\d]{1,2}").findall(d1[0])
            c1.append(int(d11[0]))
            d2 = re.compile("[\w]{1,3}").findall(b2[j])
            c2.append(r2[r1.index(d2[0])])
        d111 = re.compile("[\d]{1,3}개").findall(b1[0])
        d1111 = re.compile("[\d]{1,3}").findall(d111[0])
        c11.append(int(d1111[0]))
        d22 = re.compile("[\w]{1,4}").findall(b3[0])
        c22.append(r2[r1.index(d22[0])])
        print(i, c1, c2, c11, c22)
        qq = 0
        for q in range(0, len(c1)):
            qq = qq + (c1[q] * c2[q])
        df['model_answer'][i] = ((c11[0] - qq) // c22[0])

    elif (re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])) and (
    (re.compile("[\w]{1,3}['는,은'] [\d]{1,3}마리라면").findall(df["질문"][i]))) and (
    re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])):
        r1 = ['강아지는', '오리는', '염소는', '닭은', '토끼는', '문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의',
              '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b1 = re.compile("다리 수를 세어 보니 모두 [\d]{1,3}").findall(df["질문"][i])
        b2 = re.compile("[\w]{1,3}['는, 은'] [\d]{1,3}마리").findall(df["질문"][i])
        b3 = re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])
        c1 = []  # 각 동물의 마리수
        c11 = []  # 모든 다리수
        c2 = []  # 동물의 다리수
        c22 = []  # 구하려는 동물의 다리수
        for j in range(0, len(b2)):
            d1 = re.compile("[\d]{1,2}마리").findall(b2[j])
            d11 = re.compile("[\d]{1,2}").findall(d1[0])
            c1.append(int(d11[0]))
            d2 = re.compile("[\w]{1,3}").findall(b2[j])
            c2.append(r2[r1.index(d2[0])])
        d111 = re.compile("[\d]{1,2}").findall(b1[0])
        c11.append(int(d111[0]))
        d22 = re.compile("[\w]{1,4}").findall(b3[0])
        c22.append(r2[r1.index(d22[0])])
        print(i, c1, c2, c11, c22)
        qq = 0
        for q in range(0, len(c1)):
            qq = qq + (c1[q] * c2[q])
        df['model_answer'][i] = ((c11[0] - qq) // c22[0])

    elif (re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])) and (
    (re.compile("[\w]{1,3}와 [\w]{1,3}가 [\d]{1,3}, [\d]{1,3}마리라면").findall(df["질문"][i]))) and (
    re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])):
        r1 = ['문어', '강아지', '오리', '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4, 8, 4, 3, 4, 3, 4]
        b1 = re.compile("다리 수를 세어 보니 모두 [\d]{1,3}개").findall(df["질문"][i])
        b2 = re.compile("[\w]{1,3}와 [\w]{1,3}가 [\d]{1,3}, [\d]{1,3}마리라면").findall(df["질문"][i])
        b3 = re.compile("[\w]{1,4}['은, 는'] 몇 마리").findall(df["질문"][i])
        c1 = []  # 각 동물의 마리수
        c11 = []  # 모든 다리수
        c2 = []  # 동물의 다리수
        c22 = []  # 구하려는 동물의 다리수

        d1 = re.compile("[\d]{1,2}").findall(b2)
        for o in range(0, len(d1)):
            c1.append(int(d1[o]))
        d2 = re.compile("[\w]{1,3}").findall(b2)
        for o in range(0, len(d2)):
            c2.append(r2[r1.index(d2[o])])

        d111 = re.compile("[\d]{1,3}개").findall(b1)
        d1111 = re.compile("[\d]{1,3}").findall(d111[0])
        c11.append(int(d1111))
        d22 = re.compile("[\w]{1,4}").findall(b3)
        c22.append(r2[r1.index(d22[0])])
        print(i, c1, c2, c11, c22)
        qq = 0
        for q in range(0, len(c1)):
            qq = qq + (c1[q] * c2[q])
        df['model_answer'][i] = ((c11[0] - qq) // c22[0])

# %%

df22 = df.copy()
df22.head()
# df=df22
# df.head()

# %%

df = pd.read_excel("math_func_q_k_k1.xlsx")
df['model_answer'] = ''

for i in range(0, len(df)):
    if (re.compile("나이").findall(df["질문"][i])): print(i, df["질문"][i])

# %%

# df=pd.read_excel("math_func_q_k_k1.xlsx")
# df['model_answer']=''


for i in range(0, len(df)):
    if (re.compile("[\w]{1,5}['의 나이는,는,은'] [\d]{1,2}살").findall(df["질문"][i])) and (
    re.compile("보다 몇 살 더 많을까요?").findall(df["질문"][i])):
        a1 = re.compile("[\w]{1,5}['의 나이는,는,은'] [\d]{1,2}살").findall(df["질문"][i])
        a111 = []
        for j in range(0, len(a1)):
            a11 = re.compile("[\d]{1,2}").findall(a1[j])
            a111.append(a11[0])
        if len(a111) == 2:
            df["model_answer"][i] = abs(int(a111[0]) - int(a111[1]))

    elif (re.compile("의 나이를 더하면 [\d]{1,2}살").findall(df["질문"][i])) and (
    re.compile("의 나이가 [\d]{1,2}살이라면").findall(df["질문"][i])) and (re.compile("나이는 몇 살입니까").findall(df["질문"][i])):
        a1 = re.compile("의 나이를 더하면 [\d]{1,2}살").findall(df["질문"][i])
        a111 = []
        for j in range(0, len(a1)):
            a11 = re.compile("[\d]{1,2}").findall(a1[j])
            a111.append(a11[0])
        b1 = re.compile("의 나이가 [\d]{1,2}살이라면").findall(df["질문"][i])
        b111 = []
        for j in range(0, len(b1)):
            b11 = re.compile("[\d]{1,2}").findall(b1[j])
            b111.append(b11[0])
        df["model_answer"][i] = abs(int(a111[0]) - int(b111[0]))


    elif (re.compile("[\w]{1,5}['의 나이는,는,은'] [\d]{1,2}살").findall(df["질문"][i])) and (
    re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배['라면,입니다']").findall(df["질문"][i])):
        a1 = re.compile("[\w]{1,5}['의 나이는,는,은'] [\d]{1,2}살").findall(df["질문"][i])
        a111 = []
        for j in range(0, len(a1)):
            a11 = re.compile("[\d]{1,2}").findall(a1[j])
            a111.append(a11[0])
        b1 = re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배['라면,입니다']").findall(df["질문"][i])
        b111 = []
        for j in range(0, len(b1)):
            b11 = re.compile("[\d]{1,2}").findall(b1[j])
            b111.append(b11[0])
        df["model_answer"][i] = (int(a111[0]) * int(b111[0]))

for i in range(0, len(df)):
    if (re.compile("[\w]{1,5}['의 나이는,는,은'] [\d]{1,2}살").findall(df["질문"][i])) and (
    re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배보다 [\d]{1,2}살 더 많").findall(df["질문"][i])):
        a1 = re.compile("[\w]{1,5}['의 나이는,는,은'] [\d]{1,2}살").findall(df["질문"][i])
        a111 = []
        for j in range(0, len(a1)):
            a11 = re.compile("[\d]{1,2}").findall(a1[j])
            a111.append(a11[0])
        b1 = re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배보다 [\d]{1,2}살 더 많").findall(df["질문"][i])
        b111 = []
        for j in range(0, len(b1)):
            b11 = re.compile("[\d]{1,2}").findall(b1[j])
            b111.append(b11[0])
            b111.append(b11[1])
        if len(b111) == 2:
            df["model_answer"][i] = (int(a111[0]) * int(b111[0]) + int(b111[1]))

    elif (re.compile("[\w]{1,5}['의 나이는,는,은'] [\d]{1,2}살").findall(df["질문"][i])) and (
    re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배보다 [\d]{1,2}살 더 ['많습니다,많다면']").findall(df["질문"][i])) and (
    re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배['라면,입니다']").findall(df["질문"][i])):
        a1 = re.compile("[\w]{1,5}['의 나이는,는,은'] [\d]{1,2}살").findall(df["질문"][i])
        a111 = []
        for j in range(0, len(a1)):
            a11 = re.compile("[\d]{1,2}").findall(a1[j])
            a111.append(a11[0])
        b1 = re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배보다 [\d]{1,2}살 더 ['많습니다,많다면']").findall(df["질문"][i])
        b111 = []
        for j in range(0, len(b1)):
            b11 = re.compile("[\d]{1,2}").findall(b1[j])
            b111.append(b11[0])
            b111.append(b11[1])
        c1 = re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배['라면,입니다']").findall(df["질문"][i])
        c111 = []
        for j in range(0, len(c1)):
            c11 = re.compile("[\d]{1,2}").findall(c1[j])
            c111.append(c11[0])
        df["model_answer"][i] = (int(a111[0]) * int(b111[0]) + int(b111[1])) * int(c111[0])


    elif (re.compile("['는,은'] [\d]{1,2}살").findall(df["질문"][i])) and (
    re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배보다 [\d]{1,2}살 더 적").findall(df["질문"][i])):
        a1 = re.compile("['는,은'] [\d]{1,2}살").findall(df["질문"][i])
        a111 = []
        for j in range(0, len(a1)):
            a11 = re.compile("[\d]{1,2}").findall(a1[j])
            a111.append(a11[0])
        b1 = re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배보다 [\d]{1,2}살 더 적").findall(df["질문"][i])
        b111 = []
        for j in range(0, len(b1)):
            b11 = re.compile("[\d]{1,2}").findall(b1[j])
            b111.append(b11[0])
            b111.append(b11[1])
        df["model_answer"][i] = (int(a111[0]) * int(b111[0]) - int(b111[1]))

    elif (re.compile("['는,은'] [\d]{1,2}살").findall(df["질문"][i])) and (
    re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배보다 [\d]{1,2}살 더 적").findall(df["질문"][i])) and (
    re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배['라면,입니다']").findall(df["질문"][i])):
        a1 = re.compile("['는,은'] [\d]{1,2}살").findall(df["질문"][i])
        a111 = []
        for j in range(0, len(a1)):
            a11 = re.compile("[\d]{1,2}").findall(a1[j])
            a111.append(a11[0])
        b1 = re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배보다 [\d]{1,2}살 더 적").findall(df["질문"][i])
        b111 = []
        for j in range(0, len(b1)):
            b11 = re.compile("[\d]{1,2}").findall(b1[j])
            b111.append(b11[0])
            b111.append(b11[1])
        c1 = re.compile("[\w]{1,5}의 나이는 [\w]{1,5}의 나이의 [\d]{1,2}배['라면,입니다']").findall(df["질문"][i])
        c111 = []
        for j in range(0, len(c1)):
            c11 = re.compile("[\d]{1,2}").findall(c1[j])
            c111.append(c11[0])
        df["model_answer"][i] = (int(a111[0]) * int(b111[0]) - int(b111[1])) * int(c111[0])

# %%

www = [150, 170, 210, 321, 333, 346, 351]
for i in www:
    print(df["질문"][i])
    print(df['model_answer'][i])

# %%

for i in range(0, len(df)):
    if (re.compile("가위바위보").findall(df["질문"][i])): print(i, df["질문"][i])

# %%

# 가위바위보
for i in range(0, len(df)):
    if (re.compile("펼친 손가락은 모두 몇 개").findall(df["질문"][i])):
        r1 = ['가위', '바위', '보']
        r2 = [2, 0, 5]
        # r3=['보','가위','바위']
        r4 = [5, 2, 0]
        a = re.compile("[\d]{1,2}명의 [\w]{1,5}['이,가'] 가위바위보를").findall(df["질문"][i])
        a1 = re.compile("[\d]{1,2}").findall(a[0])
        if (re.compile("모두 ['가위,바위,보']를").findall(df["질문"][i])):
            b = re.compile("모두 ['가위,바위,보']를").findall(df["질문"][i])
            b1 = re.compile("['가위,바위,보']").findall(b[0])
            df["model_answer"][i] = r2[r1.index(b1[0])] * int(a1[0])
        elif (re.compile("['가위,바위,보']를 내서 이겼을 때").findall(df["질문"][i])):
            b = re.compile("[\w]{1,5} [\d]{1,2}명의").findall(df["질문"][i])
            bb = re.compile('[\w]{1,2}를 내서 이겼을 때').findall(df["질문"][i])
            b1 = re.compile("[\w]{1,2}").findall(bb[0])
            b2 = re.compile("[\d]{1,2}").findall(b[0])
            df["model_answer"][i] = r2[r1.index(b1[0])] * int(b2[0]) + r4[r1.index(b1[0])] * (int(a1[0]) - int(b2[0]))

# df["model_answer"][294]

# %%

for i in range(0, len(df)):
    if (re.compile("바르게 계산한 값").findall(df["질문"][i])): print(i, df["질문"][i])

# %%

# 잘못된 계산 바르게 계산한 값
for i in range(0, len(df)):
    r1 = ['더해야', '빼야', "곱해야", "나누어야", "나눠야"]
    r2 = ['더했', '뺐', "곱했", "나눴", "나누었"]
    if (re.compile("어떤 수에 [\d]{1,3}를 [\w]{2,3} 할 것을 잘못하여 [\d]{1,3}을 [\w]{1,3}더니 [\d]{1,5}").findall(df["질문"][i])):
        a = re.compile("어떤 수에 [\d]{1,5}를 [\w]{2,3} 할 것을 잘못하여 [\d]{1,5}을 [\w]{1,3}더니 [\d]{1,5}").findall(df["질문"][i])
        a1 = re.compile("어떤 수에 [\d]{1,5}를 [\w]{2,3} 할 것을 잘못하여").findall(a[0])
        a11 = re.compile("[\d]{1,5}").findall(a1[0])
        a11 = int(a11[0])
        a12 = re.compile("[\w]{2,3}").findall(a1[0])
        a2 = re.compile("[\d]{1,5}을 [\w]{1,3}더니 [\d]{1,5}").findall(a[0])
        a21 = re.compile("[\d]{1,5}").findall(a2[0])
        a211 = int(a21[0])
        a212 = int(a21[1])
        a22 = re.compile("[\w]{2,3}").findall(a2[0])
        ans = [
            [(a212 - a211) + a11, (a212 - a211) - a11, (a212 - a211) * a11, (a212 - a211) / a11, (a212 - a211) / a11],
            [(a212 + a211) + a11, (a212 + a211) - a11, (a212 + a211) * a11, (a212 + a211) / a11, (a212 + a211) / a11],
            [(a212 / a211) + a11, (a212 / a211) - a11, (a212 / a211) * a11, (a212 / a211) / a11, (a212 / a211) / a11],
            [(a212 * a211) + a11, (a212 * a211) - a11, (a212 * a211) * a11, (a212 * a211) / a11, (a212 * a211) / a11]]
        for k1, k2 in zip(range(0, 4), range(0, 4)):
            df["model_answer"][i] = ans[k1][k2]

# df["model_answer"][329]
