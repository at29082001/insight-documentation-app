import streamlit as st


st.set_page_config(page_title="DYCD Participant Demographic Statistics By Zip Code ", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# DYCD Participant Demographic Statistics By Zip Code 🗺️")

# Image
st.image("pages/image/zip.jpg", width=700)


# Text to be displayed in the blue box
info_text = """
DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE dataset contains demographic statistics for participants, particularly focusing on various categories such as race, ethnicity, gender, and more, within specific ZIP codes and dates. 
The dataset allows for a granular analysis of participant characteristics, supporting initiatives related to diversity and inclusion, community engagement, program effectiveness, and trend analysis over time. Privacy considerations and data quality are essential when using this dataset for decision-making or reporting.     
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)



st.subheader('Datasets Include')

dataset_inc= """

**DATE**: The date associated with the demographic statistics. 

**ZIP_CODE**: The ZIP code for which the demographic statistics are recorded. 

**BLACK_OR_AFRICAN_AMERICAN_COUNT**: Count of participants identifying as Black or African American. 

**BLACK_OR_AFRICAN_AMERICAN_PERCENTAGE**: Percentage of participants identifying as Black or African American. 

**MULTI_RACE_COUNT**: Count of participants identifying as belonging to multiple races. 

**MULTI_RACE_PERCENTAGE**: Percentage of participants identifying as belonging to multiple races. 

**WHITE_OR_CAUCASIAN_COUNT**: Count of participants identifying as White or Caucasian. 

**WHITE_OR_CAUCASIAN_PERCENTAGE**: Percentage of participants identifying as White or Caucasian. 

**HISPANIC_OR_LATINX_COUNT**: Count of participants identifying as Hispanic or Latinx. 

**HISPANIC_OR_LATINX_PERCENTAGE**: Percentage of participants identifying as Hispanic or Latinx. 

**NOT_HISPANIC_OR_LATINX_COUNT**: Count of participants not identifying as Hispanic or Latinx. 

**NOT_HISPANIC_OR_LATINX_PERCENTAGE**: Percentage of participants not identifying as Hispanic or Latinx. 

**NOT_SURE_COUNT**: Count of participants who are not sure about their demographic information. 

**NOT_SURE_PERCENTAGE**: Percentage of participants who are not sure about their demographic information. 

**X_NOT_MALE_OR_FEMALE_COUNT**: Count of participants who do not identify as male or female. 

**X_NOT_MALE_OR_FEMALE_PERCENTAGE**: Percentage of participants who do not identify as male or female.  

**ANOTHER_GENDER_COUNT**: Count of participants identifying as another gender. 

**ANOTHER_GENDER_PERCENTAGE**: Percentage of participants identifying as another gender. 

**DECLINE_TO_ANSWER_COUNT**: Count of participants who declined to answer. 

**DECLINE_TO_ANSWER_PERCENTAGE**: Percentage of participants who declined to answer. 

**DO_NOT_UNDERSTAND_THE_QUESTION_COUNT**: Count of participants who do not understand the question. 

**DO_NOT_UNDERSTAND_THE_QUESTION_PERCENTAGE**: Percentage of participants who do not understand the question. 

**FEMALE_GENDER_IDENTITY_COUNT**: Count of participants identifying as female. 

**FEMALE_GENDER_IDENTITY_PERCENTAGE**: Percentage of participants identifying as female. 

**MALE_GENDER_IDENTITY_COUNT**: Count of participants identifying as male. 

**MALE_GENDER_IDENTITY_PERCENTAGE**: Percentage of participants identifying as male. 

**MULTI_GENDER_IDENTITY_COUNT**: Count of participants identifying as having multiple gender identities. 

**MULTI_GENDER_IDENTITY_PERCENTAGE**: Percentage of participants identifying as having multiple gender identities. 

**NON_BINARY_NOT_FEMALE_OR_MALE_COUNT**: Count of participants identifying as non-binary and not female or male. 

**NON_BINARY_NOT_FEMALE_OR_MALE_PERCENTAGE**: Percentage of participants identifying as non-binary and not female or male. 

**NOT_SURE_GENDER_IDENTITY_COUNT**: Count of participants who are not sure about their gender identity. 

**NOT_SURE_GENDER_IDENTITY_PERCENTAGE**: Percentage of participants who are not sure about their gender identity. 

**TWO_SPIRIT_NATIVE_AMERICAN_FIRST_NATIONS_COUNT**: Count of participants identifying as Two-Spirit Native American or First Nations. 

**TWO_SPIRIT_NATIVE_AMERICAN_FIRST_NATIONS_PERCENTAGE**: Percentage of participants identifying as Two-Spirit Native American or First Nations. 

**MIDDLE_EASTERN_AND_NORTH_AFRICAN_COUNT**: Count of participants identifying as Middle Eastern and North African. 

**MIDDLE_EASTERN_AND_NORTH_AFRICAN_PERCENTAGE**: Percentage of participants identifying as Middle Eastern and North Africa. 

**OTHER_COUNT**: Count of participants identifying as other. 

**OTHER_PERCENTAGE**: Percentage of participants identifying as other.


"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color:#FEFBA2; padding: 20px; border-radius: 10px;">{dataset_inc}</div>',
    unsafe_allow_html=True,
)


