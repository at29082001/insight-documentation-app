import streamlit as st


st.set_page_config(page_title="Demographics Statistics By Zip Code ", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Demographics Statistics By Zip Code 🗺️")

# Image
st.image("pages/image/zip.jpg", width=700)


# Text to be displayed in the blue box
info_text = """
The dataset represented by the DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE appears to provide detailed demographic statistics based on various attributes within specific jurisdictions, often identified by zip codes. 
The dataset aims to offer a comprehensive overview of the demographic makeup within different jurisdictions, allowing businesses, organizations, researchers, and policymakers to gain insights into population characteristics such as gender, ethnicity, citizenship status, and public assistance reception. The dataset aggregates this information for ease of access and analysis, enabling users to make informed decisions, conduct research, and develop strategies that align with the needs and attributes of specific jurisdictions. It serves as a valuable resource for understanding and addressing diverse demographic aspects within various communities.     
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)





st.subheader('Datasets Include')

dataset_inc= """

**JURISDICTION_NAME** : Name or identifier of the jurisdiction (e.g., zip code) 

**COUNT_PARTICIPANTS** : Total count of participants within the jurisdiction 

**COUNT_FEMALE** : Count of participants who identify as female 

**PERCENT_FEMALE** : Percentage of participants who identify as female 

**COUNT_MALE** : Count of participants who identify as male 

**PERCENT_MALE** : Percentage of participants who identify as male 

**COUNT_GENDER_UNKNOWN** : Count of participants with unknown gender identity 

**PERCENT_GENDER_UNKNOWN** : Percentage of participants with unknown gender identity 

**COUNT_GENDER_TOTAL** : Total count of participants regardless of gender 

PERCENT_GENDER_TOTAL** : Percentage of the total count of participants 

**COUNT_PACIFIC_ISLANDER** : Count of participants who identify as Pacific Islander 

**PERCENT_PACIFIC_ISLANDER** : Percentage of participants who identify as Pacific Islander 

**COUNT_HISPANIC_LATINO** : Count of participants who identify as Hispanic or Latino 

**PERCENT_HISPANIC_LATINO** : Percentage of participants who identify as Hispanic or Latino 

**COUNT_AMERICAN_INDIAN** : Count of participants who identify as American Indian 

**PERCENT_AMERICAN_INDIAN** : Percentage of participants who identify as American Indian 

**COUNT_ASIAN_NON_HISPANIC** : Count of participants who identify as Asian (non-Hispanic) 

**PERCENT_ASIAN_NON_HISPANIC** : Percentage of participants who identify as Asian (non-Hispanic) 

**COUNT_WHITE_NON_HISPANIC** : Count of participants who identify as White (non-Hispanic) 

**PERCENT_WHITE_NON_HISPANIC** : Percentage of participants who identify as White (non-Hispanic) 

**COUNT_BLACK_NON_HISPANIC** : Count of participants who identify as Black (non-Hispanic) 

**PERCENT_BLACK_NON_HISPANIC** : Percentage of participants who identify as Black (non-Hispanic) 

**COUNT_OTHER_ETHNICITY** : Count of participants who identify with other ethnicities 

**PERCENT_OTHER_ETHNICIT** : Percentage of participants who identify with other ethnicities 

**COUNT_ETHNICITY_UNKNOWN** : Count of participants with unknown ethnicity 

**PERCENT_ETHNICITY_UNKNOWN** : Percentage of participants with unknown ethnicity 

**COUNT_ETHNICITY_TOTAL** : Total count of participants regardless of ethnicity 

**PERCENT_ETHNICITY_TOTAL** : Percentage of the total count of participants 

**COUNT_PERMANENT_RESIDENT_ALIEN** : Count of participants with permanent resident alien status 

**PERCENT_PERMANENT_RESIDENT_ALIEN** : Percentage of participants with permanent resident alien status 

**COUNT_US_CITIZEN** : Count of participants who are U.S. citizens 

**PERCENT_US_CITIZEN** : Percentage of participants who are U.S. citizens 

**COUNT_OTHER_CITIZEN_STATUS** : Count of participants with other citizen status 

**PERCENT_OTHER_CITIZEN_STATUS** : Percentage of participants with other citizen status 

**COUNT_CITIZEN_STATUS_UNKNOWN** : Count of participants with unknown citizen status 

**PERCENT_CITIZEN_STATUS_UNKNOWN** : Percentage of participants with unknown citizen status 

**COUNT_CITIZEN_STATUS_TOTAL** : Total count of participants regardless of citizen status 

**PERCENT_CITIZEN_STATUS_TOTAL** : Percentage of the total count of participants 

**COUNT_RECEIVES_PUBLIC_ASSISTANCE** : Count of participants receiving public assistance 

**PERCENT_RECEIVES_PUBLIC_ASSISTANCE** : Percentage of participants receiving public assistance 

**COUNT_NRECEIVES_PUBLIC_ASSISTANCE** : Count of participants not receiving public assistance 

**PERCENT_NRECEIVES_PUBLIC_ASSISTANCE** : Percentage of participants not receiving public assistance 

**COUNT_PUBLIC_ASSISTANCE_UNKNOWN** : Count of participants with unknown public assistance status 

**PERCENT_PUBLIC_ASSISTANCE_UNKNOWN** : Percentage of participants with unknown public assistance status 

**COUNT_PUBLIC_ASSISTANCE_TOTAL** : Total count of participants regardless of public assistance status 

**PERCENT_PUBLIC_ASSISTANCE_TOTAL** : Percentage of the total count of participants


"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color:#FEFBA2; padding: 20px; border-radius: 10px;">{dataset_inc}</div>',
    unsafe_allow_html=True,
)




 

