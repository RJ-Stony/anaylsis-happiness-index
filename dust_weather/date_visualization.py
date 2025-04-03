import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
data = pd.read_excel('./data/dust_weather.xlsx')

# 1. datetime 컬럼 생성
data['datetime'] = pd.to_datetime(
    data[['year', 'month', 'day']]
)

# 1. 시간별(원본 데이터) 시계열 그래프 (색상 변경)
plt.figure(figsize=(14, 7))
plt.plot(data['datetime'], data['PM10'], color='cornflowerblue', label='미세먼지', alpha=0.8)
plt.plot(data['datetime'], data['PM2.5'], color='lightcoral', label='초미세먼지', alpha=0.8)
plt.xlabel('시간')
plt.ylabel('농도')
plt.title('시간별 미세먼지 및 초미세먼지 농도 변화')
plt.legend()
plt.tight_layout()
plt.show()
