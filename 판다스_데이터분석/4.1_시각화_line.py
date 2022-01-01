# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 11:00:38 2021

@author: khb16
"""

import os
os.getcwd()
os.chdir("C:/Users/khb16/Desktop/code/DA/판다스_데이터분석")

# 1-1. 선그래프
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("시도별 전출입 인구수.xlsx", engine='openpyxl', header=0)

# NaN값을 바로 앞의 행 데이터값으로 채운다.
df = df.fillna(method = 'ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1,inplace=True)
df_seoul.set_index('전입지',inplace=True) # 행 인덱스로 지정

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# plot
plt.plot(sr_one.index, sr_one.values)

# 판다스 객체를 plot함수에 입력
plt.plot(sr_one)

plt.title('서울 -> 경기 인구 인동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.show()

# 한글 폰트 오류 해결
from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font_name)

# 1-2. 그래프 꾸미기
# 스타일 서식의 종류
print(plt.style.available)

sr_one
plt.style.use('ggplot') # 스타일 서식 지정
plt.figure(figsize=(14,5)) # 그림 사이즈 지정
plt.xticks(size = 10, rotation = 'vertical') # x축 눈금 라벨 회전
plt.plot(sr_one, marker='o',markersize = 10) # 마커 표시 추가
plt.title('서울 -> 경기 인구 인동',size=30)
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구수', size=20)
plt.legend(labels=['서울 -> 경기'], loc='best', fontsize = 15)
#plt.show()


# 주석 표시 - 화살표
plt.ylim(50000,800000) # y축 범위 지정
plt.annotate('',
             xy = (20,620000),   # 화살표 끝점
             xytext = (2,290000),# 화살표 시작점
             xycoords = 'data',  # 좌표체
             arrowprops=dict(arrowstyle='->', color='skyblue',lw=5)
             )

plt.annotate('',
             xy = (47,450000),   
             xytext = (30,580000),
             xycoords = 'data',  
             arrowprops=dict(arrowstyle='->', color='olive',lw=5)
             )

# 주석 표시 - 텍스트
plt.annotate('인구 이동 증가(1970-1995)',
             xy = (10,350000),   
             rotation = 25,
             va = 'baseline',
             ha = 'center',
             fontsize=15
             )

plt.annotate('인구 이동 감소(1995-2017)',
             xy = (40,460000),   
             rotation = -11,
             va = 'baseline',
             ha = 'center',
             fontsize=15
             )

plt.show()


# 화면 분할하여 그래프 여러 개 그리기
# aex 객체

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(sr_one, 'o', markersize=10)
ax2.plot(sr_one, marker = 'o', markerfacecolor='green',markersize=10,
         color='olive',linewidth=2,label='서울 -> 경기')
ax2.legend(loc='best')

ax1.set_ylim(50000,80000)
ax2.set_ylim(50000,80000)

ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)

plt.show()
# 오류


# axe 객체 그래프 꾸미기
fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(1,1,1)

# axe 객체에 plot 함수로 그래프 출력
ax.plot(sr_one, marker='o', markerfacecolor='orange', markersize=10,
        color='olive', linewidth=2, label='서울 -> 경기')
ax.legend(loc='best')

ax.set_ylim(50000,800000)
ax.set_title('서울 -> 경기 인구 이동', size=20)
ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수',size=12)
ax.set_xticklabels(sr_one.index, rotation=75)
ax.tick_params(axis='x', labelsize=10) # 축 눈금 라벨 크기
ax.tick_params(axis='y', labelsize=10)
plt.show()

# 같은 화면에 그래프 추가
col_years = list(map(str,range(1970,2018)))
df_3 = df_seoul.loc[['충청남도','경상북도','강원도'],col_years]

plt.style.use('ggplot')
fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(1,1,1)

ax.plot(col_years, df_3.loc['충청남도',:],marker='o', markerfacecolor='green',
        markersize=10,color='olive',linewidth=2,label='서울 -> 충남')
ax.plot(col_years, df_3.loc['경상북도',:],marker='o', markerfacecolor='blue',
        markersize=10,color='skyblue',linewidth=2,label='서울 -> 경북')
ax.plot(col_years, df_3.loc['강원도',:],marker='o', markerfacecolor='red',
        markersize=10,color='magenta',linewidth=2,label='서울 -> 강원')

ax.legend(loc='best')

ax.set_title('서울 -> 충남, 경북, 강원 인구 이동', size=20)
ax.set_xlabel('기간',size=12)
ax.set_ylabel('이동 인구수', size=12)
ax.set_xticklabels(col_years,rotation=90)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
plt.show()

# 화면 4분할 그래프
col_years = list(map(str,range(1970,2018)))
df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'],col_years]

plt.style.use('ggplot')
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(col_years, df_4.loc['충청남도',:],marker='o', markerfacecolor='green',
        markersize=10,color='olive',linewidth=2,label='서울 -> 충남')
ax2.plot(col_years, df_4.loc['경상북도',:],marker='o', markerfacecolor='blue',
        markersize=10,color='skyblue',linewidth=2,label='서울 -> 경북')
ax3.plot(col_years, df_4.loc['강원도',:],marker='o', markerfacecolor='red',
        markersize=10,color='magenta',linewidth=2,label='서울 -> 강원')
ax4.plot(col_years, df_4.loc['전라남도',:],marker='o', markerfacecolor='orange',
        markersize=10,color='yellow',linewidth=2,label='서울 -> 전남')

ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')

ax1.set_title('서울 -> 충남 인구 이동', size=15)
ax2.set_title('서울 -> 경북 인구 이동', size=15)
ax3.set_title('서울 -> 강원 인구 이동', size=15)
ax4.set_title('서울 -> 전남 인구 이동', size=15)

ax1.set_xticklabels(col_years,rotation=90)
ax2.set_xticklabels(col_years,rotation=90)
ax3.set_xticklabels(col_years,rotation=90)
ax4.set_xticklabels(col_years,rotation=90)

plt.show()

# matplotlib 스타일 리스트 출력
import matplotlib
colors={}
for name, hex in matplotlib.colors.cnames.items():
    colors[name] = hex
print(colors)

