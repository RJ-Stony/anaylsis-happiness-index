import pandas as pd

weather = pd.read_excel('./data/weather.xlsx')
weather.info()

# 데이터 가공
# 분석에 필요없는 컬럼 제거
weather.drop(['지점', '지점명'], axis=1, inplace=True)
weather.info()

weather.columns = ['date', 'temp', 'wind', 'rain', 'humid']

weather['date'] = pd.to_datetime(weather['date']).dt.date
weather['date'] = weather['date'].astype('datetime64[ns]')

weather.isnull().sum()

weather['rain'].value_counts()
'''
기상청에서는 0.1 단위로 강수량을 측정하고,
0.1 이하로 비가 내리면 0으로 표시
따라서 좀 더 세부적인 값을 측정하기 위해
'''
# 강수량이 0인 값을 0.01로 변환
weather['rain'] = weather['rain'].replace([0], 0.01)
weather['rain'].value_counts()

weather.to_excel('./data/weather_final.xlsx', index=False)
