import streamlit
streamlit.title( ' My Parents new healthy Dinner')
streamlit.header (' breakfast menu ')
streamlit.text ('🥣 Omega3 & blue berry oatmeal')
streamlit.text ('🥗 Kale, Spinach and Rocket smoothy')
streamlit.text ('🐔 Hard-Boiled free -range Egg')
streamlit.text ('🥑 🍞 Avocado Toast')

streamlit.header ('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
              
