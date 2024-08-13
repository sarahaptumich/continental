import streamlit as st
from st_pages import Page, show_pages, add_page_title
import pandas as pd
import numpy as np

#add_page_title()

show_pages(
    [
        Page(r'main.py', "Home"),
        Page(r'rules.py', "Rules"),
        Page(r'new_game.py', "New Game"),
        Page(r'stats.py', "Statistics"),
    ]
)

st.title('Welcome to Continental!')
st.divider()
st.subheader('The ultimate card game')
st.write('Get ready to play the ultimate card game experience. Navigate through the menu to read the rules, start a new game, or view your stats!')
st.image('continental_logo.png')

st.sidebar.markdown("What is Continental")
st.sidebar.image('continental_logo.png', use_column_width=True)
st.sidebar.write('Continental is a fun family friendly \\
                  card game that can be enjoy by the entire family. This site will explain how to play and can also serve to keep track of games.   ')
