1. 문제 정의 (Problem Definition)
이 프로젝트의 목표는 호텔 예약 데이터를 분석하여 고객의 예약 패턴과 행동 특성을 파악하는 것이다.

주요 분석 내용:
- 호텔 예약 추세 분석
- 예약 취소율 분석
- 고객 국가별 예약 패턴 분석
- 성수기/비수기 예약 변화 분석
- 고객 행동 기반 인사이트 도출

사용 데이터:
Hotel Booking Demand Dataset(kaggle)
https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?resource=download
예약 날짜, 고객 국가, 숙박 기간, 예약 취소 여부 등의 데이터를 사용

이 프로젝트는 대용량 데이터를 효율적으로 저장 및 처리하기 위해 클라우드 기반 환경(GCP)과 분산 처리 기술을 활용한다.

2. 기술 스택 (Technology Stack)
프로젝트에서 사용할 기술은 다음과 같다.
- Hadoop HDFS
    - 대용량 호텔 예약 데이터 저장
- Apache Spark
    - 데이터 전처리 및 분석
    - DataFrame 기반 분석 수행

Spark는 DataFrame과 Structured API를 통해 대규모 데이터 분석을 지원한다.
- Spark Streaming
    - 실시간 예약 데이터 처리
    - Kafka와 연동 가능한 스트리밍 분석

Spark Streaming은 Kafka 등의 실시간 데이터 스트림 처리를 지원한다.
- Kafka
    - 실시간 데이터 수집 파이프라인 구성
- Google Cloud Platform (GCP)
    - 클라우드 기반 Hadoop/Spark 실행 환경
GCP는 클라우드 컴퓨팅 및 빅데이터 실습 환경으로 사용된다.

3. 구현 계획 (Implementation Plan)
프로젝트의 전체 파이프라인은 다음과 같다.
Hotel Booking Dataset
        ↓
   Kafka / CSV Data
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
    1. 호텔 예약 데이터 수집
    2. HDFS에 데이터 저장
    3. Spark를 이용한 데이터 전처리
    4. 예약 트렌드 및 고객 행동 분석
    5. 결과 시각화 및 리포트 작성