# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:34:37 2025

@author: tuesv

전처리 끝난 데이터 시각화 및 분석
danawa_data_final.xlsx
"""

# 무선청소기 모델별 비교 분석
import pandas as pd
df = pd.read_excel('./data/danawa_data_final.xlsx')

# 흡입력 기준 정렬: 평균
price_mean = df['가격'].mean()
volt_mean = df['전압'].mean()
suction_mean = df['흡입력'].mean()
time_mean = df['사용시간'].mean()

# 가성비 좋은 제품 탐색
condition_data = df[(df['가격'] <= price_mean) &
                    (df['흡입력'] >= suction_mean) &
                    (df['사용시간'] >= time_mean)]

condition_data.info()

# 데이터 시각화
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 테마 설정 및 색상 팔레트 변경
sns.set_theme(style="whitegrid", palette='pastel')

## 한글 표기
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    print('Check your OS system')
    
## 결측값 없애기
chart_data = df.dropna()
chart_data.info()

## 흡입력, 사용 시간 최대, 최소
suction_max = chart_data['흡입력'].max()
suction_mean = chart_data['흡입력'].mean()

time_max = chart_data['사용시간'].max()
time_mean = chart_data['사용시간'].mean()

plt.figure(figsize=(20, 10))
plt.title('무선 핸디/스틱청소기 성능 비교', fontsize=20, fontweight='bold')

# 산점도: 회사명별 색상, 가격에 따른 크기
sns.scatterplot(data=chart_data, x='흡입력', y='사용시간', size='가격', 
                hue='회사명', sizes=(10, 1000), palette='Set3', legend=False)

# 평균값 기준 선 추가 (더 부드러운 색상 지정)
plt.plot([0, suction_max], [time_mean, time_mean], color='darkred', linestyle='--', lw=1)
plt.plot([suction_mean, suction_mean], [0, time_max], color='darkblue', linestyle='--', lw=1)

plt.show()


# Top 20
chart_data_selected = chart_data[:20]

suction_max = chart_data_selected['흡입력'].max()
suction_mean = chart_data_selected['흡입력'].mean()

time_max = chart_data_selected['사용시간'].max()
time_mean = chart_data_selected['사용시간'].mean()

plt.figure(figsize=(20, 10))
plt.title('무선 핸디/스틱청소기 TOP 20', fontweight='bold', fontsize=22)

ax = sns.scatterplot(data=chart_data_selected,
                     x='흡입력',
                     y='사용시간',
                     size='가격',
                     hue='회사명',
                     palette='Set3',
                     sizes=(100, 2000),
                     alpha=0.85,
                     edgecolor='k',
                     legend=False)

# 평균선 추가 (더 세련된 스타일로)
plt.axhline(time_mean, color='lightcoral', linestyle='--', lw=1.5, label=f'사용시간 평균 ({time_mean:.1f})')
plt.axvline(suction_mean, color='cornflowerblue', linestyle='--', lw=1.5, label=f'흡입력 평균 ({suction_mean:.1f})')

# 각 제품 이름을 약간의 오프셋과 함께 표시하여 겹침 방지
for idx, row in chart_data_selected.iterrows():
    x = row['흡입력']
    y = row['사용시간']
    # 제품명에서 첫 단어만 추출하여 라벨로 사용
    label = row['회사명']
    plt.text(x + 0.5, y + 0.5, label, fontsize=20, fontweight='bold', color='black')

plt.xlabel('흡입력', fontsize=18)
plt.ylabel('사용시간', fontsize=18)
plt.tight_layout()
plt.show()