# SQL Queries section
st.subheader('SQL Queries')

import streamlit as st

# View 1
st.markdown("""
**Retrieve Total Participants by Zip Code:**
```sql
SELECT ZIP_CODE, SUM(Black_or_African_American_Count + Multi_race_Count + White_or_Caucasian_Count) AS TotalParticipants 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
GROUP BY ZIP_CODE;
```""")

# View 2
st.markdown("""
**Get Percentage of Hispanic or Latinx Participants by Zip Code:**
```sql
SELECT ZIP_CODE, AVG(Hispanic_or_Latinx_Percentage) AS AveragePercentage 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
GROUP BY ZIP_CODE;
```""")

# View 3
st.markdown("""
**Find the Date with Highest number of participants:**
```sql
SELECT DATE 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
ORDER BY TotalParticipants DESC 
LIMIT 1;
```""")

# View 4
st.markdown("""
**Retrieve Gender Distribution for a Specific Zip Code:**
```sql
SELECT ZIP_CODE,  
       SUM(Female_Gender_Identity_Count) AS FemaleCount, 
       SUM(Male_Gender_Identity_Count) AS MaleCount, 
       SUM(Non_Binary_not_Female_or_Male_Count) AS NonBinaryCount 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
WHERE ZIP_CODE = 'your_zip_code' 
GROUP BY ZIP_CODE;
```""")

# View 5
st.markdown("""
**Get the Percentage of Participants who Declined to answer by Date:**
```sql
SELECT DATE, AVG(Decline_to_Answer_Percentage) AS AveragePercentage 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
GROUP BY DATE;
```""")

# View 6
st.markdown("""
**Find the Zip Codes with the Highest and Lowest Average Percentage of Not Sure Gender Identity:**
```sql
-- Highest
SELECT ZIP_CODE, AVG(Not_Sure_Gender_Identity_Percentage) AS AveragePercentage 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
GROUP BY ZIP_CODE 
ORDER BY AveragePercentage DESC, ZIP_CODE 
LIMIT 1;

-- Lowest
SELECT ZIP_CODE, AVG(Not_Sure_Gender_Identity_Percentage) AS AveragePercentage 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
GROUP BY ZIP_CODE 
ORDER BY AveragePercentage, ZIP_CODE 
LIMIT 1;
```""")

