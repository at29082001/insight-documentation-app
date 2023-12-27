import streamlit as st


st.set_page_config(page_title="Lottery NY Lotto Winning Numbers", page_icon="pages/image/logo.png")

# Add a title
st.markdown("# Lottery NY Lotto Winning Numbers 💸")

# Image
st.image("pages/image/lottery.jpeg", width=700)

# Text to be displayed in the blue box
info_text = """
The "LOTTERY NY LOTTO WINNING NUMBERS" view appears to provide information related to the winning numbers of the New York Lotto, a lottery game.  
The dataset captures essential information about the outcomes of New York Lotto drawings, including the date of the drawing, the winning number combination, any bonus numbers, and additional details associated with the drawing. This data is valuable for individuals interested in lottery outcomes, including players, regulatory bodies, and organizations involved in lottery operations.    
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
with st.expander("**BONUS** 💡"):
    # Content inside the expandable box
    st.write("This column represents Bonus number drawn in the NY Lotto. The bonus number is an additional number drawn in some lotteries, which can contribute to additional prize categories. ")
 
# Create an expandable box
with st.expander("**EXTRA** 💡"):
    # Content inside the expandable box
    st.write("This column represents Extra information related to the NY Lotto drawing.This column may contain supplementary information or details about the drawing, such as special events or promotions.")
 


# SQL Queries section
st.subheader('SQL Queries')

# View 1
st.markdown("""
**Retrieve All Distinct Winning Numbers:**
```sql
SELECT DISTINCT WINNING_NUMBERS 
FROM LOTTERY_NY_LOTTO_WINNING_NUMBERS;
```""")

# View 2
st.markdown("""
**Count the Occurrences of Each Winning Number:**
```sql
SELECT WINNING_NUMBERS, COUNT(*) AS OCCURRENCES 
FROM LOTTERY_NY_LOTTO_WINNING_NUMBERS 
GROUP BY WINNING_NUMBERS 
ORDER BY OCCURRENCES DESC;
```""")

# View 3
st.markdown("""
**Find Draws with a Specific Bonus Number:**
```sql
SELECT DRAW_DATE, WINNING_NUMBERS, EXTRA 
FROM LOTTERY_NY_LOTTO_WINNING_NUMBERS 
WHERE BONUS = 'desired_bonus';
```""")

# View 4
st.markdown("""
**Retrieve Draws with Extra Information:**
```sql
SELECT DRAW_DATE, WINNING_NUMBERS, BONUS, EXTRA 
FROM LOTTERY_NY_LOTTO_WINNING_NUMBERS 
WHERE EXTRA IS NOT NULL;
```""")

# View 5
st.markdown("""
**Count the Occurrences of Each Bonus Number:**
```sql
SELECT BONUS, COUNT(*) AS OCCURRENCES 
FROM LOTTERY_NY_LOTTO_WINNING_NUMBERS 
GROUP BY BONUS 
ORDER BY OCCURRENCES DESC;
```""")

# View 6
st.markdown("""
**Retrieve Draws Within a Specific Date Range:**
```sql
SELECT * 
FROM LOTTERY_NY_LOTTO_WINNING_NUMBERS 
WHERE DRAW_DATE BETWEEN 'start_date' AND 'end_date';
```""")

# View 7
st.markdown("""
**Find Draws with the Highest Number of Winners:**
```sql
SELECT DRAW_DATE, WINNING_NUMBERS, BONUS, EXTRA 
FROM LOTTERY_NY_LOTTO_WINNING_NUMBERS 
ORDER BY (WINNER_COUNT_COLUMN) DESC 
LIMIT 1;
```""")

st.subheader('Business Needs')

business_needs = """

 

**Winner Verification**: 

- Business Need: Verify winning tickets and determine the prize amount. 

- Use Case: Identify individuals who hold tickets matching the drawn numbers to facilitate prize distribution. 

  

**Analyzing Number Trends**: 

- Business Need: Understand patterns or trends in winning numbers. 

- Use Case: Conduct statistical analysis to identify frequently drawn numbers, helping ticket buyers make informed choices. 

  

**Promotional Campaigns**: 

- Business Need: Promote special events or features associated with specific draws. 

- Use Case: Utilize the "EXTRA" column to highlight special raffles or promotions during certain drawings. 

  

**Performance Evaluation**: 

- Business Need: Evaluate the success of specific draws or bonus features. 

- Use Case: Analyze the impact of introducing bonus numbers on ticket sales and overall engagement. 

  

**Regulatory Compliance**: 

- Business Need: Ensure compliance with lottery regulations and reporting requirements. 

- Use Case: Use the data to generate reports for regulatory authorities, detailing draw outcomes and related information. 

  

**Customer Engagement**: 

- Business Need: Enhance customer engagement and loyalty. 

- Use Case: Leverage winning number data for marketing campaigns, encouraging participation and maintaining interest in the lottery. 

  

**Data-driven Decision Making**: 

- Business Need: Make informed decisions based on historical draw data. 

- Use Case: Analyze past draws to inform decisions about prize structures, bonus features, or promotional activities. 

"""

# Display the text in a blue box with custom styling
st.markdown(
    f'<div style="background-color: #FFDBFC; padding: 20px; border-radius: 10px;">{business_needs}</div>',
    unsafe_allow_html=True,
)


st.subheader('Tables Included')
st.markdown("""
- LOTTERY NY LOTTO  WINNING    
""")

# Fields included section
st.subheader('Fields Included')
st.markdown("""
- DRAW DATE  
- WINNING NUMBERS  
- BONUS 
- EXTRA 
""")

# Closing section
st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



