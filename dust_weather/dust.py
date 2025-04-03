# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:01:55 2025

@author: Roh Jun Seok
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dust = pd.read_excel('./data/dust.xlsx')
dust.shape
dust.info()
dust.isna().sum()

# 데이터 가공
dust.rename(columns={'날짜':'date', '아황산가스':'so2',
                     '일산화탄소':'co', '오존':'o3',
                     '이산화질소':'no2'}, inplace=True)

dust.info()
dust['date'] = dust['date'].str[:11]
dust['date'] = pd.to_datetime(dust['date'])

dust['year'] = dust['date'].dt.year
dust['month'] = dust['date'].dt.month
dust['day'] = dust['date'].dt.day

dust = dust[['date', 'year', 'month', 'day', 'so2', 'co', 'o3', 'no2', 'PM10', 'PM2.5']]
dust.isnull().sum()

dust = dust.fillna(method='pad')
dust.fillna(20, inplace=True)

dust.info()

dust.to_excel('./data/dust_final.xlsx', index=False)
