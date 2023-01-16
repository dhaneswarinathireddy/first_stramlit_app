import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My family new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text(':bowl_with_spoon: Omega 3 & Blueberries Oatmeal')
streamlit.text(':green_salad: Kale, Spinach & Rocket Smoothie')
streamlit.text(':chicken: Hard-Boiled Free-range Egg')
streamlit.text(':avocado::bread: Avacado Toast')
streamlit.header(':banana::mango: Build Your Own Fruit Smoothie :kiwifruit::grapes:')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return (fruityvice_normalized)
#New scetion
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe (back_from_function)
except URLError as e:
  streamlit.error()
streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()
