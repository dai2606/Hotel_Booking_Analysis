# Analyze Hotel Booking Trends and Customer Behavior
## 1. 문제 정의 (Problem Definition)

이 프로젝트의 목표는 호텔 예약 데이터를 분석하여 고객의 예약 패턴과 행동 특성을 파악하는 것이다.

주요 분석 내용:
- 호텔 예약 추세 분석
- 예약 취소율 분석
- 고객 국가별 예약 패턴 분석
- 성수기/비수기 예약 변화 분석
- 고객 행동 기반 인사이트 도출

사용 데이터:
- Hotel Booking Demand Dataset (Kaggle)
- https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?resource=download
- 예약 날짜, 고객 국가, 숙박 기간, 예약 취소 여부 등의 데이터를 사용한다.

원본 데이터 파일의 크기는 약 16MB이므로, 본 프로젝트에서는 호텔 예약 데이터가 여러 날짜에 걸쳐 누적 수집되는 상황을 가정한다. 이를 위해 Python 수집 스크립트를 작성하여 원본 데이터를 여러 개의 일별 batch 파일로 생성한다. 각 batch 파일에는 `collection_date`와 `batch_id` 컬럼을 추가하여 데이터 수집 날짜와 batch 번호를 구분한다.

생성된 batch 데이터의 전체 크기는 100MB 이상이 되도록 구성하며, 이는 프로젝트 요구사항인 누적 100MB 이상의 데이터 확보 조건을 만족하기 위한 것이다.

이 프로젝트는 대용량 데이터를 효율적으로 저장 및 처리하기 위해 클라우드 기반 환경(GCP)과 분산 처리 기술을 활용한다.

## 2. 기술 스택 (Technology Stack)

프로젝트에서 사용할 기술은 다음과 같다.

- Python
    - Kaggle 원본 데이터를 기반으로 일별 batch 데이터 생성
    - `collection_date`와 `batch_id` 컬럼 추가
    - 데이터 수집 과정을 재실행 가능한 스크립트로 구현

- Hadoop HDFS
    - 누적 100MB 이상의 호텔 예약 batch 데이터 저장
    - 분산 파일 시스템 기반의 데이터 저장소로 활용

- Apache Spark
    - 데이터 전처리 및 분석
    - DataFrame 기반 분석 수행
    - 결측치 처리, 타입 변환, 필터링, 집계 작업 수행

Spark는 DataFrame과 Structured API를 통해 대규모 데이터 분석을 지원한다.

- Google Cloud Platform (GCP)
    - 클라우드 기반 Hadoop/Spark 실행 환경
    - HDP Sandbox 실습 환경 실행

- Matplotlib / Plotly
    - 분석 결과 시각화
    - 예약 추세, 취소율, 국가별 예약 패턴 등을 그래프로 표현

GCP는 클라우드 컴퓨팅 및 빅데이터 실습 환경으로 사용된다.

## 3. 구현 계획 (Implementation Plan)

프로젝트의 전체 파이프라인은 다음과 같다.

```text
Hotel Booking Dataset (Kaggle)
        ↓
Python Data Collection Script
        ↓
Daily Batch CSV Files
(collection_date, batch_id 컬럼 추가)
        ↓
HDFS 저장
        ↓
Spark Data Processing
        ↓
데이터 정제 및 전처리
        ↓
예약 패턴 분석
고객 행동 분석
취소율 분석
        ↓
결과 시각화 및 리포트


구현 단계:
  1. Kaggle에서 Hotel Booking Demand Dataset을 다운로드한다.
  2. Python 수집 스크립트를 작성하여 원본 데이터를 여러 개의 일별 batch 파일로 생성한다.
  3. 각 batch 파일에 collection_date와 batch_id 컬럼을 추가한다.
  4. 생성된 batch 데이터를 HDFS에 저장한다.
  5. Spark DataFrame을 이용하여 데이터를 불러오고 결측치 처리, 타입 변환, 필터링 등의 전처리를 수행한다.
  6. 예약 트렌드, 고객 행동, 취소율 분석을 수행한다.
  7. 분석 결과를 시각화하고 최종 리포트를 작성한다.