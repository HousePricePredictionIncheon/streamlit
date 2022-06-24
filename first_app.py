import streamlit as st
import pandas as pd
import numpy as np
import time
import xgboost as xgb
import data

# xgb모델 불러오기
xgb_model = xgb.XGBRegressor()
xgb_model.load_model('xgb_load_final2.model')

# 제목
st.title('Incheon house Price')
st.write('Incheon House Price Prediction Project')


# Add a placeholder 진행 상황 바
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

# 변수는 총 11개
# 순서대로 전용면적, 계약년월, 거래금액, 층, 건축년도, 대규모 점포, 근린공원, 반료동물 등록 수, 병원, 학교, station, starbucks
st.write("고려한 변수는 총 11개 입니다.")
st.write("전용면적, 계약년월, 층, 건축년도, 대규모 점포, 근린 공원, 반려동물 등록 수, 병원, 학교, 지하철 역 개수, startbucks 수")
max_wid = 291.335999
max_contract = 202204.0
max_price = 450000
max_floor = 60
max_builyear = 2022
maxs = [291.335999, 202204.0, 60, 2022.0, 6.0, 28.0, 11863, 303, 50, 6, 5]
mins = [11.946, 202104, 1, 1971, 0, 0, 0, 0, 0, 0, 0]

# 지역 변수를 제외한 나머지 변수 설정하는 sidebar

width = st.slider("면적을 선택하세요 단위(m^2)", 11, 291)
#contract = st.slider("계약년월을 선택하세요(년월)", 202104, 202204)
# 6. 날짜 입력
contractdate = st.date_input('계약년월')  # 디폴트로 오늘 날짜가 찍혀 있다.
contractString = contractdate.strftime("%Y%m")
contract = float(contractString)
st.write(contractdate.strftime("%Y%m"))

floor = st.slider("층을 선택하세요", 1, 60)
builtYear = st.slider("건축년도를 선택하세요(년도)", 1971, 2022)


# 지역을 고르는 select box
option = st.sidebar.selectbox(
    '어떤 지역을 고르시겠습니까?',
    ('용현동', '구월동', '송도동', '주안동', "숭의동", "연수동", "부평동", "청라동", "동춘동", "학익동"))

# 지역에 따른 지도 보여주기 및 변수 설정
market = 1
park = 6
pet = 5930
hospital = 118
school = 16
station = 1
starbucks = 1
mapalatlon = [37.4468604, 126.6551088]
if(option == '용현동'):
    maplatlon = [37.4468604, 126.6551088]
    park = 6
    pet = 5930
    hospital = 118
    school = 16
    station = 1
    starbucks = 1
elif(option == '구월동'):
    maplatlon = [37.4385657, 126.6956650]
    market = 3
    park = 19
    pet = 7174
    hospital = 303
    school = 30
    station = 4
    starbucks = 2
elif(option == "송도동"):
    maplatlon = [37.3947, 126.6393]
    market = 6
    park = 0
    pet = 7964
    hospital = 212
    school = 50
    station = 4
    starbucks = 2
elif(option == "부평동"):
    maplatlon = [37.4912, 126.7235]
    market = 3
    park = 9
    pet = 11836
    hospital = 294
    school = 23
    station = 3
    starbucks = 3
elif(option == "주안동"):
    maplatlon = [37.4653, 126.6797]
    market = 4
    park = 10
    pet = 9962
    hospital = 227
    school = 23
    station = 2
    starbucks = 1
elif(option == "동춘동"):
    maplatlon = [37.4032, 126.6694]
    market = 3
    park = 8
    pet = 3331
    hospital = 63
    school = 24
    station = 0
    starbucks = 2
elif(option == "숭의동"):
    maplatlon = [37.4638, 126.6502]
    market = 2
    park = 6
    pet = 3757
    hospital = 32
    school = 6
    station = 0
    starbucks = 0
elif(option == "연수동"):
    maplatlon = [37.4185, 126.6896]
    market = 0
    park = 16
    pet = 3569
    hospital = 67
    school = 20
    station = 5
    starbucks = 0
elif(option == "청라동"):
    maplatlon = [37.5385, 126.6337]
    market = 3
    park = 0
    pet = 5217
    hospital = 50
    school = 32
    station = 0
    starbucks = 2
elif(option == "학익동"):
    maplatlon = [37.4436, 126.6677]
    market = 0
    park = 13
    pet = 2876
    hospital = 47
    school = 20
    station = 0
    starbucks = 1

# 고른 지역 보여주기
st.write('You selected:', option)
st.write("pet:", pet)
map_data = pd.DataFrame(
    np.random.rand(1, 2) / [50, 50] + maplatlon,
    columns=['lat', 'lon'])
st.map(map_data)

# scaling되기 전의 데이터
realData = [[width, contract, floor, builtYear, market,
             park, pet, hospital, school, station, starbucks]]

# minMaxScaler를 통해 scaling해줬었으므로 여기서도 해줘야함 scaling 된 데이터를 저장할 곳
scaleData = []

# scaling
for i in range(0, 11):
    scaleData.append((realData[0][i] - mins[i]) / (maxs[i] - mins[i]))
scaleData = [scaleData]
res1 = xgb_model.predict(scaleData)

# 결과 출력
st.write(res1)
