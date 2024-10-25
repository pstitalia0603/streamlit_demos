import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 TESTING APP')

st.write('Hello world!')


with st.sidebar:
    st.header("About App")
    st.write("This is my first app")

st.title("Hello World")

st.write("Hello world again!")

st.header("This is a header with a divider", divider="rainbow")

st.markdown("This is created using st.markdown")

st.subheader("st.column")
col1, col2 = st.columns(2)

with col1:
    x = st.slider("choose an x value", 1, 10)
with col2:
    st.write("The value of :red[***x***] is: ", x)

st.subheader("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
