# Formulation of the Korean Fear Index Reflecting Foreign Investment : Validation Using Market Timing Strategies

## 0. Special Thanks
This study was inspired by research conducted based on _'EMP 전략'_ by Hanhwa Investment and Securities.

## I. Research Background and Objective

### 1.1 Background
**1.1.1 Limitaitons of VKOSPI**

The VKOSPI, introduced by KRX in 2009, serves currently as Korea's fear index measuring the implied volatility of KOSPI200 options.
Limitations of VKOSPI:
  - Does not fully reflect the market fear and shows unstable correlations with the market.
  - Low liquidity in KOSPI200 options and weak correlation with global indices like VIX (US) and VSTOXX (Europe).

**1.1.2 Foreign Investment in the Korean Financial Market**

High foreign investor proportion in KOSPI (33%) and KOSDAQ (10%) markets
The recent underperformance of KOSPI, centered around Samsung Electronics' stock price, has highlighted the selling trends of foreign investors and the medium-to-long-term risks associated with Samsung Electronics.
  
  <img width="427" alt="image" src="https://github.com/user-attachments/assets/2485dc16-c861-450d-b88c-76fb9ee3d605">
  

When assessing fear in the Korean market alone, there is a possibility that the index may lag behind the impact of foreign investors.
This underscores the need for an index that reflects :
  1. Korean market characteristics.
  2. Foreign investors' influence on the Korean market.

### 1.2 Objective
- Development of a Korea-specific Fear Index Reflecting the Characteristics of the Korean Market
- Development of a Foreign Fear Index Considering the Trends of Foreign Investors in the Korean Market
- If foreign investors' fear precedes fear in the Korean market, validate the effectiveness of a market timing strategy leveraging this time gap.

## II. Korean Fear Index

### 2.1 CNN Fear & Greed Index
The CNN Business Fear & Greed Index quantifies investor sentiment, measuring the level of fear and greed present in the stock market. It ranges from 0 to 100, where 0 represents extreme fear and 100 represents extreme greed. The index is calculated as an equally weighted arithmetic average of daily values from seven technical indicators, each ranging between 0 and 100.

<img width="404" alt="image" src="https://github.com/user-attachments/assets/c3efd7fe-258c-4cdf-a735-b8d3ce8e575d">

<img width="437" alt="image" src="https://github.com/user-attachments/assets/c4e4ee30-4cb6-446b-a721-f63cfa248a2b">

The seven technical indicators of the CNN Fear & Greed Index were reconstructed to suit the Korean market, forming the foundation for developing a Korea-specific Fear Index.

