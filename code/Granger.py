import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pymoo.optimize import minimize
from sklearn.preprocessing import RobustScaler, MinMaxScaler
from statsmodels.tsa.stattools import grangercausalitytests
import matplotlib.dates as mdates
import seaborn as sns
from statsmodels.tsa.stattools import adfuller, kpss

# 함수 형성
def adf_test(timeseries, regression_option = 'ct'):
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC', regression = regression_option)
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
       dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)
    
#출처: https://signature95.tistory.com/22 [DataAnalyst:티스토리]

def kpss_test(timeseries, regression_option = 'ct'):
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression= regression_option)
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print (kpss_output)
    
#출처: https://signature95.tistory.com/22 [DataAnalyst:티스토리]


x1 = pd.read_csv('foreign_data.csv')
x2 = pd.read_csv('momentum_data.csv')
x3 = pd.read_csv('stock_intensity_data.csv')
x4 = pd.read_csv('msi_data.csv', dtype={'MSI':'float64'})
x5 = pd.read_csv('option_data.csv')
x6 = pd.read_csv('vkospi_data.csv')
x7 = pd.read_csv('low_risk_asset_data.csv')
x8 = pd.read_csv('junkbond_data.csv')
x9 = pd.read_csv('kor_us_bond_data.csv')
x10 = pd.read_csv('dollar_data.csv')

#외국인 데이터 기준으로 날짜 맞추기
date = x1['Date'].tolist()

x2 = x2[x2['Date'].isin(date)].reset_index(drop=True)
x3 = x3[x3['Date'].isin(date)].reset_index(drop=True)
x4 = x4[x4['Date'].isin(date)].reset_index(drop=True)
x5 = x5[x5['Date'].isin(date)].reset_index(drop=True)
x6 = x6[x6['Date'].isin(date)].reset_index(drop=True)
x7 = x7[x7['Date'].isin(date)].reset_index(drop=True)
x8 = x8[x8['Date'].isin(date)].reset_index(drop=True)
x9 = x9[x9['Date'].isin(date)].reset_index(drop=True)
x10 = x10[x10['Date'].isin(date)].reset_index(drop=True)

#정크본드 데이터 기준으로 날짜 맞추기
date = x8['Date'].tolist()

x1 = x1[x1['Date'].isin(date)].reset_index(drop=True)
x2 = x2[x2['Date'].isin(date)].reset_index(drop=True)
x3 = x3[x3['Date'].isin(date)].reset_index(drop=True)
x4 = x4[x4['Date'].isin(date)].reset_index(drop=True)
x5 = x5[x5['Date'].isin(date)].reset_index(drop=True)
x6 = x6[x6['Date'].isin(date)].reset_index(drop=True)
x7 = x7[x7['Date'].isin(date)].reset_index(drop=True)
x9 = x9[x9['Date'].isin(date)].reset_index(drop=True)
x10 = x10[x10['Date'].isin(date)].reset_index(drop=True)

#국채 데이터 기준 날짜 맞추기
date = x9['Date'].tolist()

x1 = x1[x1['Date'].isin(date)].reset_index(drop=True)
x2 = x2[x2['Date'].isin(date)].reset_index(drop=True)
x3 = x3[x3['Date'].isin(date)].reset_index(drop=True)
x4 = x4[x4['Date'].isin(date)].reset_index(drop=True)
x5 = x5[x5['Date'].isin(date)].reset_index(drop=True)
x6 = x6[x6['Date'].isin(date)].reset_index(drop=True)
x7 = x7[x7['Date'].isin(date)].reset_index(drop=True)
x8 = x8[x8['Date'].isin(date)].reset_index(drop=True)
x10 = x10[x10['Date'].isin(date)].reset_index(drop=True)

#robust, min-max scaling 처리 후에 'score' 열에 점수 추가
robust_scaler = RobustScaler()
min_max_scaler = MinMaxScaler()

