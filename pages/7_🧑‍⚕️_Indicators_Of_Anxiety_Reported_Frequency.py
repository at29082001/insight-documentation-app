import streamlit as st


st.set_page_config(page_title="Indicators Of Anxiety Or Depression Reported Frequency", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Indicators Of Anxiety Or Depression Reported Frequency 🧑‍⚕️")

# Image
st.image("pages/image/depression.png", width=700)

# Text to be displayed in the blue box
info_text = """
The dataset INDICATORS OF ANXIETY OR DEPRESSION contains information related to mental health indicators. The dataset seems to include both categorical data 
(e.g., gender identities, ethnicities) and numerical data (e.g., counts, percentages). Columns like LOW CI, HIGH CI and CONFIDENCE INTERVAL indicate that the dataset might 
include statistical information, possibly confidence intervals associated with reported values.    
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)



# SQL Queries section
st.subheader('SQL Queries')

# Query 1
st.markdown("""
**Aggregate Data by Indicator and Calculate Average Value:**
```sql
SELECT INDICATOR, AVG(VALUE) AS AVG_VALUE  
FROM INDICATORS_OF_ANXIETY_OR_DEPRESSION_REPORTED_FREQUENCY_BY_FEDERAL_GOVERNMENT 
GROUP BY INDICATOR;
```""")

# Query 2
st.markdown("""
**Find Maximum Value and Corresponding Indicator:**
```sql
SELECT INDICATOR, MAX(VALUE) AS MAX_VALUE 
FROM INDICATORS_OF_ANXIETY_OR_DEPRESSION_REPORTED_FREQUENCY_BY_FEDERAL_GOVERNMENT;
```""")

# Query 3
st.markdown("""
**Calculate Confidence Interval Range:**
```sql
SELECT INDICATOR, VALUE, LOW_CI, HIGH_CI, (HIGH_CI - LOW_CI) AS CONFIDENCE_INTERVAL_RANGE 
FROM INDICATORS_OF_ANXIETY_OR_DEPRESSION_REPORTED_FREQUENCY_BY_FEDERAL_GOVERNMENT;
```""")

# Query 4
st.markdown("""
**Filter Data by Time Period Range:**
```sql
SELECT * 
FROM INDICATORS_OF_ANXIETY_OR_DEPRESSION_REPORTED_FREQUENCY_BY_FEDERAL_GOVERNMENT 
WHERE TIME_PERIOD_START_DATE >= 'Start_Date' AND TIME_PERIOD_END_DATE <= 'End_Date';
```""")

# Query 5
st.markdown("""
**Calculate Average Value and Confidence Interval by Indicator:**
```sql
SELECT INDICATOR, AVG(VALUE) AS AVG_VALUE, AVG(LOW_CI) AS AVG_LOW_CI, AVG(HIGH_CI) AS AVG_HIGH_CI 
FROM INDICATORS_OF_ANXIETY_OR_DEPRESSION_REPORTED_FREQUENCY_BY_FEDERAL_GOVERNMENT 
GROUP BY INDICATOR;
```""")

# Query 6
st.markdown("""
**Count the Number of Records per Time Period:**
```sql
SELECT TIME_PERIOD, COUNT(*) AS RECORD_COUNT 
FROM INDICATORS_OF_ANXIETY_OR_DEPRESSION_REPORTED_FREQUENCY_BY_FEDERAL_GOVERNMENT 
GROUP BY TIME_PERIOD;
```""")

# Query 7
st.markdown("""
**Identify Subgroups with the Highest Average Value:**
```sql
SELECT SUBGROUP, AVG(VALUE) AS AVG_VALUE 
FROM INDICATORS_OF_ANXIETY_OR_DEPRESSION_REPORTED_FREQUENCY_BY_FEDERAL_GOVERNMENT 
GROUP BY SUBGROUP 
ORDER BY AVG_VALUE DESC;
```""")

# Query 8
st.markdown("""
**Calculate the Average Confidence Interval Length by Phase:**
```sql
SELECT PHASE, AVG(HIGH_CI - LOW_CI) AS AVG_CONFIDENCE_INTERVAL_LENGTH 
FROM INDICATORS_OF_ANXIETY_OR_DEPRESSION_REPORTED_FREQUENCY_BY_FEDERAL_GOVERNMENT 
GROUP BY PHASE;
```""")




# Datasets section
st.subheader('Datasets Include')

# Create an expandable box
with st.expander("**INDICATOR** 💡"):
    # Content inside the expandable box
    st.write("Represents the type or category of the reported frequency, possibly related to indicators of anxiety or depression.")
    
# Create an expandable box
with st.expander("**GROUP BY** 💡"):
    # Content inside the expandable box
    st.write("Indicates a grouping or categorization for the reported frequency.")
    
# Create an expandable box
with st.expander("**STATE** 💡"):
    # Content inside the expandable box
    st.write("Refers to the geographical state associated with the reported frequency.")
    
# Create an expandable box
with st.expander("**SUBGROUP** 💡"):
    # Content inside the expandable box
    st.write("Denotes a subset or subcategory within the broader grouping.")
    
# Create an expandable box
with st.expander("**PHASE** 💡"):
    # Content inside the expandable box
    st.write("Represents a phase or stage related to the reported frequency. ")
    
# Create an expandable box
with st.expander("**TIME PERIOD** 💡"):
    # Content inside the expandable box
    st.write("Specifies a time period associated with the reported frequency. ")
    
# Create an expandable box
with st.expander("**TIME PERIOD LABEL** 💡"):
    # Content inside the expandable box
    st.write("Describes the label or name associated with the time period.")
    
# Create an expandable box
with st.expander("**TIME_PERIOD_START_DATE** 💡"):
    # Content inside the expandable box
    st.write("Indicates the start date of the time period.")
    
# Create an expandable box
with st.expander("**TIME_PERIOD_END_DATE** 💡"):
    # Content inside the expandable box
    st.write("Indicates the end date of the time period.")
    
# Create an expandable box
with st.expander("**VALUE** 💡"):
    # Content inside the expandable box
    st.write("Represents the reported frequency or numerical value associated with the indicator.")
    
# Create an expandable box
with st.expander("**LOW CI** 💡"):
    # Content inside the expandable box
    st.write("Represents the lower bound of the confidence interval associated with the reported frequency.")
    
# Create an expandable box
with st.expander("**HIGH CI** 💡"):
    # Content inside the expandable box
    st.write("Represents the upper bound of the confidence interval associated with the reported frequency.")
    
# Create an expandable box
with st.expander("**CONFIDENCE INTERVAL** 💡"):
    # Content inside the expandable box
    st.write("Indicates the overall confidence interval for the reported frequency. ")
    
# Create an expandable box
with st.expander("**QUARTILE RANGE** 💡"):
    # Content inside the expandable box
    st.write(" Represents the range between quartiles, providing a measure of the spread of the reported frequency.")
    






st.subheader('Business Needs')

business_needs = """

**Demographic Analysis**: 
The view appears to contain demographic statistics, which could be valuable for businesses or organizations interested in analyzing and understanding the composition of populations based on various characteristics.  

**Healthcare Planning**: 
If the indicators are related to mental health or well-being, the view might be used in the healthcare sector for planning and resource allocation. 

**Government Reporting**: 
The inclusion of state and federal government-related columns suggests that the view may be used for reporting to government agencies, compliance, or public health assessments.  

**Trend Analysis**: 
The time-related columns (TIME_PERIOD, TIME_PERIOD_START_DATE, TIME_PERIOD_END_DATE) suggest the potential for trend analysis over specific periods, helping businesses identify patterns and changes.  

**Public Policy Decision-Making**: 
Demographic and health-related data can be crucial for informing public policies, especially in areas related to mental health, well-being, and healthcare. 

**Resource Allocation**: 
Understanding demographic and health-related indicators by state and subgroup can assist in the allocation of resources, especially in regions with specific needs. 

**Performance Monitoring**: 
Organizations may use the view to monitor the performance of interventions, programs, or policies aimed at improving mental health or related outcomes. 

**Comparative Analysis**: 
Businesses or government agencies may use the view to compare demographic and health indicators across different states, subgroups, or time periods. 

**Decision Support**: 
Stakeholders in health-related organizations may use this view to support decision-making processes, whether in program planning or policy development. 
"""


# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- INDICATORS OF ANXIETY REPORTED FREQUENCY  
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- INDICATOR 
- GROUP BY 
- STATE 
- SUBGROUP 
- PHASE 
- TIME PERIOD 
- TIME PERIOD LABEL 
- TIME PERIOD START DATE  
- TIME PERIOD END DATE 
- VALUE 
- LOW CI 
- HIGH CI 
- CONFIDENCE INTERVAL 
- QUARTILE RANGE 
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")




