### 2.2 Variable Declaration
- Adaptation of CNN's 7 indicators for the Korean market:
  1. Market Momentum: KOSPI price relative to its 125-day moving average.
  2. Stock Strength: Ratio of 52-week high vs. low stocks in KOSPI.
  3. Stock Breadth: McClellan Summation Index (MSI) for KOSPI.
  4. Put/Call Option Ratio: Ratio of KOSPI200 options.
  5. Market Volatility: VKOSPI.
  6. Safe Haven Demand: Spread between 10-year treasury yields and KOSPI returns.
  7. Junk Bond Demand: Spread between high-yield and low-risk corporate bonds.

  ![image](https://github.com/user-attachments/assets/0e36b797-40f7-482b-aefd-3fbddc29888b)


### 2.3 Data
- Historical data from August 6, 2013, to November 8, 2024.
- Preprocessing methods:
  - Robust Scaling: Minimize outlier impact.
  - MinMax Scaling: Normalize variables between 0 and 1.
  - Adjusted arithmetic averaging to combine variables.


  <img width="418" alt="image" src="https://github.com/user-attachments/assets/70ae0894-23d6-4b77-863e-5e207cabab3e">


## III. Foreign Fear Index

### 3.1 Variable Description
What we aimed to measure through the Foreign Index is the attractiveness foreigners feel about investing in the Korean market. To put this into account, we first set up the variable as follows:
- Net Foreign Purchase * USD/KRW Exchange Rate

Since a higher USD/KRW exchange rate tends to reduce the profitability of foreign investors, we adjusted for this exchange rate risk by incorporating the adjusted figure into the calculation. Moreover, all data used in the Foreign Fear Index were processed in the same manner as the Korean Fear Index.

### 3.2 Granger Causality
The Granger Causality test is a regression-based methodology used to analyze whether two time series exhibit a causal relationship. More specifically, it compares the results of a regression analysis predicting the future of a time series (Y) based only on its past data, with those of a regression analysis using both the past data of Y and another time series (X). If the results show a statistically significant difference, it indicates that the past data of X have a meaningful impact on predicting Y.

<img width="409" alt="image" src="https://github.com/user-attachments/assets/f5351e4b-1c6f-4997-9194-a4504b8a2194">

However, as shown in the results, the p-value is notably high, suggesting limited significance and a need to strengthen the Foreign Fear Index.

### 3.3 Variable Description
The Foreign Fear Index was refined with extra variables. The final selected variables were as follows:

  1. 3-Year Interest Rate Spread: US-Korea bond yield differences.
  2. Dollar Index (DXY): Global economic conditions and currency fluctuations.

While there were many other candidate variables considered, these two variables were chosen based on their relevance to how much foreign investors trust the Korean market and find it attractive for investment. Variables that were logically inconsistent with this framework were excluded, leaving only those that passed our final selection process.
Although we initially considered including macroeconomic indicators like GDP growth rates, we excluded them due to concerns about distortion from using monthly data. Similarly, while we aimed to utilize valuation metrics given the high proportion of foreign investment in Korea’s large-cap stocks, these variables were excluded due to inconsistencies across industrial sectors during the company selection process.

### 3.4 Index Strengthening Variable
**3.4.1 3-Year Interest Rate Spread:**
- Captures cost differences for investors between US and Korea.
We extracted and compared bond yields from the U.S. and Korea, aiming to incorporate the logic of carry trade directly into the analysis. The carry trade strategy involves borrowing funds in low-interest-rate regions and investing in high-interest-rate regions. Using the interest rate differential between the U.S. and Korea, we identified factors that drive the inflow of investment funds.

**3.4.2 Dollar Index:**
- Measures relative strength of USD against other major currencies.
The Dollar Index was included to reflect global economic conditions. This index accounts for the cost of currency exchange for foreign investors. The stronger the dollar, the less attractive the Korean market becomes for investment, and this assumption was incorporated into our variable selection.

### 3.5 Final Variable Selection Result
- Korean Fear Index : Market Momentum, Stock Intensity, Stock Price Breadth, Put/Call Option Ratio, Market Volatility, Safe Haven Demand, Junk Bond Demand
- Foreign Fear Index : Net Foreign Purchase * USD/KRW Exchange Rate, 3-Year Interest Rate Spread, Dollar Index (DXY)
Regression analysis results shown below proved minimal correlation among most variables, confirming that they could be used without significant issues.

<img width="301" alt="image" src="https://github.com/user-attachments/assets/b0a3219a-63bc-4d01-89a6-5e6d2375fd25">


### 3.6 Granger Causality Comparison and Stationary Testing
The Granger causality test results after strengthening the index show that the detailed p-values are displayed as 0 due to rounding, but the actual values are extremely low. This confirms that the foreign fear index significantly impacts the Korean market fear index. However, since the Granger causality test assumes stationarity of the time series data, we conducted unit root tests using the ADF and KPSS methods. Both tests confirmed that the data were stationary within the acceptable significance levels.

<img width="256" alt="image" src="https://github.com/user-attachments/assets/84ba1250-4e58-4c52-a205-0e6af1f97d19">

ADF Test (KOR, FOR)

<img width="251" alt="image" src="https://github.com/user-attachments/assets/a59b8df9-a935-4a31-b99c-247d21c5c864">

<img width="242" alt="image" src="https://github.com/user-attachments/assets/72ecc79e-d822-4543-864b-c1125bccd1de">

KPSS Test (KOR, FOR)

<img width="220" alt="image" src="https://github.com/user-attachments/assets/23832f1c-1cb3-4311-b265-44eecdef9de2">

<img width="220" alt="image" src="https://github.com/user-attachments/assets/0d1fedfd-1d2c-479b-9728-64c012d2da24">

### 3.7 Visualization of Korean & Foreign Fear Index

<img width="488" alt="image" src="https://github.com/user-attachments/assets/59411c5e-089a-4994-8692-18bdeb8e29da">

We visualized the data to observe its impact and identified a tendency for the foreign fear index to precede the Korean market fear index to some extent. Based on this observation, we aim to validate how the time lag between foreign fear and Korean market fear could be utilized in the market, akin to volatility trading, to develop effective investment strategies.

## IV. Backtesting

### 4.1 Literature Review and Comparison
When examining prior research on market timing strategies using fear indices, it was common to set specific thresholds and rebalance the portfolio whenever the score reaches these levels. For instance, Hanwha Investment & Securities reported a market timing strategy achieving an excess return of 0.23%.
Our approach incorporated a more multidimensional and reliable investment strategy by reflecting the flow of foreign funds through a more realistic index.

### 4.2 Backtesting Procedure and Results
Methodology:
  - Data Period: 2013-08-06 to 2024-11-08.
  - Initial capital: 100M KRW split into stocks (60%) and cash (40%) with periodic rebalancing of 2:8 or 8:2.
  - Assumptions: Transaction costs were excluded.

We calculated the spread between the foreign fear index and the Korean fear index to assess the relative sentiment in the market. The spread is defined as:
**Spread = (Foreign Fear Index) - (Korean Fear Index)**

Based on the spread, we identified four market scenarios to guide portfolio rebalancing strategies:

**1. Spread > 0 and Korean Fear Index < 50:**  
   Foreign investors exhibit greed while the Korean market reflects fear, indicating a **buy** opportunity due to potential market undervaluation.

**2. Spread < 0 and Korean Fear Index ≥ 50:**  
   Foreign investors show fear while the Korean market reflects greed, suggesting a **sell** strategy due to possible market overvaluation.

**3. Foreign Fear Index ≥ 80 and Korean Fear Index ≥ 80:**  
   Both foreign and Korean markets are in extreme fear, representing a **sell** scenario to avoid significant downside risk.

**4. Foreign Fear Index ≤ 20 and Korean Fear Index ≤ 20:**  
   Both foreign and Korean markets exhibit extreme greed, creating a **buy** opportunity to leverage positive sentiment and market optimism.

Portfolio rebalancing decisions were executed based on these scenarios, reflecting adjustments to asset allocations according to the spread and the prevailing market conditions.

<img width="726" alt="image" src="https://github.com/user-attachments/assets/eb20f3f0-0ecc-4740-b346-8afecba51a12">

**Backtesting Results**

The results of our backtesting can be summarized in three key findings:
1. Lower Volatility: Our strategy exhibited lower volatility compared to benchmark indices.
2. Improved Resilience in Bear Markets: The strategy demonstrated stronger defensive performance during market downturns.
3. Higher Final Returns: The final returns of our strategy exceeded those of the benchmark.

## V. Conclusion

### 5.1 Insights

**Leading Indicators of Foreign Investor Sentiment**

- The strategy demonstrates that following a **fear-spread-based portfolio** can reduce risks compared to a simple **long-only strategy**, while also having the potential to amplify returns.  
- This suggests that the foreign fear index can serve as a leading indicator for market trends in Korea.

**Fund Design Feasibility**

- Rule-based funds or **robot-advised models** can be developed based on the foreign fear index for real-world application.
- Example: “Smart Beta Funds based on Fear/Greed Indices.”
  
### 5.2 Limitations

**Lack of Diversity in Foreign Investor Composition**
- Foreign investors in Korea are not limited to the U.S.; they also include countries like the UK, Singapore, and China.  
- However, the current strategy predominantly reflects U.S.-centric factors, such as the Dollar Index and U.S.-Korea interest rate spreads, without fully accounting for diverse investor origins.

![image](https://github.com/user-attachments/assets/336796e1-5d12-449a-8d0a-b2b44573410a)


**Ignoring Transaction Costs**
- The current strategy does not account for transaction costs, such as fees, spreads, and taxes, incurred during rebalancing.  
- Implications: Accumulated transaction costs from frequent rebalancing may significantly reduce total returns, undermining the theoretical performance.  
- Additionally, the current strategy adjusts buy/sell ratios based on signals to ratios like 8:2 or 2:8, leading to relatively high trading frequency.