# 각 목표값에 로버스트 스케일링 처리
x1['x_robust_scaled'] = robust_scaler.fit_transform(x1[['Spread']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x1['Score'] = min_max_scaler.fit_transform(x1[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x1 = x1.drop(columns=['x_robust_scaled'])

# 각 목표값에 로버스트 스케일링 처리
x2['x_robust_scaled'] = robust_scaler.fit_transform(x2[['Spread']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x2['Score'] = min_max_scaler.fit_transform(x2[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x2 = x2.drop(columns=['x_robust_scaled'])

# 각 목표값에 로버스트 스케일링 처리
x3['x_robust_scaled'] = robust_scaler.fit_transform(x3[['Intensity']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x3['Score'] = min_max_scaler.fit_transform(x3[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x3 = x3.drop(columns=['x_robust_scaled'])

# 각 목표값에 로버스트 스케일링 처리
x4['x_robust_scaled'] = robust_scaler.fit_transform(x4[['MSI']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x4['Score'] = min_max_scaler.fit_transform(x4[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x4 = x4.drop(columns=['x_robust_scaled'])

# 각 목표값에 로버스트 스케일링 처리
x5['x_robust_scaled'] = robust_scaler.fit_transform(-x5[['PutCallRatio']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x5['Score'] = min_max_scaler.fit_transform(x5[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x5 = x5.drop(columns=['x_robust_scaled'])

# 각 목표값에 로버스트 스케일링 처리
x6['x_robust_scaled'] = robust_scaler.fit_transform(-x6[['Spread']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x6['Score'] = min_max_scaler.fit_transform(x6[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x6 = x6.drop(columns=['x_robust_scaled'])

# 각 목표값에 로버스트 스케일링 처리
x7['x_robust_scaled'] = robust_scaler.fit_transform(x7[['Return_Difference']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x7['Score'] = min_max_scaler.fit_transform(x7[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x7 = x7.drop(columns=['x_robust_scaled'])

# 각 목표값에 로버스트 스케일링 처리
x8['x_robust_scaled'] = robust_scaler.fit_transform(x8[['Spread']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x8['Score'] = min_max_scaler.fit_transform(x8[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x8 = x8.drop(columns=['x_robust_scaled'])

# 각 목표값에 로버스트 스케일링 처리
x9['x_robust_scaled'] = robust_scaler.fit_transform(-x9[['Spread']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x9['Score'] = min_max_scaler.fit_transform(x9[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x9 = x9.drop(columns=['x_robust_scaled'])

# 각 목표값에 로버스트 스케일링 처리
x10['x_robust_scaled'] = robust_scaler.fit_transform(-x10[['Spread']])

# 로버스트 스케일링 결과에 대해 Min-Max 스케일링 처리
x10['Score'] = min_max_scaler.fit_transform(x10[['x_robust_scaled']])

# 불필요한 중간 열 삭제 (선택 사항)
x10 = x10.drop(columns=['x_robust_scaled'])

x1_score = x1['Score'].tolist()
x2_score = x2['Score'].tolist()
x3_score = x3['Score'].tolist()
x4_score = x4['Score'].tolist()
x5_score = x5['Score'].tolist()
x6_score = x6['Score'].tolist()
x7_score = x7['Score'].tolist()
x8_score = x8['Score'].tolist()
x9_score = x9['Score'].tolist()
x10_score = x10['Score'].tolist()


fear_greed_score = [100*(a + b + c + d + e + f + g)/7 for a, b, c, d, e, f, g in zip(x2_score, x3_score, x4_score, x5_score, x6_score, x7_score, x8_score)]

foreign_score = [100*(a + b + c)/3 for a, b, c in zip(x1_score, x9_score, x10_score)]

#adf test
adf_test(fear_greed_score)

adf_test(foreign_score)

#kpss test
kpss_test(fear_greed_score)

kpss_test(foreign_score)


#외국인 지표, 한국 지표 csv로 저장
score_df = pd.DataFrame({'Date':date, 'kor':fear_greed_score, 'foreign':foreign_score})

score_df.to_csv('score.csv', index = False)

#동일 비중으로 x2~x8까지의 점수 생성
df = pd.DataFrame({'Foreign_Index':foreign_score, 'Fear&Greed_Score':fear_greed_score})

# Granger 인과관계 분석
lag = 5 # 최대 래그(Lag) 수 설정
test_result = grangercausalitytests(df, maxlag=lag, verbose=True)

#공분산 분석
score_list = [x1_score, x2_score, x3_score, x4_score, x5_score, x6_score, x7_score, x8_score, x9_score, x10_score]
# 리스트를 데이터프레임으로 변환
cov_df = pd.DataFrame(score_list).T
cov_df.columns = [f"x{i+1}" for i in range(len(score_list))]

# 공분산 행렬 계산
cov_matrix = cov_df.cov()

#상관관계 분석
corr = cov_df.corr(method = 'pearson')

# 분석 결과 확인
print("\nGranger Causality Test Results:")
for lag, values in test_result.items():
    print(f"Lag {lag}:")
    print(f"  F-statistic: {values[0]['ssr_ftest'][0]}")
    print(f"  p-value: {values[0]['ssr_ftest'][1]}")

# 문자열 날짜를 datetime 형식으로 변환
date = pd.to_datetime(date)

#히트맵
# 레이블의 폰트 사이즈를 조정

test_heatmap = sns.heatmap(corr.values, # 데이터
                          cbar = True, # 오른쪽 컬러 막대 출력 여부
                           annot = True, # 차트에 숫자를 보여줄 것인지 여부
                           fmt = '.2f', # 숫자의 출력 소수점자리 개수 조절
                           square = 'True', # 차트를 정사각형으로 할 것인지
                          yticklabels=cov_df.columns, # y축에 컬럼명 출력
                          xticklabels=cov_df.columns) # x축에 컬럼명 출력
plt.tight_layout()
plt.show()

#동일 비중 값 시각화
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.plot(date, fear_greed_score,color = 'black', linewidth = 1, label='Fear&Greed Score')  # 선 그래프
plt.plot(date, foreign_score, color='red', linewidth = 1, label='Foreign Index', alpha = 0.7)  # 선 그래프

#날짜 표시 조정
#plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=100))
#plt.xticks(rotation=30)
# x축 포맷팅: 대표값만 몇 개 출력
plt.gca().xaxis.set_major_locator(mdates.YearLocator())  # 매년 대표값 출력
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # 주요 틱 라벨 포맷

plt.title('Korea vs Foreign', fontsize=16)  # 그래프 제목
plt.xlabel('Date', fontsize=14)  # x축 레이블
plt.legend(fontsize=12)  # 범례 표시
plt.show()  # 그래프 출력



