import streamlit as st
import pandas as pd
import numpy as np
import time
import openpyxl
import xgboost as xgb
import torch
# wb = openpyxl.load_workbook("AllData.xlsx", read_only=False, data_only=False)
# ws = wb['Sheet1']
# filename = 'AllData.xlsx'
#xgb_model = joblib.load('xgbIncheonBest_model.pkl')
# xgb모델 불러오기
xgb_model = xgb.XGBRegressor()
xgb_model.load_model('xgb_load_final2.model')
#incheondf = pd.read_excel(filename, engine='openpyxl')


st.title('Incheon house Price')
st.write('Incheon House Price Prediction Project')
# st.write(incheondf.head())

# st.write(xgb_model.predict(input2))

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

# 변수는 총 11개
# 순서대로 전용면적, 계약년월, 거래금액, 층, 건축년도, 대규모 점포, 근린공원, 반료동물 등록 수, 병원, 학교, station, starbucks
max_wid = 291.335999
max_contract = 202204.0
max_price = 450000
max_floor = 60
max_builyear = 2022
maxs = [291.335999, 202204.0, 60, 2022.0, 6.0, 28.0, 11863, 303, 50, 6, 5]
mins = [11.946, 202104, 1, 1971, 0, 0, 0, 0, 0, 0, 0]
option = st.sidebar.selectbox(
    '어떤 지역을 고르시겠습니까?',
    ('구월동', '용현동', '학익동', '문학동'))
inputData = []
with st.sidebar:
    add_radio = st.radio(
        "choose a parameter",
        ("전용면적", "계약년월", "층", "건축년도")
    )
width = st.slider("면적을 선택하세요 단위(m^2)", 11, 291)
contract = st.slider("계약년월을 선택하세요(년월)", 202104, 202204)
floor = st.slider("층을 선택하세요", 1, 60)
builtYear = st.slider("건축년도를 선택하세요(년월)", 1971, 2022)
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
    market = 1
    park = 6
    pet = 5930
    hospital = 118
    school = 16
    station = 1
    starbucks = 1

elif(option == '구월동'):
    maplatlon = [37.4385657, 126.6956650]
st.write('You selected:', option)
map_data = pd.DataFrame(
    np.random.rand(1, 2) / [50, 50] + maplatlon,
    #[50, 50] + maplatlon,
    columns=['lat', 'lon'])

st.map(map_data)
scaleData = []
# 예측 과정
realData = [[width, contract, floor, builtYear, market,
             park, pet, hospital, school, station, starbucks]]
input2 = [[114.860001, 202105, 4, 2001, 0, 0, 1245, 21, 15, 0, 1]]
# scaling
for i in range(0, 11):
    scaleData.append((realData[0][i] - mins[i]) / (maxs[i] - mins[i]))
scaleData = [scaleData]
res1 = xgb_model.predict(scaleData)
st.write(res1)
