import streamlit as st


st.set_page_config(page_title="Warn and Layoff Data", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Warn and Layoff Data 😓")

# Image
st.image("pages/image/warn_layoff.jpeg", width=700)

# Text to be displayed in the blue box
info_text = """
The "WARN Layoff" data typically refers to information related to Worker Adjustment and Retraining Notification Act (WARN Act) layoff notices and layoffs in the United States. The WARN Act requires employers to provide advance notice to their employees, their representatives (e.g., labor unions), and certain government entities before implementing a plant closing or mass layoff. 
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)

# Datasets section
st.subheader('Datasets')

# Create an expandable box
with st.expander("**Warn Layoff by State Dataset** 💡"):
    # Content inside the expandable box
    st.write("The Warn Layoff by State dataset spans from the year 2005 to 2023. This dataset provides information on WARN (Worker Adjustment and Retraining Notification) layoff events across various states. The WARN Act requires employers to provide advance notice of significant layoffs or plant closures, giving affected workers and communities time to prepare for the economic consequences. The dataset likely includes details such as the location, date, and scale of layoffs within each state, offering insights into employment trends and workforce adjustments over the specified time frame.")
    
# Create an expandable box
with st.expander("**Warn Layoff by Company Dataset** 💡"):
    # Content inside the expandable box
    st.write("The Warn Layoff by Company dataset covers the period from 2005 to 2023. This dataset focuses on WARN layoff events categorized by individual companies. It provides information about layoffs and retraining notifications issued by specific companies during this timeframe. Analyzing this dataset can offer a detailed perspective on the labor market impacts of various companies, shedding light on workforce dynamics, economic challenges, and corporate restructuring efforts. The dataset likely includes details such as company names, locations, dates, and the number of affected workers for each WARN event.")
    


# SQL Queries section
st.subheader('SQL Queries')


# Query 1
st.markdown("""
**Retrieve All Columns for a Specific State:**
```sql
SELECT * FROM WARN_LAYOFF_STATE WHERE STATE = 'Your_State_Name';
```""")

# Query 2
st.markdown("""
**Retrieve All Data for a Specific Company:**
```sql
SELECT * FROM WARN_LAYOFF_STATE WHERE COMPANY = 'Company_Name';
```""")

# Query 3
st.markdown("""
**Retrieve Data for a Specific State and City:**
```sql
SELECT * FROM WARN_LAYOFF_STATE WHERE STATE = 'Your_State_Name' AND CITY = 'Your_City_Name';
```""")

# Query 4
st.markdown("""
**Retrieve Data for Companies in a Specific Industry:**
```sql
SELECT * FROM WARN_LAYOFF_STATE WHERE INDUSTRY = 'Your_Industry_Name';
```""")

# Query 5
st.markdown("""
**Retrieve Data with Specific Closure/Layoff Type:**
```sql
SELECT * FROM WARN_LAYOFF_STATE WHERE CLOSURE_OR_LAYOFF = 'Your_Closure_Layoff_Type';
```""")

# Query 6
st.markdown("""
**Retrieve Data for Companies in a Specific County and Union:**
```sql
SELECT * FROM WARN_LAYOFF_STATE WHERE COUNTY = 'Your_County_Name' AND UNION_ = 'Your_Union_Name';
```""")

# Query 7
st.markdown("""
**Retrieve Distinct States from the Table:**
```sql
SELECT DISTINCT STATE FROM WARN_LAYOFF_STATE;
```""")

# Query 8
st.markdown("""
**Count the Number of Records for Each State:**
```sql
SELECT STATE, COUNT(*) AS RECORD_COUNT FROM WARN_LAYOFF_STATE GROUP BY STATE;
```""")


st.subheader('Business Needs')

business_needs = """

 **Workforce Planning**:Analyze WARN data to anticipate workforce changes and plan for potential layoffs, closures, or relocations. 

 

**Compliance Monitoring**:Ensure compliance with labor laws by tracking WARN notices, especially for large-scale layoffs. 

 

**Economic Indicator**: Use layoff data to understand economic trends and labor market conditions, as increased WARN notices can signal economic challenges. 

 

**Impact on Communities**:Assess the potential impact of layoffs and closures on local communities, including unemployment rates and social services needs. 

 

**Strategic Decision-Making**:Make informed decisions regarding expansion, downsizing, and facility closures based on historical and current layoff data. 

 

**Labor Union Negotiations**:Prepare for labor union negotiations and collective bargaining agreements by understanding layoff and worker displacement trends. 

 

**Industry Analysis**:Analyze layoff data by industry to identify sectors that are more prone to layoffs, helping with investment and diversification decisions. 

 

**Geographic Insights**:Understand regional variations in layoffs and closures, which can inform location-specific strategies. 

 

**Talent Acquisition and Retention**:Use layoff data to identify available talent pools and potential hiring opportunities in areas with high layoff rates. 

 

**Supply Chain Impact**:Assess how layoffs in one industry or region may affect supply chains and other related businesses. 

 

**Government Policy Evaluation**:Evaluate the effectiveness of government policies related to workforce support and retraining in response to layoffs. 

 

**Reporting and Disclosure**:Comply with legal requirements for reporting WARN notices and providing timely disclosures to affected employees and stakeholders. 

 

**Predictive Analytics**:Develop predictive models for layoff risk based on historical data to proactively manage workforce changes. 

 

**Workforce Reskilling**:Identify opportunities for reskilling and retraining programs to assist affected workers in transitioning to new roles. 

 

**Employee Assistance Programs**:Design employee assistance programs to support workers who are impacted by layoffs and closures. 

 

**Financial and Budget Planning**:Incorporate layoff data into financial and budget planning to account for potential costs and revenue impacts. 

 

**Competitive Analysis**:Understand how layoffs may affect the competitive landscape and seize opportunities created by competitors' challenges. 

 

**Market Entry and Expansion**:Assess potential markets for entry or expansion based on labor availability and workforce stability. 

 

**Risk Management**:Mitigate risks associated with labor market fluctuations and identify strategies for addressing workforce challenges. 

 

**Investor Relations**:Communicate effectively with investors regarding the potential impact of layoffs on financial performance and corporate strategy.  
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- WARN LAYOFF STATE 
- WARN LAYOFF COMPANY  
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- STATE
- COMPANY
- CITY
- NUMBER OF WORKERS
- WARN RECEIVED DATE
- EFFECTIVE DATE
- CLOSURE OR LAYOFF
- TEMPORARY OR PERMANENT
- REGION
- COUNTY
- INDUSTRY
- NOTES
- ADDRESS
- RECEIVED DATE
- LAYOFF CLOSURE DATE
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



