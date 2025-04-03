# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:34:35 2025

@author: Roh Jun Seok

미세먼지 데이터와 날씨 데이터의 상관 관계
-> 미세먼지와 초미세먼지 관계?
-> 미세먼지 변수 중 대기 오염과 관련된 변수?
-> 일산화탄소와 이산화질소 관계?
-> 오존과 바람 관계?
-> 기온과 미세먼지 관계?

=> 시각화 및 결론
"""
import pandas as pd

dust = pd.read_excel('./data/dust.xlsx')
weather = pd.read_excel('./data/weather.xlsx')
dust['날짜'][0]
weather['일시'][0]

dust[['날짜', '시간']] = dust['날짜'].str.split(' ', expand=True)
dust['날짜'] = pd.to_datetime(dust['날짜'])

def adjust_date_hour(row):
    hour = row['시간']
    date = row['날짜']
    if hour == '24':
        new_date = date + pd.Timedelta(days=1)
        new_hour = '00'
    else:
        new_date = date
        new_hour = hour.zfill(2)
    return pd.Series([new_date, new_hour])

dust[['날짜', '시간']] = dust.apply(adjust_date_hour, axis=1)

dust['날짜'] = dust['날짜'].dt.strftime('%Y-%m-%d')

weather['날짜'] = weather['일시'].dt.strftime('%Y-%m-%d')
weather['시간'] = weather['일시'].dt.strftime('%H')

data = pd.merge(dust, weather, on=['날짜', '시간'], how='inner')

data['연도'] = pd.to_datetime(data['날짜']).dt.year
data['월'] = pd.to_datetime(data['날짜']).dt.month
data['일'] = pd.to_datetime(data['날짜']).dt.day

data = data.drop(['일시', '날짜'], axis=1)

new_order = ['연도', '월', '일', '시간'] + [col for col in data.columns if col not in ['연도', '월', '일', '시간']]
data = data[new_order]

data.dropna(inplace=True)
data.info()

data.to_excel('./data/data_final.xlsx', index=False)
