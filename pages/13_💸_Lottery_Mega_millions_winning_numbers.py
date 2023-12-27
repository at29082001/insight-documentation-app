import streamlit as st


st.set_page_config(page_title="Lottery Mega Millions Winning Numbers", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Lottery Mega Millions Winning Numbers 💸")

# Image
st.image("pages/image/lottery.jpeg", width=700)

# Text to be displayed in the blue box
info_text = """
LOTTERY MEGA MILLIONS WINNING NUMBERS dataset contains information about the winning numbers and details from the Mega Millions lottery draws. 
This dataset provides a historical record of Mega Millions lottery draws, allowing for analysis and insights into patterns, frequency of winning numbers, distribution of Mega Ball numbers, and the impact of the multiplier on prize amounts. By querying this dataset, one can uncover trends, popular numbers, and other statistical insights that may be useful for understanding the Mega Millions lottery's dynamics and for making informed decisions related to the lottery's outcomes.    
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
    st.write("This column represents date of the lottery draw when the winning numbers were selected. ")
    
# Create an expandable box
with st.expander("**WINNING NUMBERS** 💡"):
    # Content inside the expandable box
    st.write("This column represents numbers drawn as the winning combination for the respective draw. This column likely stores an array of integers representing the winning numbers. ")
    
# Create an expandable box
with st.expander("**MEGA BALL** 💡"):
    # Content inside the expandable box
    st.write("This column represents mega Ball number drawn for the respective draw. The Mega Ball is a separate number drawn from a different pool of numbers.")
    
# Create an expandable box
with st.expander("**MULTIPLIER** 💡"):
    # Content inside the expandable box
    st.write("This column represents multiplier applied to the winnings, which could enhance the prize amount in case of certain combinations.")
 


# SQL Queries section
st.subheader('SQL Queries')

# View 1
st.markdown("""
**Find winning numbers for a specific draw date:**
```sql
SELECT WINNING_NUMBERS, MEGA_BALL, MULTIPLIER 
FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS 
WHERE DRAW_DATE = '2020-09-25';
```""")

# View 2
st.markdown("""
**Winning Numbers with high Multipliers:**
```sql
SELECT DRAW_DATE, WINNING_NUMBERS, MEGA_BALL, MULTIPLIER 
FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS 
WHERE MULTIPLIER > 2;
```""")

# View 3
st.markdown("""
**Common Mega Ball Numbers:**
```sql
SELECT MEGA_BALL, COUNT(*) AS Frequency 
FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS 
GROUP BY MEGA_BALL 
ORDER BY Frequency DESC;
```""")

# View 4
st.markdown("""
**Average Multiplier Applied:**
```sql
SELECT AVG(MULTIPLIER) AS Average_Multiplier 
FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS;
```""")

# View 5
st.markdown("""
**Highest Multiplier Recorded:**
```sql
SELECT MAX(MULTIPLIER) AS Highest_Multiplier 
FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS;
```""")

# View 6
st.markdown("""
**Draw Dates with Jackpot Win:**
```sql
SELECT DRAW_DATE, WINNING_NUMBERS, MULTIPLIER 
FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS 
WHERE MEGA_BALL = 25;
```""")

# View 7
st.markdown("""
**Largest Jackpot Multiplier:**
```sql
SELECT DRAW_DATE, WINNING_NUMBERS, MULTIPLIER 
FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS 
WHERE MULTIPLIER = (
    SELECT MAX(MULTIPLIER) 
    FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS 
) AND MEGA_BALL = 25;
```""")

# View 8
st.markdown("""
**Top Multipliers by Draw Date:**
```sql
SELECT DRAW_DATE, WINNING_NUMBERS, MEGA_BALL, MULTIPLIER 
FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS  
WHERE MULTIPLIER = (
    SELECT MAX(MULTIPLIER) 
    FROM LOTTERY_MEGA_MILLIONS_WINNING_NUMBERS lm 
    WHERE DRAW_DATE = lm.DRAW_DATE 
);
```""")

st.subheader('Business Needs')

business_needs = """

**Pattern Analysis**:  

Analyze historical winning numbers to identify any patterns or trends that might provide insights into potential future winning combinations. Businesses or individuals interested in playing the lottery could use this analysis to make informed number selections.  

**Frequency Analysis**:  

Determine the frequency of each winning number and Mega Ball number across draws. This information can help players understand which numbers are drawn more often, potentially guiding their number choices.  

**Multiplier Impact**:  

Study the impact of the multiplier on prize amounts over time. This analysis can help players and lottery enthusiasts understand how the multiplier affects potential winnings.  

**Promotional Campaigns**:  

Lottery operators or organizations may use the dataset to identify popular or lucky numbers for promotional campaigns, potentially increasing ticket sales. 

**Player Insights**:  

Understand player preferences and behaviors by analyzing which winning numbers and Mega Ball numbers players tend to choose. This information could inform marketing strategies and tailor promotions.  

**Strategic Planning**:  

For lottery operators, analyzing winning number distribution and prize amounts can inform strategic planning, such as adjusting prize structures or launching new games.  

**Research and Reporting**:  

Researchers and journalists can use the dataset to study lottery outcomes, trends, and the impact of the multiplier on winnings. This can lead to insightful reports and articles.  

**Educational Purposes**:  

The dataset can be used in educational settings to teach statistical analysis, probability, and data interpretation using real-world examples. 

**Data Visualization**:  

Create visually appealing dashboards and visualizations to present winning number patterns, frequency distributions, and other insights to a wider audience. 

**Data Quality Assessment**:  

For lottery regulators, auditing organizations, or data analysts, comparing the dataset with official records can help ensure data accuracy and regulatory compliance. 


"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- LOTTERY WINNING   
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- DRAW DATE  
- WINNING NUMBERS  
- MEGA BALL  
- MULTIPLIER 



""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



