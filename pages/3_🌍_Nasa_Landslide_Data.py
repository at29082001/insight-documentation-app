import streamlit as st


st.set_page_config(page_title="Nasa Landslide Data", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Nasa Landslide Data 🌍")

# Image
st.image("pages/image/nasa.jpg", width=700)

# Text to be displayed in the blue box
info_text = """
The "Global Landslide" dataset captures crucial information about landslides worldwide, offering a comprehensive view of events that have shaped landscapes and communities. It includes details such as event dates, locations, triggers, sizes, and the associated impact on human life and infrastructure. This dataset proves invaluable for researchers, emergency services, environmental agencies, and businesses, providing insights into the patterns and causes of landslides. By studying this data, stakeholders can enhance disaster preparedness, inform infrastructure planning, and contribute to the understanding of geological phenomena, fostering safer and more resilient environments globally.
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)

# Datasets section
st.subheader('Datasets')

# Create an expandable box
with st.expander("**Global Landslide Data** 💡"):
    # Content inside the expandable box
    st.write("The dataset that documents instances of landslides worldwide over the specified period. Landslides are geological events characterized by the movement of rock, soil, and debris down a slope. This dataset likely includes information about the location, date, and characteristics of landslides that occurred across the globe between 1988 and 2017.")
    


# SQL Queries section
st.subheader('SQL Queries')

# Query 1
st.markdown("""
**Count the number of landslide events per country:**
```sql
SELECT 
    country_name, 
    COUNT(*) AS event_count 
FROM vw_global_landslide 
GROUP BY country_name 
ORDER BY event_count DESC; 
```""")

# Query 2
st.markdown("""
**Find the countries with the highest fatality count:**
```sql
SELECT 
    country_name, 
    SUM(fatality_count) AS total_fatalities 
FROM vw_global_landslide 
GROUP BY country_name 
HAVING total_fatalities IS NOT NULL 
ORDER BY total_fatalities DESC; 
```""")

# Query 3
st.markdown("""
**Identify the most common landslide trigger:**
```sql
SELECT 
    landslide_trigger, 
    COUNT(*) AS trigger_count 
FROM vw_global_landslide 
GROUP BY landslide_trigger 
ORDER BY trigger_count DESC; 
```""")

# Query 4
st.markdown("""
**Rows with both fatality and injury count greater than 0:**
```sql
SELECT * 
FROM vw_global_landslide 
WHERE fatality_count > 0 AND injury_count > 0;
```""")

# Query 5
st.markdown("""
**Average fatalities per landslide category:**
```sql
SELECT 
    landslide_category, 
    AVG(fatality_count) AS avg_fatalities 
FROM vw_global_landslide 
GROUP BY landslide_category 
ORDER BY avg_fatalities DESC; 
```""")

# Query 6
st.markdown("""
**Select rows based on date range:**
```sql
SELECT * 
FROM vw_global_landslide 
WHERE event_date BETWEEN 'start_date' AND 'end_date';
```""")

st.subheader('Business Needs')

business_needs = """

**Insurance Companies**: Insurance companies can use landslide data to assess the risk of property damage due to landslides, allowing them to adjust insurance premiums accordingly. 

**Construction Companies**: Companies involved in construction and infrastructure development can use landslide data to assess and mitigate the risk of landslides in their projects. 

**Environmental Agencies**: Government and non-governmental environmental agencies can use landslide data for environmental monitoring and assessment. This includes studying the impact of landslides on ecosystems and developing strategies for conservation. 

**Emergency Services**: Landslide data can be crucial for emergency services to plan and execute effective disaster response efforts, including evacuation procedures and resource allocation. 

**Government Agencies**: Government agencies responsible for disaster management can use landslide data for risk modeling, preparedness planning, and post-disaster recovery. 

**Researchers and Scientists**: Landslide datasets are valuable for researchers and scientists studying geology, climatology, and environmental science. They contribute to the understanding of landslide triggers, patterns, and impacts. 

**Urban Planning**: City planners and developers can use landslide data to make informed decisions about where to build infrastructure, avoiding areas prone to landslides. 

**Transportation Planning**: Landslide data can inform the planning and maintenance of roads, highways, and other transportation infrastructure to minimize the risk of disruptions. 

**Real Estate Developers**: Developers can use landslide data to assess the suitability of land for real estate projects, ensuring the safety and stability of structures. 

**Claims Adjusters**: Landslide data can be used by claims adjusters to assess the validity of insurance claims related to property damage caused by landslides. 

**Educational Institutions**: Landslide datasets can be valuable teaching tools in educational institutions for courses related to geoscience, geography, and environmental studies. 

**Public Awareness Campaigns**: Public awareness campaigns about landslide-prone areas and safety measures can benefit from accurate and up-to-date landslide data. 
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- GLOBAL LANDSLIDE 
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- SOURCE NAME
- SOURCE LINK
- EVENT ID
- EVENT DATE
- EVENT TITLE
- EVENT DESCRIPTION
- LOCATION DESCRIPTION
- LOCATION ACCURACY
- LANDSLIDE CATEGORY
- LANDSLIDE TRIGGER
- LANDSLIDE SIZE
- LANDSLIDE SETTING
- FATALITY COUNT
- INJURY COUNT
- COUNTRY NAME
- COUNTRY CODE
- ADMIN DIVISION NAME
- ADMIN DIVISION POPULATION
- GAZETEER CLOSEST POINT
- GAZETEER DISTANCE
- SUBMITTED DATE
- CREATED DATE
- LAST EDITED DATE
- LONGITUDE
- LATITUDE
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")
