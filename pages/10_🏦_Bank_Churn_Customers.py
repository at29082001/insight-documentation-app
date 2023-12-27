import streamlit as st


st.set_page_config(page_title="Bank Churn Customers ", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Bank Churn Customers 🏦")

# Image
st.image("pages/image/Customer-churn.png", width=700)

# Text to be displayed in the blue box
info_text = """
Customer churn, often referred to as attrition or customer turnover, is a critical metric that assesses the rate at which customers disengage from a bank's products and services. In the banking industry, churn occurs when customers, who were once actively engaged with the bank, decide to terminate their accounts, close credit lines, cancel credit cards, or stop using certain financial services offered by the bank.    
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)

# Datasets section
st.subheader('Factors Contributing to Churn')

# Create an expandable box
with st.expander("**Financial Performance** 💡"):
    # Content inside the expandable box
    st.write("Changes in a customer's financial situation, such as reduced income, increased debt, or unemployment, can lead to decreased engagement with banking services.")
    
# Create an expandable box
with st.expander("**Service Dissatisfaction** 💡"):
    # Content inside the expandable box
    st.write("Poor customer service experiences, unresolved issues, or dissatisfaction with the quality of services provided by the bank can drive customers to seek alternatives. ")
    
# Create an expandable box
with st.expander("**Competitive Offerings** 💡"):
    # Content inside the expandable box
    st.write("Customers might be enticed by competitive offerings from other banks, such as better interest rates, lower fees, or innovative financial products.")
    
# Create an expandable box
with st.expander("**Life Events** 💡"):
    # Content inside the expandable box
    st.write("Major life events like relocation, marriage, divorce, or retirement can prompt customers to reassess their banking relationships and potentially switch to institutions that better align with their changing needs.")
    
# Create an expandable box
with st.expander("**Lack of Relevance** 💡"):
    # Content inside the expandable box
    st.write("If a bank fails to offer personalized solutions and relevant financial products to customers, they may feel neglected and seek banking services elsewhere.")
    
# Create an expandable box
with st.expander("**Technological Changes** 💡"):
    # Content inside the expandable box
    st.write("Rapid advancements in digital technology and online banking can influence customer preferences, causing them to shift to banks that offer more convenient and user-friendly digital experiences.")
 
 

# SQL Queries section
st.subheader('SQL Queries')

# Query 1
st.markdown("""
**Count the total number of customers:**
```sql
SELECT COUNT(*) AS total_customers 
FROM CHURN_BANK_CUSTOMERS;
```""")

# Query 2
st.markdown("""
**List customers who have exited (churned):**
```sql
SELECT CUSTOMER_ID, SURNAME, EXITED 
FROM CHURN_BANK_CUSTOMERS 
WHERE EXITED = 1;
```""")

# Query 3
st.markdown("""
**Calculate the average age of active members:**
```sql
SELECT AVG(AGE) AS avg_age 
FROM CHURN_BANK_CUSTOMERS 
WHERE IS_ACTIVE_MEMBER = 1;
```""")

# Query 4
st.markdown("""
**Identify the highest and lowest credit scores:**
```sql
SELECT MAX(CREDIT_SCORE) AS max_credit_score, MIN(CREDIT_SCORE) AS min_credit_score 
FROM CHURN_BANK_CUSTOMERS;
```""")

st.subheader('Business Needs')

business_needs = """

Churn for Bank Customers refers to the phenomenon where customers discontinue their banking relationship with a particular bank and shift their accounts  or business to another financial institution. 

**Churn Analysis**:  

- The table allows tracking customer churn by storing relevant information like customer ID, credit score, geography, gender, age, tenure, balance, number of products, credit card status, active membership, estimated salary, and exit status.  

**Product Analysis**:  

- The "NUM_OF_PRODUCTS" field can be used to analyze the number of products or services each customer is using. This information can guide the bank's efforts to upsell or cross-sell additional products to customers who have a lower product count. 

**Marketing Campaigns**: 

- The table can aid in designing targeted marketing campaigns based on various customer attributes.  

- The bank could promote specific products to customers with certain characteristics or create tailored offers to prevent churn. 

**Customer Experience Enhancement**:  

- By analyzing customer data and churn reasons, the bank can identify pain points in the customer journey and make improvements to enhance overall customer experience. 


"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- CHURN BANK CUSTOMERS
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- ROW NUMBER
- CUSTOMER ID
- SURNAME
- CREDIT SCORE
- GEOGRAPHY
- GENDER
- AGE
- TENURE
- BALANCE
- NUM OF PRODUCTS
- HASCR CARD
- IS ACTIVE MEMBER
- ESTIMATED SALARY
- EXITED
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



