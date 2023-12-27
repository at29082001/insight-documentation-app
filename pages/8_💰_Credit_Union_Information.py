import streamlit as st


st.set_page_config(page_title="Credit Union Information", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Credit Union Information 💰")

# Image
st.image("pages/image/credit_unions.jpg", width=700)

# Text to be displayed in the blue box
info_text = """
Established by the U.S. Congress in 1970, the National Credit Union Administration (NCUA) is an autonomous federal agency responsible for safeguarding member deposits in federally insured credit unions. It provides deposit insurance, protecting the financial interests of credit union members. Additionally, the NCUA oversees and regulates federal credit unions, ensuring their compliance with relevant laws and regulations. Through its chartering process, the NCUA grants authorization for credit unions to operate, facilitating their establishment and growth. Overall, the NCUA plays a crucial role in promoting stability, consumer protection, and sound governance within the credit union industry. 
The National Credit Union Administration (NCUA) provides several key features and information to credit unions, credit union members, and the general public.   
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)

# Datasets section
st.subheader('Some of the prominent features and information provided by the NCUA include:')

# Create an expandable box
with st.expander("**Deposit Insurance** 💡"):
    # Content inside the expandable box
    st.write("The NCUA administers the National Credit Union Share Insurance Fund (NCUSIF), which provides insurance coverage for member deposits in federally insured credit unions. The standard coverage is up to $250,000 per individual depositor, ensuring that members' deposits are protected in case of a credit union's failure.")
    
# Create an expandable box
with st.expander("**Regulatory Guidance** 💡"):
    # Content inside the expandable box
    st.write("The NCUA sets and enforces regulations and guidelines that govern credit union operations. It provides guidance to credit unions on compliance matters, helping them operate within the legal framework and ensuring financial safety and soundness.")
    
# Create an expandable box
with st.expander("**Examination and Supervision** 💡"):
    # Content inside the expandable box
    st.write("The NCUA conducts regular examinations and on-site inspections of credit unions to assess their financial condition and compliance with regulations. This supervision helps identify potential risks and weaknesses, allowing for timely corrective actions.")
    
# Create an expandable box
with st.expander("**Chartering and Field of Membership** 💡"):
    # Content inside the expandable box
    st.write("The NCUA is responsible for granting federal charters to credit unions, allowing them to operate as federally chartered institutions. It also approves expansions of credit unions' fields of membership, enabling them to serve more individuals and communities.")
    
# Create an expandable box
with st.expander("**Financial Literacy and Education** 💡"):
    # Content inside the expandable box
    st.write("The NCUA promotes financial literacy among credit union members and the general public. It offers educational resources, tools, and initiatives to improve financial knowledge and decision-making.")
    
# Create an expandable box
with st.expander("**Consumer Complaints and Assistance** 💡"):
    # Content inside the expandable box
    st.write("The NCUA handles consumer complaints related to credit unions and provides assistance to resolve issues between credit unions and their members.")
    
# Create an expandable box
with st.expander("**Industry Data and Reports** 💡"):
    # Content inside the expandable box
    st.write("The NCUA collects and publishes data on credit unions' financial performance, trends, and industry statistics. This information helps credit unions and stakeholders stay informed about the credit union sector's health and performance.")
    
# Create an expandable box
with st.expander("**Risk Management Resources** 💡"):
    # Content inside the expandable box
    st.write("The NCUA offers risk management resources and best practices to help credit unions identify and manage potential risks effectively. ")
    
# Create an expandable box
with st.expander("**Advocacy and Representation** 💡"):
    # Content inside the expandable box
    st.write("The NCUA represents the credit union industry's interests at the federal level and advocates for policies that support the growth and sustainability of credit unions.")
    
# Create an expandable box
with st.expander("**Cybersecurity and Technology Guidance** 💡"):
    # Content inside the expandable box
    st.write("The NCUA provides guidance on cybersecurity and technology best practices to help credit unions protect sensitive information and digital assets.")
    


# SQL Queries section
st.subheader('SQL Queries')

# View 1
st.markdown("""
**Create a view to show basic credit union information:**
```sql
CREATE OR REPLACE VIEW VIEW_CREDIT_UNION_INFO AS 
SELECT CREDIT_UNION_NO, CREDIT_UNION_NAME, STATE_CODE, CITY, COUNTY_NAME 
FROM CREDIT_UNION_BRANCH_INFORMATION;
```""")

# View 2
st.markdown("""
**Create a view to show main offices of credit unions:**
```sql
CREATE OR REPLACE VIEW VIEW_MAIN_OFFICES AS 
SELECT CREDIT_UNION_NAME, MAIN_OFFICE, CITY, STATE_CODE 
FROM CREDIT_UNION_BRANCH_INFORMATION 
WHERE MAIN_OFFICE = 'Yes';
```""")

# View 3
st.markdown("""
**Create a view to show credit union branches by state:**
```sql
CREATE OR REPLACE VIEW VIEW_BRANCHES_BY_STATE AS 
SELECT CREDIT_UNION_NAME, SITE_NAME, CITY, STATE_CODE 
FROM CREDIT_UNION_BRANCH_INFORMATION;
```""")

st.subheader('Business Needs')

business_needs = """

**Deposit Insurance and Member Protection**:  

- The NCUA provides deposit insurance through the National Credit Union Share Insurance Fund (NCUSIF). 

- This insurance coverage protects the deposits of credit union members, instilling confidence in the credit union system and ensuring the financial well-being of individual members. 

**Regulatory Compliance**:  

- Credit unions must adhere to various federal regulations to operate legally and maintain financial stability. 

- The NCUA establishes and enforces these regulations, offering clear guidelines and standards that credit unions need to follow to comply with the law. 

**Examination and Supervision**: 

- The NCUA conducts regular examinations and on-site inspections of credit unions to assess their financial health and risk management practices. 

- This supervision helps identify potential issues early on and allows credit unions to take corrective actions to ensure their stability. 

**Financial Literacy and Education**:  

- The NCUA promotes financial literacy among credit union members and the public. 

- By providing educational resources and initiatives, the NCUA empowers individuals to make informed financial decisions and improve their financial well-being. 


"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- ACCOUNT 
- ATM 
- CREDIT REDIT UNION BRANCH INFORMATION 
- TRADE NAMES  
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- ACCOUNT DESCRIPTION
- ACCOUNT NAME
- ACCOUNT ID
- STATUS
- CREDIT UNION NO
- CYCLE DATE
- JOIN NUMBER
- CREDIT UNION NAME
- SITE ID
- SITE NAME
- SITE TYPE
- ADDRESS LINE 1
- ADDRESS LINE 2
- CITY
- STATE CODE
- STATE NAME
- POSTAL CODE
- COUNTY
- GRANT ID
- DATE AWARDED
- AMOUNT
- GRANTOR
- OTHER GRANTOR
- GRANTOR TYPE
- CURRENT NAME
- TRADE NAME ID
- TRADE NAME



""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



