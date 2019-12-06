# %%

import pandas as pd

df = pd.read_excel("math_func_type.xlsx", sheet_name=3)
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
    if re.compile("몇 [\w]{1,5}가 필요하고, [\w]{0,5} 몇 [\w]{1,5}가 남을까요?").findall(df["질문"][i]) != []:
        print(i, df["질문"][i])

    elif re.compile("몇 [\w]{1,5}에게 나누어 줄 수 있고, 몇 [\w]{1,5}가 남을까요?").findall(df["질문"][i]) != []:
        print(i, df["질문"][i])

    elif re.compile("몇 [\w]{1,5}에게 나누어 줄 수 있을까요?").findall(df["질문"][i]) != []:
        print(i, df["질문"][i])

# %%

# basic


for i in range(0, len(df)):
    if (re.compile("몇 [\w]{1,5}가 필요하고, [\w]{0,5} 몇 [\w]{1,5}가 남을까요?").findall(df["질문"][i])) or (
            re.compile("몇 [\w]{1,5}에게 나누어 줄 수 있고, 몇 [\w]{1,5}가 남을까요?").findall(df["질문"][i]) != []) or (
            re.compile("몇 [\w]{1,5}에게 나누어 줄 수 있을까요?").findall(df["질문"][i]) != []) or (
            re.compile("몇 [\w]{1,5}필요합니까?").findall(df["질문"][i]) != []):
        if (re.compile("한 [\w]{1,5}['에,당'] [\d]{1,3}[\w]{1,5}씩 ['나누어, 나눠, 담는다면, 담으려면']").findall(df["질문"][i]) != []):
            if (re.compile("한 [\w]{1,5}['에,당'] [\d]{1,3}[\w]{1,5}씩 [\d]{1,3}[\w]{1,5}").findall(df["질문"][i]) != []):
                a = []
                a1 = re.compile("한 [\w]{1,5}['에,당'] [\d]{1,3}[\w]{1,5}씩 [\d]{1,3}[\w]{1,5}").findall(df["질문"][i])
                a11 = re.compile("[\d]{1,3}").findall(a1[0])
                a.append(int(a11[0]) * int(a11[1]))
                a2 = re.compile("한 [\w]{1,5}['에,당'] [\d]{1,3}[\w]{1,5}씩 ['나누어, 나눠, 담는다면, 담으려면']").findall(df["질문"][i])
                a22 = re.compile("[\d]{1,3}").findall(a2[0])
                a.append(int(a22[0]))

            elif (re.compile("[\d]{1,3}[\w]{1,5}씩 [\d]{1,3}[\w]{1,5}").findall(df["질문"][i]) != []):
                a = []
                a1 = re.compile("[\d]{1,3}[\w]{1,5}씩 [\d]{1,3}[\w]{1,5}").findall(df["질문"][i])
                a11 = re.compile("[\d]{1,3}").findall(a1[0])
                a.append(int(a11[0]) * int(a11[1]))
                a2 = re.compile("한 [\w]{1,5}['에,당'] [\d]{1,3}[\w]{1,5}씩 ['나누어, 나눠, 담는다면, 담으려면']").findall(df["질문"][i])
                a22 = re.compile("[\d]{1,3}").findall(a2[0])
                a.append(int(a22[0]))

            else:
                a = re.compile("[\d]{1,4}").findall(df["질문"][i])

            if (re.compile("남을까요").findall(df["질문"][i])):
                df["model_answer"][i] = [int(a[0]) // int(a[1]), int(a[0]) % int(a[1])]
            else:
                df["model_answer"][i] = int(a[0]) // int(a[1])

            print(i, df["model_answer"][i])

# %%

# if (re.compile("몇 [\w]{1,4}가 필요합니까?").findall(df["질문"][i])!=[])

# 의자 basic

for i in range(0, len(df)):
    if (re.compile("몇 [\w]{1,4}가 필요합니까?").findall(df["질문"][i]) != []) and (
            re.compile("[\d]{1,4}명이 모두 앉으려면").findall(df["질문"][i]) != []):
        a1 = re.compile("[\d]{1,4}명이 모두 앉으려면").findall(df["질문"][i])
        a11 = re.compile("[\d]{1,4}").findall(a1[0])
        a2 = re.compile("[\d]{1,4}명씩 앉을 수 있는 의자").findall(df["질문"][i])
        a22 = re.compile("[\d]{1,4}").findall(a2[0])
        if int(a11[0]) % int(a22[0]) != 0:
            df["model_answer"][i] = (int(a11[0]) // int(a22[0])) + 1
        else:
            df["model_answer"][i] = int(a11[0]) // int(a22[0])

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 동전 총 금액

for i in range(0, len(df)):
    if (re.compile("동전이 모두 [\d]{1,4}개").findall(df["질문"][i]) != []) and (
            re.compile("[\d]{1,4}원짜리").findall(df["질문"][i]) != []) and (
            re.compile("동전의 금액을 모두 더하면 얼마").findall(df["질문"][i]) != []):
        a1 = re.compile("동전이 모두 [\d]{1,4}개").findall(df["질문"][i])
        a11 = re.compile("[\d]{1,4}").findall(a1[0])
        a2 = re.compile("[\d]{1,4}원짜리").findall(df["질문"][i])
        a22 = []
        for jj in range(0, len(a2)):
            a22.append(int((re.compile("[\d]{1,4}").findall(a2[jj]))[0]))
        a3 = re.compile("[\d]{1,4}종류").findall(df["질문"][i])
        a33 = re.compile("[\d]{1,4}").findall(a3[0])
        k = int(a11[0]) // int(a33[0])

        df["model_answer"][i] = 0
        for j in range(0, len(a22)):
            df["model_answer"][i] = df["model_answer"][i] + (int(a22[j]) * k)

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 테이프나 리본으로 여러개 만들기
for i in range(0, len(df)):
    if (re.compile('테이프').findall(df["질문"][i]) != []) or (re.compile('리본').findall(df["질문"][i]) != []):
        if re.compile('전체 길이가 [\d]{1,2}cm').findall(df["질문"][i]) != []:
            c = re.compile('전체 길이가 [\d]{1,2}cm').findall(df["질문"][i])
        elif re.compile('[\d]{1,2}cm짜리 색 테이프').findall(df["질문"][i]) != []:
            c = re.compile('[\d]{1,2}cm짜리 색 테이프').findall(df["질문"][i])
        elif re.compile('색 테이프 [\d]{1,2}cm').findall(df["질문"][i]) != []:
            c = re.compile('색 테이프 [\d]{1,2}cm[\w]{1,20} 같은 [\w]{1,20} [\w]{1,20} 몇 개까지').findall(df["질문"][i])
        c1 = re.compile('[\d]{1,2}').findall(c[0])

        if (re.compile('겹쳐지는 부분이 [\d]{1,2}cm').findall(df["질문"][i]) != []) or (
                re.compile('전체 길이가 [\d]{1,2}cm').findall(df["질문"][i]) != []):
            a = re.compile('[\d]{1,2}개').findall(df["질문"][i])
            a1 = re.compile('[\d]{1,2}').findall(a[0])
            b = re.compile('겹쳐지는 부분이 [\d]{1,2}cm').findall(df["질문"][i])
            b1 = re.compile('[\d]{1,2}').findall(b[0])
            df["model_answer"][i] = (int(c1[0]) + int(b1[0]) * (int(a1[0]) - 1)) // int(a1[0])

        elif (re.compile('[\d]{1,2}cm짜리 [\w]{1,20} [\d]{1,2}개').findall(df["질문"][i]) != []):
            a = re.compile('[\d]{1,2}cm짜리 [\w]{1,20} [\d]{1,2}개').findall(df["질문"][i])
            a1 = re.compile('[\d]{1,2}cm').findall(a[0])
            a2 = re.compile('[\d]{1,2}개').findall(a[0])
            a11 = re.compile('[\d]{1,2}').findall(a1[0])
            a22 = re.compile('[\d]{1,2}').findall(a2[0])
            b = df["질문"][i].split("나머지")
            b1 = re.compile('[\d]{1,2}').findall(b[1])
            df["model_answer"][i] = (int(c1[0]) - int(a11[0]) * int(a22[0])) // int(b1[0])

        elif (re.compile('[\d]{1,2}cm로 [\w]{1,10}["을,를"] 한 개').findall(df["질문"][i]) != []):
            a = re.compile('[\d]{1,2}cm로 [\w]{1,10}["을,를"] 한 개').findall(df["질문"][i])
            a1 = re.compile('[\d]{1,2}').findall(a[0])
            df["model_answer"][i] = (int(c1[0]) // int(a1[0]))

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 일정간격으로 무언가를 두기
for i in range(0, len(df)):
    if (re.compile('간격').findall(df["질문"][i]) != []) and (re.compile('[\d]{1,2}[\w]{1,2}인').findall(df["질문"][i]) != []):
        if (re.compile('가로 [\w]{1,5}, 세로 [\w]{1,5}').findall(df["질문"][i]) != []):
            a = re.compile('가로 [\w]{1,5}, 세로 [\w]{1,5}').findall(df["질문"][i])
            aa = re.compile('[\d]{1,2}').findall(a[0])
            a1 = 2 * (int(aa[0]) + int(aa[1]))
        elif (re.compile('[\d]{1,2}[\w]{1,2}인').findall(df["질문"][i]) != []):
            a = re.compile('[\d]{1,2}m인').findall(df["질문"][i]) or re.compile('[\d]{1,2}cm인').findall(df["질문"][i])
            aa = re.compile('[\d]{1,2}').findall(a[0])
            a1 = int(aa[0])
        print(a1)

        if (re.compile('한 군데만').findall(df["질문"][i]) != []):
            b = re.compile('한 군데만 가운데에 길을 내기 위해 [\d]{1,2}[\w]{1,2} 간격').findall(df["질문"][i])
            b1 = re.compile('[\d]{1,2}').findall(b[0])
            c = re.compile('나머지는 모두 [\d]{1,2}[\w]{1,2} 간격').findall(df["질문"][i])
            c1 = re.compile('[\d]{1,2}').findall(c[0])
            k = abs(int(b1[0]) - int(c1[0]))
            df["model_answer"][i] = (a1 - k) // int(c1[0])

        else:
            c = re.compile('[\d]{1,2}[\w]{1,2} 간격').findall(df["질문"][i]) or re.compile('[\d]{1,2}[\w]{1,2}간격').findall(
                df["질문"][i])
            c1 = re.compile('[\d]{1,2}').findall(c[0])
            if (re.compile('단').findall(df["질문"][i]) != []):
                if (re.compile('처음과 끝').findall(df["질문"][i]) != []) or (re.compile('양끝').findall(df["질문"][i]) != []):
                    if (re.compile('않').findall(df["질문"][i]) != []):
                        if a1 % int(c1[0]) != 0:
                            df["model_answer"][i] = a1 // int(c1[0])
                        else:
                            df["model_answer"][i] = (a1 // int(c1[0])) - 1
                    else:
                        df["model_answer"][i] = (a1 // int(c1[0])) + 1
                if (re.compile('모서리').findall(df["질문"][i]) != []):
                    if (re.compile('않').findall(df["질문"][i]) != []): df["model_answer"][i] = (a1 // int(c1[0])) - 4

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 매일 똑같은 수
for i in range(0, len(df)):
    if (re.compile('[\d]{1,2}[\w]{1,2}가 하루에 [\w]{1,2}["을,를"] [\d]{1,2}[\w]{1,2}').findall(df["질문"][i]) != []):
        a = re.compile('[\d]{1,2}[\w]{1,2}가 하루에 [\w]{1,2}["을,를"] [\d]{1,2}[\w]{1,2}').findall(df["질문"][i])
        aa = re.compile('[\d]{1,2}').findall(a[0])
        b = df["질문"][i].split("다면")
        bb = re.compile('[\d]{1,2}').findall(b[1])
        df["model_answer"][i] = int(bb[1]) // ((int(aa[1]) // int(aa[0])) * int(bb[0]))

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 연필 몇타
for i in range(0, len(df)):
    if re.compile("연필[\w]{0,2} [\d]{1,2}타").findall(df["질문"][i]) != []:
        a = re.compile("연필[\w]{0,2} [\d]{1,2}타").findall(df["질문"][i])
        aa = re.compile("[\d]{1,2}").findall(a[0])
        a1 = 12 * int(aa[0])

        b = re.compile("[\d]{1,2}자루씩").findall(df["질문"][i]) or re.compile("[\d]{1,2}명에게").findall(df["질문"][i])
        bb = re.compile("[\d]{1,2}").findall(b[0])
        if re.compile("나머지").findall(df["질문"][i]) == []:
            df["model_answer"][i] = a1 // int(bb[0])
        else:
            df["model_answer"][i] = [a1 // int(bb[0]), a1 % int(bb[0])]

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 한변 길이
for i in range(0, len(df)):
    if (re.compile("둘레의 길이").findall(df["질문"][i]) != []) or (re.compile("변의 길이의 합").findall(df["질문"][i]) != []) or (
            re.compile("개의 변으로 둘러싸인 도형").findall(df["질문"][i]) != []) or (
            re.compile("변의 길이를 모두 더하였더니").findall(df["질문"][i]) != []):
        r1 = ['정사각형', '세 변', '정삼각형']
        r2 = [4, 3, 3]
        a = (re.compile("둘레의 길이가 각각 [\w]{1,10} [\d]{1,2}").findall(df["질문"][i])) or (
            re.compile("둘레의 길이가 [\d]{1,2}").findall(df["질문"][i])) or (
                re.compile("변의 길이의 합이 [\d]{1,2}").findall(df["질문"][i])) or (
                re.compile("변의 길이를 모두 더하였더니 [\d]{1,2}").findall(df["질문"][i]))
        a = re.compile("[\d]{1,2}").findall(a[0])
        b = (re.compile("[\d]{1,2}개의 변으로 둘러싸인 도형").findall(df["질문"][i]))
        if b != []:
            b = re.compile("[\d]{1,2}").findall(b[0])

        for r in r1:
            if re.compile(r).findall(df["질문"][i]): b.append(r2[r1.index(r)])

        if (re.compile("때,").findall(df["질문"][i]) != []):
            if (re.compile("똑같은 [\w]{4} [\d]{1,2}개로 나누어져").findall(df["질문"][i]) != []):
                c = re.compile("똑같은 [\w]{4} [\d]{1,2}개로 나누어져").findall(df["질문"][i])
                c1 = re.compile("[\d]{1,2}").findall(c[0])
                c2 = re.compile("[\w]{4}").findall(c[0])
                c2 = [r2[r1.index(c2[0])]]
                if (re.compile("변의 길이의 합").findall(df["질문"][i]) != []):
                    df["model_answer"][i] = ((int(a[0]) // int(b[0])) // int(c1[0])) * int(c2[0])
            elif (re.compile("[\w]{4}의 한 변의 길이와 한 변의 길이가 같은 [\w]{4}이 있을 때").findall(df["질문"][i]) != []):
                c = re.compile("[\w]{4}의 한 변의 길이와 한 변의 길이가 같은 [\w]{4}이 있을 때").findall(df["질문"][i])
                c = re.compile("[\w]{4}").findall(c[0])
                c2 = []
                for j in range(0, len(c)):
                    c2.append(r2[r1.index(c[j])])
                if (re.compile("변의 길이의 합").findall(df["질문"][i]) != []):
                    df["model_answer"][i] = (int(a[0]) // int(c2[0])) * int(c2[1])

        elif (re.compile("한 변의 길이의 차").findall(df["질문"][i]) != []):
            df["model_answer"][i] = abs(int(a[0]) - int(a[1])) // int(b[0])

        elif (re.compile("한 [\w]{1,2}의 길이[\w]{1} 몇").findall(df["질문"][i]) != []):
            df["model_answer"][i] = int(a[0]) // int(b[0])

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 하루분량
for i in range(0, len(df)):
    if ((re.compile("매일 똑같은").findall(df["질문"][i]) != []) or (re.compile("매일 같은").findall(df["질문"][i]) != []) or (
            re.compile("하루에").findall(df["질문"][i]) != [])):
        if (re.compile("[\w]{1}주일 동안").findall(df["질문"][i]) != []) or (
                re.compile("[\w]{1}주일동안").findall(df["질문"][i]) != []):

            r1 = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
            r2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            a = re.compile("[\w]{1}주일 동안").findall(df["질문"][i]) or re.compile("[\w]{1}주일동안").findall(df["질문"][i])
            if a != []:
                a = re.compile("[\w]{1}").findall(a[0])
                a = [r2[r1.index(a[0])]]
                b = re.compile("[\d]{1,4}").findall(df["질문"][i])
                df["model_answer"][i] = int(b[0]) // (7 * (int(a[0])))

                if re.compile("나머지는 [\w]{1}주일 동안").findall(df["질문"][i]):
                    df["model_answer"][i] = abs(int(b[0]) - int(b[1])) // (7 * (int(a[0])))

                print(i, df["질문"][i], df["model_answer"][i])

# %%

# 층수 시간
for i in range(0, len(df)):
    if ((re.compile("[\d]{1,3}층부터 [\d]{1,3}층까지 [\w]{1,4} 데 [\d]{1,3}초가 걸렸다면").findall(df["질문"][i]) != []) or (
            re.compile("[\d]{1,3}층부터 [\d]{1,3}층까지 [\w]{1,4} [\w]{1,2} 몇 초").findall(df["질문"][i]) != [])):
        a = (re.compile("[\d]{1,3}층부터 [\d]{1,3}층까지 [\w]{1,4} 데 [\d]{1,3}초가 걸렸다면").findall(df["질문"][i]))
        b = (re.compile("[\d]{1,3}층부터 [\d]{1,3}층까지 [\w]{1,4} [\w]{1,2} 몇 초").findall(df["질문"][i]))
        a = re.compile("[\d]{1,3}").findall(a[0])
        b = re.compile("[\d]{1,3}").findall(b[0])
        for j in range(0, len(a)):
            a[j] = int(a[j])
        for j in range(0, len(b)):
            b[j] = int(b[j])
        df["model_answer"][i] = (a[2] / abs(a[0] - a[1])) * abs(b[0] - b[1])

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 일부 출발하고 추가로 필요한 차랑
for i in range(0, len(df)):
    if (re.compile(
            "[\d]{1,3}명이 현장학습을 갑니다. [\d]{1,3}명씩 탄 버스 [\d]{1,3}대가 출발하고 남은 학생들은 [\d]{1,3}명씩 탈 수 있는 차에 타려고 합니다. 차는 ").findall(
            df["질문"][i]) != []) or (re.compile(
            "[\d]{1,3}명이 현장 학습을 갑니다. [\d]{1,3}명씩 탈 수 있는 버스가 [\d]{1,3}대 출발하고, 남은 학생들은 [\d]{1,3}명씩 탈 수 있는 승합차를 이용하였다면, ").findall(
            df["질문"][i]) != []):
        print(i)
        a = re.compile(
            "[\d]{1,3}명이 현장학습을 갑니다. [\d]{1,3}명씩 탄 버스 [\d]{1,3}대가 출발하고 남은 학생들은 [\d]{1,3}명씩 탈 수 있는 차에 타려고 합니다. 차는").findall(
            df["질문"][i]) or re.compile(
            "[\d]{1,3}명이 현장 학습을 갑니다. [\d]{1,3}명씩 탈 수 있는 버스가 [\d]{1,3}대 출발하고, 남은 학생들은 [\d]{1,3}명씩 탈 수 있는 승합차를 이용하였다면,").findall(
            df["질문"][i])
        a = re.compile("[\d]{1,3}").findall(a[0])
        for j in range(0, len(a)):
            a[j] = int(a[j])
        df["model_answer"][i] = (a[0] - (a[1] * a[2])) // a[3]
        if (a[0] - (a[1] * a[2])) % a[3] != 0: df["model_answer"][i] = df["model_answer"][i] + 1

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 얼마나 시간이 걸리는지
for i in range(0, len(df)):
    if re.compile("1[\w]{1,3}은 [\d]{1,3}[\w]{1,3}입니다").findall(df["질문"][i]) != []:
        a = re.compile("1[\w]{1,3}은 [\d]{1,3}[\w]{1,3}입니다").findall(df["질문"][i])
        a = re.compile("[\d]{1,3}").findall(a[0])
        b = re.compile("[\w]{1,3}[\w]{1,3} ['며,몇']").findall(df["질문"][i])
        b = re.compile("[\d]{1,3}").findall(b[0])

        df["model_answer"][i] = [int(b[0]) // int(a[1]), int(b[0]) % int(a[1])]

    elif re.compile("한 계절에는 몇 번의 절기").findall(df["질문"][i]) != []:
        r1 = ['일 년', '한 계절', '한 시간', '일 분']
        r2 = [12, 3, 60.60]
        a = []
        for r in r1:
            if r in df['질문'][i]:
                a.append(r2[r1.index(r)])
        b = re.compile("일 년을 24로 나눈 것").findall(df["질문"][i])
        b = re.compile("[\d]{1,3}").findall(b[0])
        df["model_answer"][i] = int(b[0]) // a[0] * a[1]

        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 일부 버리고 나누기
for i in range(0, len(df)):
    if (re.compile("중").findall(df["질문"][i]) != []):
        if (re.compile("남은").findall(df["질문"][i]) != []) or (re.compile("나머지").findall(df["질문"][i]) != []):
            a = df["질문"][i].split(".")
            b = re.compile(a[0]).findall(df["질문"][i])
            b = re.compile("[\d]{1,4}").findall(b[0])
            if len(b) == 2:
                b = [int(b[0]) * int(b[1])]
            if len(b) == 1: b = [int(b[0])]
            c1 = a[1].split("고")
            # print(len(a))
            # print(c1)
            c = re.compile("[\d]{1,4}").findall(c1[0])
            if re.compile("씩").findall(c1[0]): c = [int(c[0]) * int(c[1])]
            if (c == []) and (re.compile("한 ").findall(c1[0])): c = [1]

            if len(a) == 3:
                d = re.compile("[\d]{1,4}").findall(c1[1])
            else:
                d = re.compile("[\d]{1,4}").findall(a[2])

            if d == []:
                d = [b[0]]
                b = [c[0]]
                c = [c[1]]

            # print(b)
            # print(c) #뺄것
            # print(d)
            if (re.compile("몇 개가 남습니까?").findall(df["질문"][i]) != []):
                df["model_answer"][i] = [(int(b[0]) - int(c[0])) // int(d[0]), (int(b[0]) - int(c[0])) % int(d[0])]
            else:
                df["model_answer"][i] = (int(b[0]) - int(c[0])) // int(d[0])
            print(i, df["질문"][i], df["model_answer"][i])

    elif (re.compile("잘라내고 나머지").findall(df["질문"][i]) != []) or (re.compile("남겨 두고 나머지").findall(df["질문"][i]) != []):
        a = df["질문"][i].split(".")
        b = re.compile(a[0]).findall(df["질문"][i])
        b = re.compile("[\d]{1,4}").findall(b[0])
        if len(b) == 2:
            b = [int(b[0]) * int(b[1])]
        if len(b) == 1: b = [int(b[0])]
        c1 = a[1].split("고")
        # print(len(a))
        # print(c1)
        c = re.compile("[\d]{1,4}").findall(c1[0])
        if re.compile("씩").findall(c1[0]): c = [int(c[0]) * int(c[1])]
        if (c == []) and (re.compile("한 ").findall(c1[0])): c = [1]

        if len(a) == 3:
            d = re.compile("[\d]{1,4}").findall(c1[1])
        else:
            d = re.compile("[\d]{1,4}").findall(a[2])

        if d == []:
            d = [b[0]]
            b = [c[0]]
            c = [c[1]]

        # print(b)
        # print(c) #뺄것
        # print(d)

        if (re.compile("몇 개가 남습니까?").findall(df["질문"][i]) != []):
            df["model_answer"][i] = [(int(b[0]) - int(c[0])) // int(d[0]), (int(b[0]) - int(c[0])) % int(d[0])]
        else:
            df["model_answer"][i] = (int(b[0]) - int(c[0])) // int(d[0])
        print(i, df["질문"][i], df["model_answer"][i])

    elif (re.compile("똑같이 나누어").findall(df["질문"][i]) != []) or (re.compile("똑같게 나누어").findall(df["질문"][i]) != []):
        if (re.compile("남았습니다").findall(df["질문"][i]) != []) or (re.compile("남을까요").findall(df["질문"][i]) != []):
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            for j in range(0, len(a)):
                a[j] = int(a[j])
            if len(a) == 2:
                df["model_answer"][i] = [max(a) // min(a), max(a) % min(a)]
            else:
                b1 = df["질문"][i].split("를")
                b2 = re.compile("[\d]{1,4}").findall(b1[0])
                b3 = re.compile("[\d]{1,4}").findall(b1[1])
                if b2 == []:
                    b2 = b2 + re.compile("[\d]{1,4}").findall(b1[1].split(",")[0])
                    if len(b2) == 2:
                        b2 = [int(b2[0]) * int(b2[1])]
                        df["model_answer"][i] = (int(b2[0]) + int(b3[-1]))
                else:
                    df["model_answer"][i] = (int(b2[0]) - int(b3[1])) // int(b3[0])
            print(i, df["질문"][i], df["model_answer"][i])

# %%

# 남김없이 나눠주기
for i in range(0, len(df)):
    if (re.compile("똑같이 나누어").findall(df["질문"][i]) != []):
        if (re.compile("남는 것이 없도록").findall(df["질문"][i]) != []) or (re.compile("남김없이").findall(df["질문"][i]) != []):
            a = re.compile("[\d]{1,2}").findall(df["질문"][i])
            if len(a) == 3:
                k = a[0]
                for j in range(1, len(a)):
                    if k < a[j]: k = a[j]
                del a[a.index(k)]
                k2 = int(a[0]) + int(a[1])
                a = [k, str(k2)]

            if (int(max(a))) % (int(min(a))) != 0:
                df["model_answer"][i] = int(min(a)) - (int(max(a)) % int(min(a)))
            print(i, df["질문"][i], df["model_answer"][i])

# %%

# 수를 세고 전체에서 나누기
for i in range(0, len(df)):
    if (re.compile("가 똑같게 나누어").findall(df["질문"][i]) != []) or (re.compile("모두 합해").findall(df["질문"][i]) != []):
        a = df["질문"][i].split(".")
        a = a[0].split(",")
        b = re.compile("[\d]{1,5}").findall(df["질문"][i])
        if len(b) == 1: df["model_answer"][i] = int(b[0]) // len(a)
        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 누구와 친구가 일정수로 나눠서 하루에 일정개수 사용하면 며칠간 사용가능?
for i in range(0, len(df)):
    if (re.compile("[\w]{2,4}와 친구 [\d]{1,2}명").findall(df["질문"][i]) != []):
        a1 = re.compile("[\w]{2,4}와 친구 [\d]{1,2}명").findall(df["질문"][i])
        a = re.compile("[\d]{1,2}").findall(a1[0])
        a = int(a[0]) + 1
        b1 = re.compile("하루에 [\w]{2,4}['를,을'] [\d]{1,2}[\w]{1,4}씩").findall(df["질문"][i]) or re.compile(
            "하루에 [\d]{1,2}[\w]{1,4}씩").findall(df["질문"][i])

        b = re.compile("[\d]{1,2}").findall(b1[0])
        b = int(b[0])
        c1 = re.compile("[\d]{1,2}").findall(df["질문"][i])
        for j in range(0, len(c1)):
            c1[j] = int(c1[j])
        c = c1[0]
        for j in range(1, len(c1)):
            if c < c1[j]: c = c1[j]
        df["model_answer"][i] = (c / a) / b
        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 나르는데 걸리는 시간 구하기
for i in range(0, len(df)):
    if (re.compile("한 번 나르는 데 [\d]{1,2}분 걸린다면, 모두 나르는 데에 걸리는 시간").findall(df["질문"][i]) != []):
        a1 = re.compile("한 번에 [\d]{1,2}[\w]{1,4}씩").findall(df["질문"][i])
        a = int(re.compile("[\d]{1,2}").findall(a1[0])[0])  # 한번에 몇개씩
        b1 = re.compile("한 번 나르는 데 [\d]{1,2}분 걸린다면, 모두 나르는 데에 걸리는 시간").findall(df["질문"][i])
        b = int(re.compile("[\d]{1,2}").findall(b1[0])[0])  # 나르는데 걸리는 시간
        c1 = re.compile("[\d]{1,2}").findall(df["질문"][i])
        for j in range(0, len(c1)):
            c1[j] = int(c1[j])
        c = c1[0]
        for j in range(1, len(c1)):
            if c < c1[j]: c = c1[j]
        df["model_answer"][i] = (c / a) * b
        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 배추 뽑고 팔기
for i in range(0, len(df)):
    if (re.compile("판매한 금액은 모두 얼마").findall(df["질문"][i]) != []) and (re.compile("남은").findall(df["질문"][i]) != []):
        a = df["질문"][i].split(".")
        b = re.compile("[\d]{1,2}").findall(a[0])
        if re.compile("씩").findall(a[0]) != [] and len(b) == 2:
            b = int(b[0]) * int(b[1])  # 총수
        if re.compile("한 묶음에 [\d]{1,4}만 원").findall(a[1]) != [] and re.compile("[\d]{1,2}[\w]{1,2}씩 묶어서").findall(
                a[1]) != []:
            c1 = re.compile("한 묶음에 [\d]{1,4}만 원").findall(a[1])
            c1 = re.compile("[\d]{1,2}").findall(c1[0])
            c2 = re.compile("[\d]{1,2}[\w]{1,2}씩 묶어서").findall(a[1])
            c2 = re.compile("[\d]{1,2}").findall(c2[0])
        df["model_answer"][i] = [30000 * (b // int(c2[0])), b % int(c2[0])]
        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 새로운 사람 포함하여 운동장에 줄 세우기
for i in range(0, len(df)):
    if (re.compile("교실").findall(df["질문"][i]) != []) and (re.compile("운동장").findall(df["질문"][i]) != []):
        a = re.compile("한 줄에 [\d]{1,2}[\w]{1,4}씩 [\d]{1,4}줄로 서 있습니다").findall(df["질문"][i])
        a = re.compile("[\d]{1,2}").findall(a[0])
        a = int(a[0]) * int(a[1])
        b1 = re.compile("중 [\d]{1,2}명이 교실에 들어가고").findall(df["질문"][i])  # 뺄 것
        b1 = re.compile("[\d]{1,2}").findall(b1[0])
        b2 = re.compile("교실에 있던 [\d]{1,2}명이 운동장으로").findall(df["질문"][i])  # 더할 것
        b2 = re.compile("[\d]{1,2}").findall(b2[0])
        c = re.compile("한 줄에 [\d]{1,2}명씩 세우면 몇 줄").findall(df["질문"][i])
        c = re.compile("[\d]{1,2}").findall(c[0])
        df["model_answer"][i] = (a - int(b1[0]) + int(b2[0])) // int(c[0])
        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 모둠으로 나눈 후 몇개씩 주기
for i in range(0, len(df)):
    if (re.compile("한 모둠에 [\d]{1,2}개씩 나누어 주려면").findall(df["질문"][i]) != []):
        c1 = re.compile("[\d]{1,2}").findall(df["질문"][i])
        for j in range(0, len(c1)):
            c1[j] = int(c1[j])
        c = c1[0]
        for j in range(1, len(c1)):
            if c < c1[j]: c = c1[j]  # 총 인원
        a1 = re.compile("[\d]{1,2}명씩 한 모둠").findall(df["질문"][i])
        a = re.compile("[\d]{1,2}").findall(a1[0])
        b1 = re.compile("한 모둠에 [\d]{1,2}[\w]{1,2}씩").findall(df["질문"][i])
        b = re.compile("[\d]{1,2}").findall(b1[0])
        df["model_answer"][i] = (c // int(a[0])) * int(b[0])
        print(i, df["질문"][i], df["model_answer"][i])

# %%

# 몇명모여
for i in range(0, len(df)):
    if (re.compile("남은 사람을 뺀 다음, 다시").findall(df["질문"][i]) != []) and (
            re.compile("빠진 사람은 모두 몇 명").findall(df["질문"][i]) != []):
        c1 = re.compile("[\d]{1,2}").findall(df["질문"][i])
        for j in range(0, len(c1)):
            c1[j] = int(c1[j])
        c = c1[0]
        for j in range(1, len(c1)):
            if c < c1[j]: c = c1[j]  # 총 인원
        bb = df["질문"][i].split("뺀 다음, 다시")
        b1 = re.compile("[\d]{1,2}명씩").findall(bb[0])
        b1 = re.compile("[\d]{1,2}").findall(b1[0])
        b2 = re.compile("[\d]{1,2}명씩").findall(bb[1])
        b2 = re.compile("[\d]{1,2}").findall(b2[0])
        df["model_answer"][i] = (c % int(b1[0])) + ((c // int(b1[0])) * int(b1[0])) % int(b2[0])
        print(i, df["질문"][i], df["model_answer"][i])

# %%

#  두 그룹 각각 나눈 몫 비교 후 그의 차이(완료) 준희 / 진영
for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df["질문"][i])
    if (re.compile("나누어 ['가집니다','담겨']").findall(df["질문"][i]) != []):
        if re.compile("모둠에서는 딱지 [\d]{1,4}장을").findall(df["질문"][i]) != []:
            if (int(a[0]) > int(a[1])) & (int(a[2]) > int(a[3])):
                x = int(a[0]) / int(a[1])
                y = int(a[2]) / int(a[3])
                z = x - y

                df["model"][i] = [int(a[0]) / int(a[1]), int(a[2]) / int(a[3])]
                df["model_answer"][i] = [x - y]
                print(i, df["질문"][i], df["model_answer"][i])

    if re.compile("[\d]{1,4}묶음으로 나누어").findall(df["질문"][i]) != []:
        if re.compile("색종이를 [\d]{1,4}[\w]]"):
            if (int(a[1]) > int(a[0])) & (int(a[3]) > int(a[2])):
                x1 = int(a[1]) / int(a[0])
                y1 = int(a[3]) / int(a[2])
                z1 = x1 - y1

                df["model"][i] = [int(a[1]) / int(a[0]), int(a[3]) / int(a[2])]
                df["model_answer"][i] = [x1 - y1]
                print(i, df["질문"][i], df["model_answer"][i])

# %%

## 파란색 공 빨간색 공 상자에 똑같게 나누어
for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df['질문'][i])
    if (re.compile("[\w]색 공")).findall(df['질문'][i]) != []:
        if int(a[0]) > int(a[1]):
            x = (int(a[0]) + int(a[1])) + int(a[0])
            y = x / int(a[2])
            df["model"][i] = [(int(a[0]) + int(a[1])) + int(a[0])]
            df["model_answer"][i] = [x / int(a[2])]
            print(i, df["질문"][i], df["model_answer"][i])

# %%

# ## 한 명에게 몇개씩 나누어 주었더니  남았습니다
for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df['질문'][i])
    if (re.compile("[\d][\w]['가','이'] 남았습니다").findall(df['질문'][i]) != []) and (
            (re.compile("다시")).findall(df['질문'][i]) == []):
        if int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), "/", int(a[1])]
            df["model_answer"][i] = [int(int(a[0]) / int(a[1]))]
            print(i, df["질문"][i], df["model_answer"][i])

# %%

#  형 변환을 해야함
for i in range(0, len(df)):
    a = re.compile("[\d]{1,4}").findall(df['질문'][i])
    if (re.compile("두 학급의 남학생들을")).findall(df['질문'][i]) != [] or (
            re.compile("고구마는 몇 개가 남겠습니까").findall(df['질문'][i]) != []) or (
            re.compile("지우개는 적어도").findall(df['질문'][i]) != []) or (re.compile("민우네").findall(df['질문'][i]) != []):
        b = df["질문"][i].split('.')
        if (re.compile("[\d]{1,3}명").findall(b[0]) != []) or (re.compile("[\d]{1,3}개").findall(b[0]) != []):
            b1 = (re.compile("[\d]{1,3}명").findall(b[0]) or re.compile("[\d]{1,3}개").findall(b[0]))
            a1 = []
            for j in range(0, len(b1)):
                a1.append(re.compile("[\d]{1,4}").findall(b1[j])[0])
        a1_front = int(a1[0]) + int(a1[1])

        if re.compile("[\d]{1,3}").findall(b[1]) != []:
            b2 = (re.compile("[\d]{1,3}").findall(b[1]))
            b2 = int(b2[0])

            df["model"][i] = [a1_front, "/", b2]
            if re.compile("적어도 몇").findall(df["질문"][i]) != []:
                if a1_front % b2 != 0: df["model_answer"][i] = (a1_front // b2) + 1
            elif re.compile("남겠습니까").findall(df["질문"][i]) != []:
                df["model_answer"][i] = [a1_front // b2, a1_front % b2]
            else:
                df["model_answer"][i] = a1_front / b2

            print(i, df["질문"][i], df["model_answer"][i])

# %%

for i in range(0, len(df)):
    if (re.compile("다리를 세었더니 모두 [\d]{1,4}개").findall(df["질문"][i])) or (
    re.compile("다리를 세어 보니 모두 [\d]{1,4}개").findall(df["질문"][i])) or (
    re.compile("다리 수를 세어 보니 모두 [\d]{1,4}개").findall(df["질문"][i])):
        a1 = (re.compile("다리를 세었더니 모두 [\d]{1,4}개").findall(df["질문"][i])) or (
            re.compile("다리를 세어 보니 모두 [\d]{1,4}개").findall(df["질문"][i])) or (
                 re.compile("다리 수를 세어 보니 모두 [\d]{1,4}개").findall(df["질문"][i]))
        a = int(re.compile("[\d]{1,4}").findall(a1[0])[0])  # 총 다리수
        r1 = ['문어가', '강아지가', '오리가', '염소가', '닭이', '토끼가', '문어는', '강아지는', '오리는', '염소는', '닭은', '토끼는', '문어', '강아지', '오리',
              '염소', '닭', '토끼', '문어의', '강아지의', '오리의', '염소의', '닭의', '토끼의']
        r2 = [8, 4, 2, 4, 2, 4, 8, 4, 2, 4, 2, 4, 8, 4, 2, 4, 2, 4, 8, 4, 2, 4, 2, 4]
        b = []
        if re.compile("[\w]{1,4} [\d]{1,3}마리").findall(df["질문"][i]) != []:
            b = re.compile("[\w]{1,4} [\d]{1,3}마리").findall(df["질문"][i])
        if re.compile("[\w]{1,4} [\w]{1,4} 모두 [\d]{1,3}마리라면").findall(df["질문"][i]) != []:
            b = re.compile("[\w]{1,4} 모두 [\d]{1,3}마리라면").findall(df["질문"][i])
        c = []  # 기존동물 다리수
        for j in range(0, len(b)):
            if re.compile("[\w]{1,4}").findall(b[j])[0] in r1:
                c.append(r2[r1.index(re.compile("[\w]{1,4}").findall(b[j])[0])])
            b[j] = int(re.compile("[\d]{1,3}").findall(b[j])[0])  # 기존 동물수

        if re.compile("[\w]{1,4} 몇 마리").findall(df["질문"][i]) != []:
            d = re.compile("[\w]{1,4} 몇 마리").findall(df["질문"][i])
            d = [r2[r1.index(re.compile("[\w]{1,4}").findall(d[0])[0])]]  # 구하고 싶은 동물 다리수

        if b == []:
            df["model_answer"][i] = a // d[0]
        else:
            for k in range(0, len(b)):
                a = a - b[k] * c[k]
            df["model_answer"][i] = a // d[0]
        print(i, df["질문"][i], df["model_answer"][i])

# %%

for i in range(0, len(df)):
    if (re.compile("바퀴 수를 세었더니").findall(df["질문"][i])):
        r1 = ["오토바이", "오토바이는", "오토바이가", "승용차", '자동차', "승용차는", '자동차는', '승용차가', '자동차가', '세발자전거', '세발자전거가', '두발자전거',
              '세발자전거는', '두발자전거는']
        r2 = [2, 2, 2, 4, 4, 4, 4, 4, 4, 3, 3, 2, 3, 2]
        a = re.compile("바퀴 수를 세었더니 모두 [\d]{1,2}개").findall(df["질문"][i])
        a = re.compile("[\d]{1,2}").findall(a[0])  # 총 바퀴수
        b = re.compile("[\w]{1,10} [\d]{1,2}대").findall(df["질문"][i])
        c1 = []
        c2 = []
        for j in range(0, len(b)):
            d1 = re.compile("[\d]{1,2}대").findall(b[j])
            c1.append(int(d1[0][0]))
            d2 = re.compile("[\w]{1,10}").findall(b[j])
            c2.append(r2[r1.index(d2[0])])
        c = c1[0] * c2[0]  # 주어진 총 바퀴개수
        d = re.compile("[\w]{1,6} 몇 대").findall(df["질문"][i])
        d = re.compile("[\w]{1,6}").findall(d[0])
        d = r2[r1.index(d[0])]  # 구할것의 바퀴수

        df['model_answer'][i] = (int(a[0]) - c) // d
        print(i, df['질문'][i], df['model_answer'][i])

# %%

for i in range(0, len(df)):
    if (re.compile("정사각형").findall(df["질문"][i])):
        if (re.compile("가로가 [\d]{1,3}[\w]{1,10}, 세로가 [\d]{1,3}[\w]{1,10}").findall(df["질문"][i])) or (
        re.compile("가로 [\d]{1,3}[\w]{1,10}, 세로 [\d]{1,3}[\w]{1,10}").findall(df["질문"][i])):
            a1 = re.compile("가로가 [\d]{1,3}[\w]{1,10}, 세로가 [\d]{1,3}[\w]{1,10}").findall(df["질문"][i]) or (
                re.compile("가로 [\d]{1,3}[\w]{1,10}, 세로 [\d]{1,3}[\w]{1,10}").findall(df["질문"][i]))
            a = re.compile("[\d]{1,3}").findall(a1[0])
            b1 = re.compile("한 변의 길이가 [\d]{1,3}[\w]{1,10}").findall(df["질문"][i])
            b = re.compile("[\d]{1,3}").findall(b1[0])
            df['model_answer'][i] = (int(a[0]) // int(b[0])) * (int(a[1]) // int(b[0]))
            print(i, df['질문'][i], df['model_answer'][i])

        elif (re.compile("철사").findall(df["질문"][i])) and (re.compile("한 변의 길이").findall(df["질문"][i])):
            a = (re.compile("[\d]{1,3}").findall(df["질문"][i]))
            if len(a) == 2:
                if int(a[0]) > int(a[1]):
                    df['model_answer'][i] = (int(a[0]) // int(a[1])) // 4
                elif int(a[1]) > int(a[0]):
                    df['model_answer'][i] = (int(a[1]) // int(a[0])) // 4
                print(i, df['질문'][i], df['model_answer'][i])
            elif len(a) == 1:
                df['model_answer'][i] = int(a[0]) // 4
                print(i, df['질문'][i], df['model_answer'][i])

# %%

for i in range(0, len(df)):
    if re.compile("[\d]{1,4}일은 몇 주이며 나머지").findall(df["질문"][i]):
        a = int(re.compile("[\d]{1,4}").findall(df["질문"][i])[0])
        df['model_answer'][i] = [a // 7, a % 7]
        print(i, df["질문"][i], df["model_answer"][i])

# %%

h = []
for i in range(0, len(df)):
    if df['model_answer'][i] == "":
        h.append(i)
        print(i, df["질문"][i], df["model_answer"][i])

len(h)

# %%

df.to_excel("a4.xlsx", index=False)

# %%