# View 7
st.markdown("""
**Identify the Date with the Highest Percentage of Multi-Gender Identity Participants:**
```sql
SELECT DATE, MAX(Multi_Gender_Identity_Percentage) AS MaxPercentage 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# View 8
st.markdown("""
**Calculate the Overall Percentage of Participants who do not understand the question:**
```sql
SELECT AVG(Do_not_understand_the_question_Percentage) AS OverallPercentage 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")

# View 9
st.markdown("""
**Retrieve the Top 5 dates with the Highest Total Participants:**
```sql
SELECT DATE, SUM(Black_or_African_American_Count + Multi_race_Count + White_or_Caucasian_Count) AS TotalParticipants 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE 
GROUP BY DATE 
ORDER BY TotalParticipants DESC 
LIMIT 5;
```""")

# View 10
st.markdown("""
**Find the Zip Code with the Highest Percentage of Two-Spirit Native American/First Nations Participants:**
```sql
SELECT ZIP_CODE, MAX(TWO_SPIRIT_NATIVE_AMERICAN_FIRST_NATIONS_PERCENTAGE) AS MaxPercentage 
FROM DYCD_PARTICIPANT_DEMOGRAPHIC_STATISTICS_BY_ZIP_CODE;
```""")


st.subheader('Business Needs')

business_needs = """

**Diversity and Inclusion Monitoring**: 

Monitor the distribution of participants across different racial and ethnic groups to assess the organization's diversity. 

Track gender distribution and identify opportunities for promoting gender inclusivity.  

**Community Engagement**: 

Understand the demographic makeup of participants within specific ZIP codes to tailor community engagement efforts. 

Identify areas with diverse populations for targeted outreach and program development. 

**Program Effectiveness**: 

Evaluate the impact of programs on specific demographic groups by analyzing changes in participant demographics over time. 

Assess whether programs are reaching a diverse set of participants as intended. 

**Resource Allocation**: 

Allocate resources based on the demographic needs of specific ZIP codes, ensuring that programs are appropriately tailored to the communities they serve. 

Identify areas with a high concentration of participants who declined to answer or do not understand the questions for targeted outreach and support. 

**Informed Decision-Making**: 

Make informed decisions about program development, outreach strategies, and resource allocation based on a comprehensive understanding of participant demographics. 

Adjust programs and services to better meet the needs of specific demographic groups. 

**Compliance and Reporting**: 

Fulfill reporting requirements related to diversity and inclusion metrics for regulatory compliance. 

Generate reports on participant demographics to share with stakeholders, funders, or regulatory bodies. 

**Trend Analysis**: 

Analyze trends in participant demographics over time to identify patterns or shifts in the community. 

Investigate variations in responses to questions about gender identity or understanding to inform educational or communication strategies. 

**Engagement with Underrepresented Groups**: 

Identify ZIP codes with a lower representation of certain demographic groups and develop strategies to increase engagement with those groups. 

Tailor marketing and outreach efforts to resonate with underrepresented communities. 

**Customer or Participant Satisfaction**: 

Assess participant satisfaction by analyzing responses related to understanding questions and satisfaction with the survey process. 

Use feedback to improve survey instruments and the overall participant experience. 

**Benchmarking**: 

Compare the demographic statistics with industry benchmarks or regional averages to assess the organization's performance in terms of diversity and inclusion. 

"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- DYCD DEMOGRAPHIC STATISTICS 
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- DATE
- ZIP CODE
- BLACK OR AFRICAN AMERICAN COUNT
- BLACK OR AFRICAN AMERICAN PERCENTAGE
- MULTI RACE COUNT
- MULTI RACE PERCENTAGE
- WHITE OR CAUCASIAN COUNT
- WHITE OR CAUCASIAN PERCENTAGE
- HISPANIC OR LATINX COUNT
- HISPANIC OR LATINX PERCENTAGE
- NOT HISPANIC OR LATINX COUNT
- NOT HISPANIC OR LATINX PERCENTAGE
- NOT SURE COUNT
- NOT SURE PERCENTAGE
- X NOT MALE OR FEMALE COUNT
- X NOT MALE OR FEMALE PERCENTAGE
- ANOTHER GENDER COUNT
- ANOTHER GENDER PERCENTAGE
- DECLINE TO ANSWER COUNT 
- DECLINE TO ANSWER PERCENTAGE
- DO NOT UNDERSTAND THE QUESTION COUNT
- DO NOT UNDERSTAND THE QUESTION PERCENTAGE
- FEMALE GENDER IDENTITY COUNT
- FEMALE GENDER IDENTITY PERCENTAGE
- MALE GENDER IDENTITY COUNT
- MALE GENDER IDENTITY PERCENTAGE
- MULTI GENDER IDENTITY COUNT
- MULTI GENDER IDENTITY PERCENTAGE
- NON BINARY NOT FEMALE OR MALE COUNT
- NON BINARY NOT FEMALE OR MALE PERCENTAGE
- NOT SURE GENDER IDENTITY COUNT
- NOT SURE GENDER IDENTITY PERCENTAGE
- TWO SPIRIT NATIVE AMERICAN FIRST NATIONS COUNT
- TWO SPIRIT NATIVE AMERICAN FIRST NATIONS PERCENTAGE
- MIDDLE EASTERN AND NORTH AFRICAN COUNT
- MIDDLE EASTERN AND NORTH AFRICAN PERCENTAGE
- OTHER COUNT
- OTHER PERCENTAGE 
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



