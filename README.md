# streamlitIncheonHousePricePrediction
## Streamlit 라이브러리를 이용한 인천 집 값 예측 모델 시각화 웹 버전입니다. 
### 10개 정도의 동에 대한 집 값 예측을 제공하려고 하고 있습니다. 
## 인하대학교 인공지능 응용시스템 17조 조별 과제의 마무리

## 사용 모델
- XGBOOST
- MLP

## 예측을 제공하는 동
- 용현동
- 구월동
- 주안동
- 숭의동
- 연수동
- 송도동
- 부평동
- 청라동
- 학익동
- 동춘동

## 실행 방법
1. 우선 레포지토리를 fork받는다. 
2. 터미널에 fork받고 clone받은 레포지토리로 이동한다. 
3. 그 후 다음과 같은 명령어를 터미널에 입력한다.
~~~
streamlit run first_app.py
~~~

### 웹페이지 소개
#### 1. 변수 설명
<img width ="60%" src = "https://user-images.githubusercontent.com/71626430/175750283-44574e0b-c571-45b4-9a3d-fbd84d771ddf.png" />

#### 2. 사이드 바(예측하고 싶은 위치 설정)
<img width = "50%" src = "https://user-images.githubusercontent.com/71626430/175750417-8cdd6e51-8246-499b-aa57-44ccda85a3fc.png" />

#### 3. 옵션( 전용면적, 계약년월, 층, 건축년도)
<img width = "60%" src = "https://user-images.githubusercontent.com/71626430/175750497-fc76e949-1b6c-4c2f-953b-9b0244c0c15f.png" />

#### 4. 지도 (설정한 곳의 위치를 보여줍니다.)
<img width = "60%" src = "https://user-images.githubusercontent.com/71626430/175750454-02f77844-8177-45a0-9bc3-fb69bb36caf7.png" />

#### 5. 결과 
<img width = "80%" src = "https://user-images.githubusercontent.com/71626430/175750585-2caccd35-49f9-4849-b7ce-eb2f04c604a5.png" />
 
