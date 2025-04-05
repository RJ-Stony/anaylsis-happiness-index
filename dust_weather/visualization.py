"""
미세먼지 데이터와 날씨 데이터의 상관 관계
-> 미세먼지와 초미세먼지 관계?
-> 미세먼지 변수 중 대기 오염과 관련된 변수?
-> 일산화탄소와 이산화질소 관계?
-> 오존과 바람 관계?
-> 기온과 미세먼지 관계?
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('./data/dust_weather.xlsx')
data.info()

def plot_reg_scatter(df, x_col, y_col, title, x_label, y_label):
    plt.figure(figsize=(12, 10), dpi=500)
    sns.regplot(x=x_col, y=y_col, data=df, scatter_kws={'alpha':0.5})
    plt.title(title, fontsize=18, y=1.01)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()
    plt.show()
    
    corr_value = df[[x_col, y_col]].corr().iloc[0, 1]
    print(f"{title} - 상관계수({x_col} vs {y_col}): {corr_value:.3f}")

# --- 1. 미세먼지와 초미세먼지 관계 ---
plot_reg_scatter(data, 'PM10', 'PM2.5',
                 '미세먼지와 초미세먼지의 관계',
                 '미세먼지', '초미세먼지')

'''
미세먼지와 초미세먼지
강한 양의 상관관계 확인
PM10과 PM2.5가 동일한 대기 오염원 및 기상 요인에 의해 함께 증가/감소
'''

# --- 2. 대기오염 관련 변수 간 상관관계 ---
pollution_vars = ['PM10', 'PM2.5', '아황산가스', '일산화탄소', '오존', '이산화질소']
plt.figure(figsize=(10, 8), dpi=500)
corr_matrix = data[pollution_vars].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('대기오염 관련 변수 간 상관관계', y=1.01, fontsize=15)
plt.tight_layout()
plt.show()

'''
일산화탄소, 이산화질소, PM10, PM2.5 간에는 대체로 양의 상관관계가 존재
오존은 다른 오염 물질과 생성 구조가 달라서, 음의 상관관계나 약한 상관성을 보이는 경우가 다수
'''

# --- 3. 일산화탄소와 이산화질소 관계 ---
plot_reg_scatter(data, 'co', 'no2',
                 '일산화탄소와 이산화질소의 관계',
                 '일산화탄소', '이산화질소')

'''
높은 양의 상관계수, 공통 배출원을 강하게 시사.
자동차가 많은 강남구 지역에서 CO와 NO2가 함께 증가하는 패턴
'''

# --- 4. 오존과 바람(풍속) 관계 ---
plot_reg_scatter(data, 'o3', 'wind',
                 '오존과 바람의 관계',
                 '오존', '풍속')
'''
오존 농도와 풍속 그래프에서는 풍속이 증가할수록 오존 농도도 증가하는 경향
복합적인 요인이 작용했을 가능성도 있음
'''

# --- 5. 기온과 미세먼지 관계 ---
plot_reg_scatter(data, 'temp', 'PM10',
                 '기온과 미세먼지의 관계',
                 '기온(°C)', '미세먼지')

'''
비교적 약한 양의 상관관계, 계절별 특성이 크게 작용
겨울철 난방 수요 증가나 여름철 대기 정체 등 다양한 변수도 함께 고려해야 정확한 해석이 가능할 듯
'''
