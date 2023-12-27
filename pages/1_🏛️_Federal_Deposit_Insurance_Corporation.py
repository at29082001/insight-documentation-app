import streamlit as st



st.set_page_config(page_title="Nasdaq Data", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Federal Deposit Insurance Corporation Data 🏛️")


# Image
st.image("pages/image/fdic.png", width=700)

# Text to be displayed in the blue box
info_text = """
The Federal Deposit Insurance Corporation (FDIC) is a vital government agency in the United States established to safeguard and stabilize the nation's banking system. Formed in response to the economic challenges of the Great Depression in the 1930s, the FDIC primarily operates as a guarantor of deposits held in U.S. banks and thrifts. Its fundamental purpose is to instill confidence in the financial system by offering insurance coverage for deposits, with the standard amount currently set at $250,000 per depositor, per bank. Beyond deposit insurance, the FDIC assumes a critical regulatory role, overseeing and examining banks to ensure their safety and soundness. In cases of bank failures, the FDIC takes charge of resolving the institution, either through the sale of its assets or by facilitating the transfer of operations to another financial entity. This regulatory body extends its influence across a spectrum of financial institutions, ranging from large national banks to smaller community banks. By diligently assessing risks, promoting sound banking practices, and wielding resolution authority when necessary, the FDIC contributes significantly to the stability and confidence in the U.S. financial landscape. Its proactive measures in risk management, coupled with its role in maintaining the integrity of the banking sector, underscore the FDIC's crucial position in protecting depositors and ensuring the resilience of the country's financial system.
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)




# Datasets section
st.subheader('Datasets')

# Create an expandable box
with st.expander("**FDIC Failed Bank List** 💡"):
    # Content inside the expandable box
    st.write("The FDIC's failed bank list is a comprehensive record of banks and financial institutions that have been closed or taken over by the Federal Deposit Insurance Corporation due to financial distress or insolvency. This list is maintained by the FDIC on its official website and is regularly updated to reflect the status of failed banks.")
    
# Create an expandable box
with st.expander("**FDIC Insured Bank List** 💡"):
    # Content inside the expandable box
    st.write("An FDIC insured financial institution is a bank or savings association that is covered by deposit insurance provided by the Federal Deposit Insurance Corporation (FDIC) in the United States. When a bank is insured by the FDIC, it means that the deposits held by customers in that institution are protected up to certain limits in case the bank experiences financial difficulties, fails, or is closed.")


# SQL Queries section
st.subheader('SQL Queries')

# Query 1
st.markdown("""
**Fetch Symbols for NASDAQ-Traded Securities:**
```sql
SELECT SYMBOL FROM your_table WHERE NASDAQ_TRADED = 'Y';""")

# Query 2
st.markdown("""
**Find Failed Banks:**
```sql
SELECT * FROM VW_FDIC_INSURED_FINANCE_INSTITUTE WHERE failed_banklist IS NOT NULL;""")

# Query 3
st.markdown("""
**Get Banks in a Specific State:**
```sql
SELECT * FROM VW_FDIC_INSURED_FINANCE_INSTITUTE WHERE state_name = 'Your Desired State';""")

# Query 4
st.markdown("""
**Get Banks with Assets Greater Than a Certain Amount:**
```sql
SELECT * FROM VW_FDIC_INSURED_FINANCE_INSTITUTE WHERE asset > your_desired_amount;""")

# Query 5
st.markdown("""
**Find Failed Banks and Their Acquiring Institutions:**
```sql
SELECT name, failed_banklist, failed_bank_acquiring_insitution
FROM VW_FDIC_INSURED_FINANCE_INSTITUTE WHERE failed_banklist IS NOT NULL;""")

# Query 6
st.markdown("""
**Count the Number of Active Banks in Each State:**
```sql
SELECT state_name, COUNT(*) as num_active_banks
FROM VW_FDIC_INSURED_FINANCE_INSTITUTE WHERE active = 1
GROUP BY state_name;""")

# Query 7
st.markdown("""
**Calculate the Average Asset Value of Banks in Each State:**
```sql
SELECT state_name, AVG(asset) as avg_asset_value FROM VW_FDIC_INSURED_FINANCE_INSTITUTE
GROUP BY state_name;""")

# Query 8
st.markdown("""
**Find the Most Common Bank Class:**
```sql
SELECT bank_class, COUNT(*) as class_count FROM VW_FDIC_INSURED_FINANCE_INSTITUTE
GROUP BY bank_class ORDER BY class_count DESC LIMIT 1;""")

# Query 9
st.markdown("""
**Search for Banks with Specific Keywords in Their Name or Address:**
```sql
SELECT * FROM VW_FDIC_INSURED_FINANCE_INSTITUTE
WHERE name LIKE '%keyword%' OR Address LIKE '%keyword%';""")

# Query 10
st.markdown("""
**Find Banks in a Specific Metropolitan Area:**
```sql
SELECT * FROM VW_FDIC_INSURED_FINANCE_INSTITUTE
WHERE cbsa_metro_name = 'Your Desired Metropolitan Area';""")

st.subheader('Business Needs')

business_needs = """

**For Failed Bank List Data:** 

**Risk Assessment**: Financial institutions and investors can use the failed bank list to assess potential risks associated with specific banks or the banking industry as a whole.  

**Regulatory Analysis**: Regulatory agencies and policymakers utilize the data to analyze trends and patterns in bank failures, helping them identify potential weaknesses in the banking system. 

**Lessons Learned**: Studying failed banks provides valuable insights and lessons for the industry, contributing to better risk management practices and policies. 

**Investor Confidence**: Transparency in failed bank data fosters investor confidence, as they can understand the regulatory response to bank failures and the protection mechanisms for depositors.
 
**Consumer Awareness**: The list helps inform consumers about the health and stability of the banking system, influencing their decisions on where to place their deposits. 

**Merger and Acquisition Opportunities**: Healthy financial institutions may explore potential merger or acquisition opportunities with failed banks to expand their market presence. 

**For Non-Failed Bank List Data:** 

**Market Research**: Researchers and analysts use non-failed bank data to conduct market research and track the performance of financial institutions over time.
 
**Investment Decisions**: Investors rely on the data to make informed decisions regarding investments in banks and related financial products. 

**Business Expansion**: Financial institutions utilize the data to identify potential areas for business expansion and market growth opportunities. 

**Regulatory Compliance**: Banks use the data to ensure compliance with regulatory reporting requirements and standards. 

**Competitive Analysis**: Financial institutions compare their performance with other non-failed banks to evaluate their competitive position in the market. 

**Customer Insights**: Analyzing data on non-failed banks can provide insights into customer behavior and preferences, enabling banks to tailor their products and services
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- FDIC FAILED BANKLIST 
- FDIC INSURED FINANCIAL INSTITUTE
- FDIC OFFICE LOCATION
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- CERTIFICATE NUMBER
- DOCKET
- CBSA
- CBSA DIV       
- CBSA DIV FLG    
- CBSA DIV NO
- CBSA METRO  
- CBSA METRO FLG
- CBSA   
- CBSA METRO NAME
- CBSA MICRO FLG    
- CBSA NO
- DATE UPDATED
- STALP
- ZIP
- ACTIVE
- ADDRESS
- ASSET
- BANK CLASS
- CITY
- STATE NAME
- COUNTRY
- NAME
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")