# SQL Queries section
st.subheader('SQL Queries')

# Query 1
st.markdown("""
**Total Participants:**
```sql
SELECT JURISDICTION_NAME, COUNT_PARTICIPANTS 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# Query 2
st.markdown("""
**Gender Distribution:**
```sql
SELECT JURISDICTION_NAME, COUNT_FEMALE, COUNT_MALE, COUNT_GENDER_UNKNOWN, 
       PERCENT_FEMALE, PERCENT_MALE, PERCENT_GENDER_UNKNOWN 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# Query 3
st.markdown("""
**Ethnicity Distribution:**
```sql
SELECT JURISDICTION_NAME, COUNT_PACIFIC_ISLANDER, COUNT_HISPANIC_LATINO, 
       COUNT_AMERICAN_INDIAN, COUNT_ASIAN_NON_HISPANIC, COUNT_WHITE_NON_HISPANIC, 
       COUNT_BLACK_NON_HISPANIC, COUNT_OTHER_ETHNICITY, COUNT_ETHNICITY_UNKNOWN, 
       COUNT_ETHNICITY_TOTAL 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# Query 4
st.markdown("""
**Citizenship Status:**
```sql
SELECT JURISDICTION_NAME, COUNT_PERMANENT_RESIDENT_ALIEN, COUNT_US_CITIZEN, 
       COUNT_OTHER_CITIZEN_STATUS, COUNT_CITIZEN_STATUS_UNKNOWN, COUNT_CITIZEN_STATUS_TOTAL 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# Query 5
st.markdown("""
**Public Assistance:**
```sql
SELECT JURISDICTION_NAME, COUNT_RECEIVES_PUBLIC_ASSISTANCE, COUNT_NRECEIVES_PUBLIC_ASSISTANCE, 
       COUNT_PUBLIC_ASSISTANCE_UNKNOWN, COUNT_PUBLIC_ASSISTANCE_TOTAL 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# Query 6
st.markdown("""
**Gender Distribution Summary:**
```sql
SELECT  
    SUM(COUNT_FEMALE) AS Total_Females, 
    SUM(COUNT_MALE) AS Total_Males, 
    SUM(COUNT_GENDER_UNKNOWN) AS Total_Gender_Unknown 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# Query 7
st.markdown("""
**Ethnicity Distribution Summary:**
```sql
SELECT  
    SUM(COUNT_PACIFIC_ISLANDER) AS Total_Pacific_Islander, 
    SUM(COUNT_HISPANIC_LATINO) AS Total_Hispanic_Latino, 
    SUM(COUNT_AMERICAN_INDIAN) AS Total_American_Indian, 
    SUM(COUNT_ASIAN_NON_HISPANIC) AS Total_Asian_Non_Hispanic, 
    SUM(COUNT_WHITE_NON_HISPANIC) AS Total_White_Non_Hispanic, 
    SUM(COUNT_BLACK_NON_HISPANIC) AS Total_Black_Non_Hispanic, 
    SUM(COUNT_OTHER_ETHNICITY) AS Total_Other_Ethnicity, 
    SUM(COUNT_ETHNICITY_UNKNOWN) AS Total_Ethnicity_Unknown 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# Query 8
st.markdown("""
**Citizenship Distribution Summary:**
```sql
SELECT  
    SUM(COUNT_PERMANENT_RESIDENT_ALIEN) AS Total_Permanent_Resident_Alien, 
    SUM(COUNT_US_CITIZEN) AS Total_US_Citizen, 
    SUM(COUNT_OTHER_CITIZEN_STATUS) AS Total_Other_Citizen_Status, 
    SUM(COUNT_CITIZEN_STATUS_UNKNOWN) AS Total_Citizen_Status_Unknown 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# Query 9
st.markdown("""
**Public Assistance Summary:**
```sql
SELECT  
    SUM(COUNT_RECEIVES_PUBLIC_ASSISTANCE) AS Total_Receives_Public_Assistance, 
    SUM(COUNT_NRECEIVES_PUBLIC_ASSISTANCE) AS Total_Not_Receives_Public_Assistance, 
    SUM(COUNT_PUBLIC_ASSISTANCE_UNKNOWN) AS Total_Public_Assistance_Unknown 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# Query 10
st.markdown("""
**Top Jurisdictions by Total Participants:**
```sql
SELECT JURISDICTION_NAME, COUNT_PARTICIPANTS 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
ORDER BY COUNT_PARTICIPANTS DESC 
LIMIT 10;
```""")

# Query 11
st.markdown("""
**Gender Diversity by Jurisdiction:**
```sql
SELECT JURISDICTION_NAME, PERCENT_FEMALE 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
ORDER BY PERCENT_FEMALE DESC;
```""")

# Query 12
st.markdown("""
**Ethnicity Distribution Analysis:**
```sql
SELECT JURISDICTION_NAME, PERCENT_WHITE_NON_HISPANIC, PERCENT_BLACK_NON_HISPANIC 
FROM DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
ORDER BY PERCENT_WHITE_NON_HISPANIC DESC, PERCENT_BLACK_NON_HISPANIC DESC;
```""")

st.subheader('Business Needs')

business_needs = """

**Market Segmentation**: 

Businesses can use demographic data to segment markets and tailor their products, services, and marketing efforts to specific groups.  

**Resource Allocation**: 

Government agencies and social service organizations can allocate resources effectively by understanding the distribution of population characteristics. This can help in planning programs, services, and assistance for various demographic groups. 

**Social Equity Analysis**: 

Demographic data can be used to identify areas where there might be disparities in access to resources or services based on gender, ethnicity, or other factors. This can guide efforts to promote social equity. 

**Community Engagement**: 

Community organizations can use demographic insights to tailor their engagement efforts, events, and initiatives to the specific demographics of each jurisdiction, fostering a sense of inclusion and community involvement. 

**Public Policy Development**: 

Policymakers can use demographic data to formulate and evaluate policies related to gender equality, diversity, social welfare, and more. For instance, understanding gender distribution can inform policies related to workplace diversity and gender equality. 

**Healthcare Planning**: 

Healthcare providers can analyze demographic data to anticipate health needs within different communities. This could include planning for language-specific services, health education campaigns, or disease prevention strategies.  

**Educational Outreach**: 

Educational institutions can tailor their programs and outreach efforts to address the needs of diverse student populations, ensuring inclusivity and equal educational opportunities.  

**Business Expansion**: 

Companies looking to expand can assess demographic data to identify regions where their products or services might have a higher demand based on population characteristics. 

**Research and Analysis**: 

Researchers can leverage demographic statistics to study trends, correlations, and patterns across different demographic groups, leading to insights in fields like sociology, economics, and public health. 

**Civic Engagement**: 

Political campaigns and advocacy groups can use demographic insights to target their messaging and efforts to specific populations that are more likely to resonate with their causes. 

**Public Reporting**: 

Government agencies can provide transparent demographic information to the public for accountability and informed decision-making. 


"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- DEMOGRAPHIC STATISTICS 
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- JURISDICTION NAME  
- COUNT PARTICIPANTS  
- COUNT FEMALE  
- PERCENT FEMALE  
- COUNT MALE  
- PERCENT MALE  
- COUNT GENDER UNKNOWN  
- PERCENT GENDER UNKNOWN  
- COUNT GENDER TOTAL  
- PERCENT GENDER TOTAL  
- COUNT PACIFIC ISLANDER 
- PERCENT PACIFIC ISLANDER  
- COUNT HISPANIC LATINO  
- PERCENT HISPANIC LATINO  
- COUNT AMERICAN INDIAN  
- PERCENT AMERICAN INDIAN  
- COUNT ASIAN NON HISPANIC  
- PERCENT ASIAN NON HISPANIC  
- COUNT WHITE NON HISPANIC  
- PERCENT WHITE NON HISPANIC  
- COUNT BLACK NON HISPANIC  
- PERCENT BLACK NON HISPANIC  
- COUNT OTHER ETHNICITY  
- PERCENT OTHER ETHNICITY  
- COUNT ETHNICITY UNKNOWN  
- PERCENT ETHNICITY UNKNOWN  
- COUNT ETHNICITY TOTAL  
- PERCENT ETHNICITY TOTAL  
- COUNT PERMANENT RESIDENT ALIEN  
- PERCENT PERMANENT RESIDENT ALIEN  
- COUNT US CITIZEN  
- PERCENT US CITIZEN  
- COUNT OTHER CITIZEN STATUS  
- PERCENT OTHER CITIZEN STATUS  
- COUNT CITIZEN STATUS UNKNOWN  
- PERCENT CITIZEN STATUS UNKNOWN  
- COUNT CITIZEN STATUS TOTAL  
- PERCENT CITIZEN STATUS TOTAL  
- COUNT RECEIVES PUBLIC ASSISTANCE  
- PERCENT RECEIVES PUBLIC ASSISTANCE  
- COUNT NRECEIVES PUBLIC ASSISTANCE  
- PERCENT NRECEIVES PUBLIC ASSISTANCE  
- COUNT PUBLIC ASSISTANCE UNKNOWN  
- PERCENT PUBLIC ASSISTANCE UNKNOWN  
- COUNT PUBLIC ASSISTANCE TOTAL  
- PERCENT PUBLIC ASSISTANCE TOTAL
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



