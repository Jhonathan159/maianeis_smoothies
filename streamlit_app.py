# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write("""
""")

Name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', Name_on_order)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:',
    my_dataframe,
    max_selections=5
)

if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    # st.write(ingredients_string)

    my_insert_stmt = """INSERT INTO smoothies.public.orders(ingredients, name_on_order)
            VALUES ('""" + ingredients_string + """','""" + Name_on_order + """')"""

    #st.write(my_insert_stmt)
    # Para ejecutar la consulta deberías agregar:
    # session.sql(my_insert_stmt).collect()
    #st.stop()
    time_to_insert = st.button('Submit Order')

    if ingredients_string:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
