import streamlit as st


st.write("Guten Morgen Everyone")
st.header("Guten Morgen Everyone")
st.subheader("Guten Morgen Everyone")
st.caption("Guten Morgen Everyone")
st.success("good")
st.error("error!")
st.warning("bad")
st.info("info")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown(''' :red[Streamlit] :orange[is] :green[fun] ''')
st.markdown("Here's a bouquet &mdash;\ :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">This is advanced font manipulation!</p>'
st.markdown(new_title, unsafe_allow_html=True)

st.selectbox("Kuala Lumpur is located at", ['Malaysia', 'Thailand', 'UK'])
st.multiselect("Select 2 states", ['Selangor','Johor','Kedah'])

c1= st.button("click me")
if c1:
    st.write("you have just clicked the button")
    st.slider("Select the length of stay", 1,10, value=3)

number = st.number_input("insert a number",  value=None, placeholder="Type a number....")



#st.button("Click Here to Proceed")


number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write("The current number is ", number)

#import image
from PIL import Image 
im = Image.open('IMG_1141.JPG')
st.image(im, width=500)

col1, col2, col3 = st.columns(3)
#with col1:
 #st.header("A cat")
 #st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
   im = Image.open('this-is-england-438165 (1).png')
   st.image(im, width=500)
#with col3:
   #st.header("An owl")
   #st.image("https://static.streamlit.io/examples/owl.jpg")

#import data
import pandas as pd
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)

#barchart
#st.bar_chart(df, x="Location", y="Income")

#linechart
#st.line_chart(df, x="Household", y="Income")

#scatter plot
#st.scatter_chart(df, x="Household", y="Income")

#create multi-tabpage
#tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
##with tab1:
    #st.header("A cat")
    #st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
#with tab2:
    #st.header("A dog")
    #st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
#with tab3:
    #st.header("An owl")
    #st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

tab1, tab2, tab3 = st.tabs(["Bar Chart", "Line Chart", "Scatter Plot"])
with tab1:
    st.header("Bar Chart")
    st.bar_chart(df, x="Location", y="Income")
with tab2:
    st.header("Line Chart")
    st.line_chart(df, x="Household", y="Income")
with tab3:
    st.header("Scatter Plot")
    st.scatter_chart(df, x="Household", y="Income")


#create multi-columns
col1, col2, col3 = st.columns(3)
#with col1:
 #st.header("A cat")
 #st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")
#with col3:
   #st.header("An owl")
   #st.image("https://static.streamlit.io/examples/owl.jpg")