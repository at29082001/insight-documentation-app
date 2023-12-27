import streamlit as st


st.set_page_config(page_title="Indicators of Health Insurance Coverage", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Indicators of Health Insurance Coverage 🏥")

# Image
st.image("pages/image/health-insurance.jpg", width=700)

# Text to be displayed in the blue box
info_text = """
The dataset INDICATORS OF HEALTH INSURANCE COVERAGE BY FEDERAL GOVERNMENT provides insights into various indicators related to health insurance coverage, as reported by the Federal Government. The indicators encompass a range of factors, including different demographic subgroups, states, 
and time periods.   
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)

# Datasets section
st.subheader('Key Features')

# Create an expandable box
with st.expander("**Dynamic Indicators** 💡"):
    # Content inside the expandable box
    st.write("The dataset captures a dynamic range of health insurance indicators, reflecting the evolving landscape of coverage-related factors.")
    
# Create an expandable box
with st.expander("**Temporal Dimension** 💡"):
    # Content inside the expandable box
    st.write("With a temporal dimension, analysts can delve into trends over time, identifying patterns, fluctuations, and potential long-term impacts of policy changes.")
    
# Create an expandable box
with st.expander("**Demographic Insights** 💡"):
    # Content inside the expandable box
    st.write("The inclusion of subgroup data allows for a closer examination of how health insurance coverage varies among different demographic categories within each state.")
    
# Create an expandable box
with st.expander("**Data Quality Assurance** 💡"):
    # Content inside the expandable box
    st.write("The dataset incorporates confidence intervals and suppression flags, enabling users to gauge the reliability of reported values and identify instances where data may be suppressed due to privacy concerns.")
    


# SQL Queries section
st.subheader('SQL Queries')

# Query 1
st.markdown("""
**Calculate Average Health Insurance coverage value by Subgroup:**
```sql
SELECT SUBGROUP, AVG(VALUE) AS AVG_COVERAGE 
FROM INDICATORS_OF_HEALTH_INSURANCE_COVERAGE_BY_FEDERAL_GOVERNMENT 
GROUP BY SUBGROUP;
```""")

# Query 2
st.markdown("""
**Identify Subgroups with the Lowest Health Insurance Coverage:**
```sql
SELECT SUBGROUP, MIN(VALUE) AS MIN_COVERAGE 
FROM INDICATORS_OF_HEALTH_INSURANCE_COVERAGE_BY_FEDERAL_GOVERNMENT 
GROUP BY SUBGROUP 
ORDER BY MIN_COVERAGE;
```""")

# Query 3
st.markdown("""
**Identify States with the Highest Health Insurance Coverage:**
```sql
SELECT STATE, MAX(VALUE) AS MAX_COVERAGE 
FROM INDICATORS_OF_HEALTH_INSURANCE_COVERAGE_BY_FEDERAL_GOVERNMENT 
GROUP BY STATE 
ORDER BY MAX_COVERAGE DESC;
```""")

# Query 4
st.markdown("""
**Calculate the Median Health Insurance Coverage for Each Subgroup:**
```sql
SELECT SUBGROUP, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY VALUE) AS MEDIAN_COVERAGE 
FROM INDICATORS_OF_HEALTH_INSURANCE_COVERAGE_BY_FEDERAL_GOVERNMENT 
GROUP BY SUBGROUP;
```""")

# Query 5
st.markdown("""
**Average Confidence Interval Length:**
```sql
SELECT AVG(HIGH_CI - LOW_CI) AS AVG_CI_LENGTH 
FROM INDICATORS_OF_HEALTH_INSURANCE_COVERAGE_BY_FEDERAL_GOVERNMENT;
```""")

# Query 6
st.markdown("""
**Percentage of Suppressed Data Points:**
```sql
SELECT 
    TIME_PERIOD, 
    (SUM(CASE WHEN SUPPRESSION_FLAG = 'Y' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS PERCENT_SUPPRESSED 
FROM INDICATORS_OF_HEALTH_INSURANCE_COVERAGE_BY_FEDERAL_GOVERNMENT 
GROUP BY TIME_PERIOD;
```""")

st.subheader('Business Needs')

business_needs = """

**Monitoring Health Insurance Coverage Trends**: 
Track changes in health insurance coverage over time to identify trends and patterns.  

**Regional Disparities Analysis**: 
Assess health insurance coverage disparities across different states and regions.  

**Subgroup-Specific Insights**: 
Understand how health insurance coverage varies among different demographic subgroups within states. 

**Policy Evaluation**: 
Evaluate the effectiveness of health insurance policies and initiatives at the state and subgroup levels. 

**Identifying Vulnerable Populations**: 
Identify subgroups or states with lower health insurance coverage, helping target interventions for vulnerable populations. 

**Quality Improvement**: 
Use confidence intervals to assess the reliability of reported values and identify areas for data quality improvement. 

**Suppression Flag Analysis**: 
Investigate and understand the reasons for data suppression, addressing potential privacy concerns or data limitations. 

**Comparative Analysis**: 
Compare health insurance coverage across different phases, time periods, or subgroups to derive insights into the impact of specific factors. 

**Forecasting and Planning**: 
Use historical data to forecast future health insurance coverage trends and plan interventions accordingly. 

**Performance Metrics for Healthcare Systems**: 
Use the indicators as performance metrics for healthcare systems, evaluating their success in providing insurance coverage. 

**Regulatory Compliance**: 
Ensure compliance with federal reporting requirements related to health insurance coverage data. 

**Identifying Outliers**: 
Detect outliers in the data that may indicate unusual or unexpected changes in health insurance coverage. 

**Benchmarking**: 
Benchmark health insurance coverage metrics against industry or national standards to assess performance. 

**Public Health Research**: 
Support public health research by providing granular data on health insurance coverage for various demographic groups. 

**Strategic Planning**: 
Inform strategic planning for government agencies, healthcare providers, and policymakers to improve overall health outcomes. 
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- HEALTH INSURANCE COVERAGE  
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
- QUARTILE NUMBER 
- SUPPRESSION FLAG 
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



