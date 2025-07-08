import streamlit as st
import pandas as pd
import duckdb
import io

csv = '''
beverage,price
orange juice,2.5
expresso,2
tea,3
'''
beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''
food_items = pd.read_csv(io.StringIO(csv2))

answer ="""
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(answer)


with st.sidebar:
    option = st.selectbox(
        "What do you like to review?",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
        )
    st.write('You selected:', option)


st.header("enter your code")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3= st.tabs(["tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution)

with tab3:
<<<<<<< HEAD
    st.write(answer)
=======
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

>>>>>>> 0f9c35f (code de pierre)
