import time
import numpy as np
import streamlit as st
import pandas as pd
# import snowflake.connector
import configparser
from io import BytesIO
import zipfile
import requests

st.set_page_config(page_title="Nasdaq Data", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Nasdaq Data 📈")

# Image
st.image("pages/image/nasdaq1.png", width=700)

# Text to be displayed in the blue box
info_text = """
The The NASDAQ, short for the National Association of Securities Dealers Automated Quotations, is a major stock exchange in the United States. Established in 1971, it stands out for being an electronic exchange, meaning it relies on computer systems for trading rather than a traditional trading floor. NASDAQ provides a platform where companies, ranging from tech giants to various others, can list their shares for public trading.
What makes NASDAQ distinct is its fully electronic nature. Trades are executed swiftly through a computerized system, allowing buyers and sellers to connect efficiently. It hosts a diverse array of companies, including many in the technology sector, and accommodates both U.S. and international listings.
Participants in NASDAQ include individual and institutional investors, as well as market makers who facilitate trades to maintain liquidity. The exchange has been a pioneer in technological advancements in trading, introducing innovations such as online trading platforms and electronic execution.
While based in the U.S., NASDAQ has a global impact, attracting listings and investors from around the world. It is associated with key stock market indices like the NASDAQ Composite Index, which includes a broad range of listed companies, and the NASDAQ-100 Index, focusing on major non-financial companies.
NASDAQ is known for hosting significant Initial Public Offerings (IPOs), especially in the technology sector, contributing to its reputation for innovation and growth-oriented companies. It plays a crucial role in global financial markets, embodying the modern, electronically driven landscape of securities trading.
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)


# Datasets section
st.subheader('Datasets')

# Create an expandable box
with st.expander("**Nasdaq Stock Data** 💡"):
    # Content inside the expandable box
    st.write("The dataset you have, spanning from 1975 to 2020, likely contains historical stock market data for various securities listed on Nasdaq during this period. This data could include information such as daily stock prices, trading volumes, and other relevant metrics for the listed companies.")
    



# SQL Queries section
st.subheader('SQL Queries')

# Query 1
st.markdown("""
**Fetch Symbols for NASDAQ-Traded Securities:**
```sql
SELECT SYMBOL FROM your_table WHERE NASDAQ_TRADED = 'Y';""")

# Query 2
st.markdown("""
**Calculate Daily Price Range:**
```sql
SELECT SECURITY_NAME, DATE, HIGH - LOW AS DAILY_PRICE_RANGE FROM VW_NASDAQ_STOCK_DATA;""")


st.markdown("""
**Top 5 Securities by Trading Volume:**
```sql
SELECT SECURITY_NAME, AVG(ADJ_CLOSE) AS AVG_ADJ_CLOSE FROM VW_NASDAQ_STOCK_DATA GROUP BY SECURITY_NAME;""")

st.markdown("""
**Average Adjusted Closing Price for Each Symbol:**
```sql
SELECT SECURITY_NAME, AVG(ADJ_CLOSE) AS AVG_ADJ_CLOSE FROM VW_NASDAQ_STOCK_DATA GROUP BY SECURITY_NAME;""")


st.markdown("""
**Find SECURITY with the Highest Closing Price on a Specific Date:**
```sql
SELECT
    SECURITY_NAME,
    CLOSE
FROM VW_NASDAQ_STOCK_DATA
WHERE CLOSE is not null and DATE BETWEEN '2000-01-01' AND '2019-01-01'
ORDER BY CLOSE DESC
LIMIT 1;""")


st.markdown("""
**Calculate Weighted Average Price (Volume-Weighted Average Price - VWAP):**
```sql
SELECT DATE, SUM(CLOSE * VOLUME) / SUM(VOLUME) AS VWAP
FROM VW_NASDAQ_STOCK_DATA
GROUP BY DATE;""")


st.subheader('Business Needs')

business_needs = """

**Market Analysis**: NASDAQ data is crucial for market analysis, helping businesses and investors understand trends, performance, and overall market conditions.

**Investment Decision-Making**: Investors use NASDAQ data to make informed decisions about buying or selling stocks, managing portfolios, and optimizing investment strategies.

**Risk Management**: Businesses leverage NASDAQ data for risk assessment, identifying potential market fluctuations and making decisions to mitigate risks associated with stock investments.

**Financial Planning**: Companies use NASDAQ data to assess their financial health, monitor stock performance, and make strategic decisions related to fundraising, mergers, or acquisitions.

**Benchmarking**: NASDAQ serves as a benchmark for many technology and growth-oriented companies. Businesses use this data for performance benchmarking against market indices.

**IPO Planning**: Companies planning Initial Public Offerings (IPOs) analyze NASDAQ trends to gauge market sentiment, determine optimal timing, and strategize their public debut.

**Market Intelligence**: NASDAQ data provides valuable insights into competitor performance, industry trends, and overall market dynamics, enabling businesses to stay competitive.

**Algorithmic Trading**: High-frequency trading and algorithmic trading strategies rely on real-time NASDAQ data to execute trades, optimize algorithms, and capitalize on market opportunities.

**Portfolio Management**: Investment firms and individuals use NASDAQ data for effective portfolio management, diversification, and performance tracking.

**Regulatory Compliance**: Businesses in the financial sector use NASDAQ data to ensure compliance with regulatory requirements, reporting standards, and transparency obligations.
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)



st.subheader('Tables Included')
st.markdown("""

- NASDAQ SYMBOL
- NASDAQ DATA
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- ROW NUM 
- SECURITY NAME 
- DATE COMMENT 
- OPEN 
- HIGH 
- LOW 
- CLOSE
- ADJ CLOSE 
- VOLUME 
- SYMBOL 
- NASDAQ TRADED 
- LISTING EXCHANGE 
- ETF 
- ROUND LOT SIZE
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



















# import streamlit as st
# import pandas as pd
# import snowflake.connector
# import configparser
# from io import BytesIO
# import zipfile
# import requests

# # Snowflake connection parameters
# config = configparser.ConfigParser()
# config.read('snowflake.env')

# # Function to fetch data from the provided URL
# def fetch_data(url):
#     response = requests.get(url)
#     with zipfile.ZipFile(BytesIO(response.content), 'r') as z:
#         file_list = z.namelist()
#         df_combined = pd.DataFrame()
#         for file_name in file_list:
#             df = pd.read_csv(z.open(file_name))
#             df_combined = pd.concat([df_combined, df], ignore_index=True)
#     return df_combined

# Streamlit app begins here
# st.title('NASDAQ Stock Data Analysis')

# Load NASDAQ data
# nasdaq_url = 'YOUR_NASDAQ_DATA_URL'
# nasdaq_data = fetch_data(nasdaq_url)

# Display a sample of the data
# st.subheader('Sample Data')
# st.dataframe(nasdaq_data.head())