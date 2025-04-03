import pandas as pd

# 파일 불러오기
health = pd.read_excel("./data/대한민국행복지도_건강.xlsx")
economy = pd.read_excel("./data/대한민국행복지도_경제.xlsx")
relationship = pd.read_excel("./data/대한민국행복지도_관계및사회참여.xlsx")
education = pd.read_excel("./data/대한민국행복지도_교육.xlsx")
satisfaction = pd.read_excel("./data/대한민국행복지도_삶의만족도.xlsx")
safety = pd.read_excel("./data/대한민국행복지도_안전.xlsx")
leisure = pd.read_excel("./data/대한민국행복지도_여가.xlsx")
environment = pd.read_excel("./data/대한민국행복지도_환경.xlsx")

health = health.rename(columns={'평균': '건강평균'})
health = health[['No', '시도', '구군', '건강평균']]

economy = economy.rename(columns={'평균': '경제평균'})
economy = economy[['No', '시도', '구군', '경제평균']]

relationship = relationship.rename(columns={'평균': '관계평균'})
relationship = relationship[['No', '시도', '구군', '관계평균']]

education = education.rename(columns={'평균': '교육평균'})
education = education[['No', '시도', '구군', '교육평균']]

satisfaction = satisfaction.rename(columns={'삶의 만족도': '삶의만족도평균'})
satisfaction = satisfaction[['No', '시도', '구군', '삶의만족도평균']]

safety = safety.rename(columns={'평균': '안전평균'})
safety = safety[['No', '시도', '구군', '안전평균']]

leisure = leisure.rename(columns={'평균': '여가평균'})
leisure = leisure[['No', '시도', '구군', '여가평균']]

environment = environment.rename(columns={'평균': '환경평균'})
environment = environment[['No', '시도', '구군', '환경평균']]

data = health.merge(economy, on=["No", "시도", "구군"], how="outer") \
                    .merge(relationship, on=["No", "시도", "구군"], how="outer") \
                    .merge(education, on=["No", "시도", "구군"], how="outer") \
                    .merge(satisfaction, on=["No", "시도", "구군"], how="outer") \
                    .merge(safety, on=["No", "시도", "구군"], how="outer") \
                    .merge(leisure, on=["No", "시도", "구군"], how="outer") \
                    .merge(environment, on=["No", "시도", "구군"], how="outer")

data.to_excel("./data/happy_index.xlsx", index=False)
