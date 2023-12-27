import streamlit as st


st.set_page_config(page_title="Lottery Powerball Winning Numbers", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Lottery Powerball Winning Numbers 💸")

# Image
st.image("pages/image/lottery.jpeg", width=700)

# Text to be displayed in the blue box
info_text = """
LOTTERY MEGA MILLIONS WINNING NUMBERS dataset contains information about the Powerball lottery drawings. 
This dataset can be valuable for individuals interested in Powerball lottery outcomes, including players, analysts, or researchers. It enables tracking and analysis of historical winning numbers, drawing dates, and the impact of multipliers on prize amounts. The information may be used for various purposes, such as player engagement, strategic decision-making, and compliance reporting within the context of lottery operations.    
"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
)

# Datasets section
st.subheader('Datasets')

# Create an expandable box
with st.expander("**DRAW DATE** 💡"):
    # Content inside the expandable box
    st.write("This column represents specific date when the Powerball drawing occurred.")
    
# Create an expandable box
with st.expander("**WINNING NUMBERS** 💡"):
    # Content inside the expandable box
    st.write("This column represents numbers drawn as the winning combination for the respective draw. This column likely stores an array of integers representing the winning numbers.")
    
# Create an expandable box
with st.expander("**MULTIPLIER** 💡"):
    # Content inside the expandable box
    st.write(" This column represents multiplier applied to the winnings, which could enhance the prize amount in case of certain combinations.")
 


# SQL Queries section
st.subheader('SQL Queries')

# View 1
st.markdown("""
**Get Powerball Drawings for a Specific Date Range:**
```sql
SELECT * 
FROM LOTTERY_POWERBALL_WINNING_NUMBERS 
WHERE DRAW_DATE BETWEEN 'start_date' AND 'end_date';
```""")

# View 2
st.markdown("""
**Get Unique Winning Numbers:**
```sql
SELECT DISTINCT WINNING_NUMBERS 
FROM LOTTERY_POWERBALL_WINNING_NUMBERS;
```""")

# View 3
st.markdown("""
**Most Common Winning Numbers:**
```sql
SELECT WINNING_NUMBERS, COUNT(*) AS OCCURRENCES 
FROM LOTTERY_POWERBALL_WINNING_NUMBERS 
GROUP BY WINNING_NUMBERS 
ORDER BY OCCURRENCES DESC;
```""")

# View 4
st.markdown("""
**Get Powerball Drawings with Suppressed Information:**
```sql
SELECT * 
FROM LOTTERY_POWERBALL_WINNING_NUMBERS 
WHERE SUPPRESSION_FLAG = 'suppressed';
```""")

# View 5
st.markdown("""
**Powerball Drawings with a Specific Multiplier Range:**
```sql
SELECT * 
FROM LOTTERY_POWERBALL_WINNING_NUMBERS 
WHERE MULTIPLIER BETWEEN 'min_multiplier' AND 'max_multiplier';
```""")

# View 6
st.markdown("""
**Get Powerball Drawings for a Specific Date with Multiplier Applied:**
```sql
SELECT * 
FROM LOTTERY_POWERBALL_WINNING_NUMBERS 
WHERE DRAW_DATE = 'your_date' AND MULTIPLIER IS NOT NULL;
```""")

st.subheader('Business Needs')

business_needs = """

**Player Engagement and Communication**: 

- Business Need: Engage with lottery players by sharing historical Powerball drawing information. 

- Usage: Use the view to communicate past winning numbers, drawing dates, and any applied multipliers to enhance player interest. 

**Winning Patterns Analysis**: 

- Business Need: Understand and analyze winning patterns over time to provide insights to players. 

- Usage: Share statistical analyses and trends regarding frequently drawn numbers or patterns. 

**Promotional Campaigns**: 

- Business Need: Design marketing campaigns to attract more participants. 

- Usage: Utilize historical data to create promotions around special drawing dates or unique winning number combinations. 

**Optimizing Prize Structures**: 

- Business Need: Evaluate the impact of the multiplier on winnings to optimize prize structures. 

- Usage: Analyze how often players choose the multiplier and the resulting impact on prize amounts. 

**Enhancing Transparency**: 

- Business Need: Ensure transparency in lottery operations. 

- Usage: Share historical winning information with the public to build trust and transparency in lottery practices. 

**Player Education**: 

- Business Need: Educate players on the multiplier's role in increasing winnings. 

- Usage: Use the view to provide information on how the multiplier affects the prize amounts. 

**Compliance Reporting**: 

- Business Need: Meet regulatory requirements and provide necessary reports. 

- Usage: Use the view to generate reports that comply with regulations, ensuring accurate and secure data access. 

**Strategic Decision-Making**: 

- Business Need: Enable data-driven decision-making for lottery operations. 

- Usage: Provide insights into player preferences, helping in strategic decisions related to promotions, prizes, and operations. 

**Customer Satisfaction**: 

- Business Need: Enhance customer satisfaction by providing valuable information. 

- Usage: Use the view to answer customer queries about past draws and winning combinations. 

**Security and Compliance**: 

- Business Need: Ensure secure access to sensitive lottery data. 

- Usage: Implement secure views to control access and comply with data protection and privacy regulations. 

"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- LOTTERY POWERBALL WINNING    
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- DRAW DATE  
- WINNING NUMBERS  
- MULTIPLIER 



""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



