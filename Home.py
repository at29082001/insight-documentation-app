import streamlit as st

st.set_page_config(
    page_title="InSights",
    page_icon="pages/image/logo.png"
)


# Add an image in the same row
st.image("pages/image/logo.png", width=80) 
# st.image("pages/img112.png", width=100) 
st.write("# Welcome to InSights Data! 👋")

st.sidebar.success("Select a documentations above.")

st.markdown(
    """
   Welcome to InSights, the pinnacle of global decision-making data by CG Infinity. 
  Our cutting-edge data technology solutions compress data discovery to insights, saving time, effort, and budget. 
  Empower individuals and enterprises to explore, visualize, model, and present data for informed decisions and better business outcomes. 
  Revolutionize your world with InSights!
"""
)