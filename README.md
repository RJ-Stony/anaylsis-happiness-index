# 😊 Happiness Index Analysis

행복은 어디서 오는가?  
공공 데이터를 기반으로 행복지수를 구성하는 다양한 요소들을 통합하고, 시각화하는 프로젝트입니다.

---

## 📁 구성 파일

```
happy_index/
├── merge.py              # 행복지수 관련 데이터 병합
├── preprocessing.py      # 결측치 처리 및 스케일링 등 전처리
├── visualization.py      # 지역별, 지표별 행복지수 시각화
```

---

## 🔍 분석 흐름

1. **데이터 병합**
   - `merge.py`  
     → 복수의 데이터 소스를 하나의 테이블로 통합 (예: 건강, 날씨, 소비, 문화 등)

2. **데이터 전처리**
   - `preprocessing.py`  
     → 결측치 처리, 정규화/표준화, 필터링 등 분석 준비를 위한 클린징 단계

3. **시각화**
   - `visualization.py`  
     → matplotlib, seaborn 등을 활용하여 행복지수 분포 및 상관관계 시각화

---

## 🧠 활용 가능성

- 지역별 행복 격차 확인
- 기후, 소비, 문화 활동 등이 행복지수에 미치는 영향 분석
- 정책 제안용 인사이트 도출

---

## 🛠 사용 기술

- Python 3.12+
- pandas, matplotlib, seaborn
- (데이터 출처에 따라) openpyxl, requests 등

---

## 📌 참고 사항

- 통합되는 데이터셋의 구조나 출처가 바뀔 경우 `merge.py` 조정 필요
- 시각화는 Jupyter Notebook 환경에서 실행 시 더욱 효과적입니다
