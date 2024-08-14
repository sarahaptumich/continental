import streamlit as st
import pandas as pd
import uuid
import os

def start_new_game():
    game_id = str(uuid.uuid4())
    st.write(f"Game ID: {game_id}")
    

def new_game():
    st.title("Continental Card Game")
    if st.button("Start New Game"):
            start_new_game()


