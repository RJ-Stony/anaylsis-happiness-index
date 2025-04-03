# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:48:31 2025

@author: Roh Jun Seok

시도별 행복 지수 요소별 시각화 : 선 그래프

행복 지수 요소별 각각 시각화 : 막대 그래프 (서브플롯 반드시 사용)
삶의 만족도, 건강, 안전, 환경, 경제...

행복 지수 요소간의 상관관계 시각화 : 히트맵
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="whitegrid", palette='pastel')

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

df = pd.read_excel("./data/happy_index.xlsx")
df.rename(columns={'건강평균':'건강', '경제평균':'경제', '관계평균':'관계',
           '교육평균':'교육', '삶의만족도평균':'삶의 만족도',
           '안전평균':'안전', '여가평균':'여가', '환경평균':'환경'}, inplace=True)

index_columns = ['건강', '경제', '관계', '교육', '삶의 만족도', '안전', '여가', '환경']

# =============================================================================
# 1. 시도별 행복 지수 요소별 시각화 : 선 그래프
# =============================================================================
df_by_city = df.groupby('시도')[index_columns].mean().reset_index()

plt.figure(figsize=(12, 6))
for col in index_columns:
    plt.plot(df_by_city['시도'], df_by_city[col], marker='o', label=col)
plt.xlabel('시도')
plt.ylabel('각 지수 평균')
plt.title("시도별 행복 지수 요소별 선 그래프")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

'''
1. 시도별 행복 지수 요소별 선 그래프
전반적으로 시도마다 지수 값이 고르게 분포하기보다는 특정 요소에서 상대적으로 높거나 낮은 값을 보이는 경우가 많았습니다.
예를 들어 어떤 시도는 건강 지수가 높지만, 안전 지수가 낮은 양상을 보이는 등 ‘고르게 높은’ 시도보다 특정 요소가 두드러지게 높은(혹은 낮은) 시도가 존재합니다.
이는 지역별 특성(예: 도시 환경, 산업 구조, 교육 환경, 복지 정책 등)에 따라 개별 지표가 편차를 보일 가능성이 높음을 시사합니다.
'''

# =============================================================================
# 2. 행복 지수 요소별 각각 시각화 : 막대 그래프 (서브플롯)
# =============================================================================
n_cols = 2 
n_rows = (len(index_columns) + 1) // n_cols

fig, axes = plt.subplots(n_rows, n_cols, figsize=(14, n_rows * 4))
axes = axes.flatten()

for i, col in enumerate(index_columns):
    ax = axes[i]
    sorted_data = df_by_city.sort_values(by=col, ascending=True)
    sns.barplot(x='시도', y=col, data=sorted_data, ax=ax, palette='Blues')
    ax.set_title(col)
    ax.set_xlabel("시도")
    ax.set_ylabel("평균 지수")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    
if len(index_columns) < len(axes):
    for j in range(len(index_columns), len(axes)):
        fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

'''
2. 행복 지수 요소별 각각 시각화(막대 그래프)
요소별로 각 시도를 내림차순(또는 오름차순)으로 정렬했을 때, 어떤 시도가 건강에서 1위를 차지하지만 경제에서는 중하위권에 속하는 등, 요소마다 순위가 크게 달라지는 모습이 확인됩니다.
일부 시도는 여러 요소에서 상위권을 유지하거나 하위권을 유지하는 등 상대적으로 전반적인 생활 만족도가 높거나 낮은 양상을 보이기도 합니다.
정책적으로는 어떤 시도가 ‘어느 지표에서 부족한지’를 파악하여, 해당 분야에 특화된 개선책을 마련할 필요가 있음을 시사합니다.
'''

# =============================================================================
# 3. 행복 지수 요소간의 상관관계 시각화 : 히트맵
# =============================================================================
corr_matrix = df[index_columns].corr()

mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, mask=mask, annot=True, cmap="coolwarm", fmt=".2f", 
            square=True, linewidths=.5, cbar_kws={"shrink": .8})
plt.title("행복 지수 요소간 상관관계")
plt.tight_layout()
plt.show()

'''
3. 행복 지수 요소간 상관관계(히트맵)
전반적으로 상관관계가 높지 않은 지표도 있지만, 눈에 띄게 음(-)의 상관을 보이는 경우가 있습니다(예: 삶의 만족도와 안전 지수 간의 음의 상관이 두드러진다면, 안전 지표가 높은 시도일수록 삶의 만족도 지표가 낮게 나타날 가능성이 있음을 의미).
반대로 여가 지수와 환경 지수 등은 양(+)의 상관을 보이는 편이어서, 자연환경이 우수하거나 여가 시설이 잘 갖춰진 곳일수록 여가 지수가 높게 나타날 가능성이 있습니다.
각 요소 간 상관관계는 인과관계를 직접적으로 의미하지 않지만, 여러 지표 간의 ‘함께 변하는’ 경향을 파악해볼 수 있는 지표로써 의미가 있습니다.
'''