# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:01:15 2025

@author: Roh Jun Seok
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('./data/dust_weather.xlsx')
corr = df.corr()

corr['PM10'].sort_values(ascending=False)

# 히스토그램으로 시각화
df[['so2', 'co', 'o3', 'no2', 'PM10', 'PM2.5', 'temp', 'wind', 'humid']].hist(bins=50, figsize=(20, 15))
plt.show()

# 막대 그래프로 시각화: 일별 미세먼지 평균현황
plt.figure(figsize=(15, 10))
sns.barplot(x='day', y='PM10', data=df, palette='Set1')
plt.xticks(rotation=0)
plt.show()

plt.figure(figsize=(15, 12))
sns.heatmap(data=corr, annot=True, fmt='.2f', cmap='hot')
plt.show()