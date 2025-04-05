import pandas as pd

df = pd.read_excel('./data/happy_index.xlsx')
df.info()

index_columns = ['건강평균', '경제평균', '관계평균', '교육평균', '삶의만족도평균', '안전평균', '여가평균', '환경평균']

for col in index_columns:
    df[col] = df.groupby('시도')[col].transform(lambda x: x.fillna(x.mean()))
    
df.info()
df.to_excel('./data/happy_index.xlsx', index=False)
