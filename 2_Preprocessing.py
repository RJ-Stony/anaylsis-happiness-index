"""
수집 데이터 전처리
danawa_crawling_result.xlsx
"""
import pandas as pd

data = pd.read_excel('./data/danawa_crawling_result.xlsx')
data.info()

# 1. 상품명 데이터를 회사명과 상품명으로 분리
data['상품명'][:10]
title = 'LG전자 코드제로 A9 A978'

## 첫번째 공백까지만 쪼개짐
info = title.split(' ', 1)

companies = []
products = []

for title in data['상품명']:
    info = title.split(' ', 1)
    company = info[0]
    product = info[1]
    
    companies.append(company)
    products.append(product)

# 2. 스펙 목록 데이터를 분석에 필요한 요소만 추출
## 카테고리, 사용 시간, 흡입력, 나는 전압까지

'''
['핸디/스틱청소기', => 카테고리
 '전압: 25.2V',   => 전압
 '흡입력: 140AW', => 흡입력
 '흡입력: 22000Pa', => 흡입력
 '사용시간: 1시간']    => 사용시간
'''

'''
카테고리명이 첫번째 위치,
전압: 00V,
사용시간: 00분 / 00시간,
흡입력: 000pa / 000AW
'''

# 카테고리
data['스펙 목록'][0]
specs = data['스펙 목록'][0].split(' / ')
specs
category = specs[0]

# 전압 / 흡입력 / 사용시간
volt = ''
suction = '' 
use_time = ''

for spec in specs:
    if '전압' in spec:
        volt = spec.split(' ')[1].strip()
    elif '흡입력' in spec:
        suction = spec.split(' ')[1].strip()
    elif '사용시간' in spec:
        use_time = spec.split(' ')[1].strip()

# 이제 전체로
categories = []
volts = []
use_times = []
suctions = []

for spec_list in data['스펙 목록']:
    specs = spec_list.split(' / ')
    
    category = specs[0]
    categories.append(category)
    
    # 전압, 흡입력, 사용시간 추출
    ## 정보가 없는 제품을 위해 초기화 변수 생성
    volt = None       # volt = ''과 다름 -> 값이 있는 상태
    suction = None
    use_time = None
    
    for spec in specs:
        if '전압' in spec:
            volt = spec.split(' ')[1].strip()
        elif '흡입력' in spec:
            suction = spec.split(' ')[1].strip()
        elif '사용시간' in spec:
            use_time = spec.split(' ')[1].strip()
            
    volts.append(volt)
    use_times.append(use_time)
    suctions.append(suction)
    
# 3. 단위 통일시키기
'''
전압
모두 V로 되어있기 때문에 V 앞에 단위만 추출
'''
# 모델별 전압
new_volts = []

for volt in volts:
    try:
        if 'V' in volt:
            value = float(volt.split('V')[0].strip())
        elif 'v' in volt:
            value = float(volt.split('v')[0].strip())
    except:
        value = None
    new_volts.append(value)
    
'''
사용시간
'시간' 단어가 있으면
1. '시간' 앞의 숫자를 추출한 뒤, * 60 -> 분
2. '시간' 뒤에 '분' 글자 앞의 숫자 추출하여 시간에 더하기

'시간' 단어가 없으면
'분' 글자 앞의 숫자를 추출해 시간에 더하기

예외 처리
'''

# 이상치 우선 처리
use_times[227] = '2시간30분'
use_times[227]

# 테스트 코드
times = ['40분', '4분', '1시간', '3시간30분', '4시간']

def convert_time_minute(time):
    try:
        if '시간' in time:
            hour = time.split('시간')[0]
            if '분' in time:
                minute = time.split('시간')[-1].split('분')[0]
            else:
                minute = 0
        else:
            hour = 0
            minute = time.split('분')[0]
        return int(hour) * 60 + int(minute)
    except:
        return None
    
for i in range(len(times)):
    times[i] = convert_time_minute(times[i])
    
# 모델별 사용시간을 분 단위로 통일
new_times = []

for time in use_times:
    value = convert_time_minute(time)
    new_times.append(value)

'''
흡입력
AW: 진공청소기의 전력량 (Airwatt)
W: 모터의 소비전력단위 (Watt)
PA: 흡입력 단위 (Pascal)

(1W == 1AW == 100PA)
'''
# 흡입력 단위 통일 함수
def get_suction(value):
    try:
        value = value.upper()
        if 'AW' in value or 'W' in value:
            result = value.replace('A', '').replace('W', '')
            result = int(result.replace(',', ''))
        elif 'PA' in value:
            result = value.replace('PA', '')
            result = int(int(result.replace(',', '')) / 100)
        else:
            result = None
        return result
    except:
        return None
    
'''
대/소문자를 통일하기 위해 upper()로 대문자 통일 사용
만약 흡입력에 'AW'나 'W'가 있으면
1. 흡입력에서 'A'와 'W' 삭제
2. ','도 삭제 후, 숫자형으로 변환

만약 흡입력에 'PA'가 있으면
1. 흡입력에서 'PA' 삭제
2. ','도 삭제 후, 숫자형으로 바꾸고 Watt 단위 통일을 위해 100으로 나눔

흡입력 값이 비어있거나 단위 변환 시, 문제가 있으면 예외로 처리
'''

# 흡입력 단위 통일
new_suctions = []

for power in suctions:
    value = get_suction(power)
    new_suctions.append(value)
    
# 전처리 결과를 엑셀 파일로 저장
df = pd.DataFrame({
    '카테고리': categories,
    '회사명': companies,
    '제품': products,
    '가격': data['가격'],
    '전압': new_volts,
    '사용시간': new_times,
    '흡입력': new_suctions
})

df['카테고리'].value_counts()

'''
카테고리
핸디/스틱청소기    241
물걸레청소기       39
차량용청소기       13
침구청소기         5
업소용청소기        1
진공청소기         1
'''

# 핸디/스틱청소기만 선택
data_final = df[df['카테고리'].isin(['핸디/스틱청소기'])]

# 가성비
data_final['가격'].unique()

data_final.to_excel('./data/danawa_data_final.xlsx', index=False)
len(data_final)
