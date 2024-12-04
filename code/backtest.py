import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


kospi = pd.read_csv('kospi_data.csv')

score_df = pd.read_csv('score_adj.csv')

#외국인 데이터 기준으로 날짜 맞추기
date = score_df['Date'].tolist()

kospi = kospi[kospi['Date'].isin(date)].reset_index(drop=True)

#리밸런싱 시그널 함수
def signal(date_index):
    score_spread = score_df['Spread']
    score = score_df['kor']
    f_score = score_df['foreign']

    #외국인과 한국 시장 스프레드가 10를 넘어갈 때
    if (score_spread[date_index] > 0) and score[date_index] < 50:
        rebalance_signal = 1

    elif (score_spread[date_index] < 0) and score[date_index] > 50:
        rebalance_signal = -1

    elif (f_score[date_index] > 80) and score[date_index] > 80:
        rebalance_signal = -1

    elif (f_score[date_index] < 20) and score[date_index] < 20:
        rebalance_signal = 1

    else:
        rebalance_signal = 0

    return rebalance_signal


# kospi 종가 불러오기
def portfolio_price(date_index):
    kospi_close = kospi['Close']

    return float(kospi_close[date_index])


#backtest
n = 0
#시작 자산 = 1억(6000만원 주식, 4000만원 무위험 자산)
currency = []
start_currency = 40000000
#주식 가치
stock_value = []
#시작 주식 가치
start_value = 60000000
#리밸런싱 날짜
long_rebalanced_date = []
short_rebalanced_date = []
#포트폴리오 가치
portfolio_value = []
#비교지수(long_only)
long_only = []

#오늘 시그널, 마지막 시그널
latest_signal = 0
current_signal = 0

#시작 주식 개수 계산
start_price = portfolio_price(0)
current_long = math.floor(start_value / start_price)
current_currency =start_currency

#비교지수 주식 개수
long_only_stocks = current_long
#비교지수 현금
long_only_currency = start_currency

for i in date:
    #추가되는 순현금
    added_currency = 0
    #당일 주식 종가 계산
    current_stock_price = portfolio_price(n)
    #당일 현금 가치 계산
    current_currency = current_currency * ( (1 + 0.04) ** (1 / 252))
    #당일 포트폴리오 가치 계산
    current_portfolio_value = current_stock_price*current_long + current_currency

    #오늘 리밸런싱 해야되는지 확인 후 주식 개수 변화
    if (latest_signal == 0 or latest_signal == -1) and current_signal == 1:
        #주식:현금 비중 8:2로 조정
        added_currency = (current_long - math.floor( current_portfolio_value*0.8 / current_stock_price )) * current_stock_price
        current_long = math.floor( current_portfolio_value*0.8 / current_stock_price )
        long_rebalanced_date.append(i)
        #현재 시그널 표시
        latest_signal = 1

    elif (latest_signal == 0 or latest_signal == 1) and current_signal == -1:
        #주식:현금 비중 2:8로 조정
        added_currency = (current_long - math.floor( current_portfolio_value*0.2 / current_stock_price )) * current_stock_price
        current_long = math.floor( current_portfolio_value*0.2 / current_stock_price ) 
        short_rebalanced_date.append(i) 
        #현재 시그널 표시
        latest_signal = -1

    #당일 현금 가치 재계산
    current_currency = current_currency + added_currency  

    #리밸런싱된 가치 재계산
    current_portfolio_value = current_stock_price*current_long + current_currency        

    #계산된 값들 기록
    currency.append(current_currency)
    stock_value.append(current_stock_price*current_long)
    portfolio_value.append(current_portfolio_value)
    
    
######################비교지수 가치 계산######################
    #당일 현금 가치 계산
    long_only_currency = long_only_currency * ( (1 + 0.04) ** (1 / 252))   

    #당일 주식 가치 계산
    long_only_stocks*current_stock_price
    long_only.append(long_only_stocks*current_stock_price + long_only_currency)
#############################################################

    #리밸런싱 시그널 확인
    
    current_signal = signal(n)
    
    n = n + 1

    print(i)


# DataFrame 생성
data = pd.DataFrame({
    'Date': date,
    'Total_Value': portfolio_value, 
    'Spread':score_df['Spread'],
    'Index':long_only
})

# CSV 파일로 저장
data.to_csv('backtest.csv', index=False)

# DataFrame 생성
data = pd.DataFrame({
    'long': long_rebalanced_date
})

# CSV 파일로 저장
data.to_csv('long_rebalanced_date.csv', index=False)

# DataFrame 생성
data = pd.DataFrame({
    'short':short_rebalanced_date
})

# CSV 파일로 저장
data.to_csv('short_rebalanced_date.csv', index=False)



    