import streamlit as st
import pandas as pd
import uuid
import os

def start_new_game():
    game_id = str(uuid.uuid4())
    st.write(f"Game ID: {game_id}")
    with st.form("new_game_form"):
        # Input for the number of players
        num_players = st.number_input("Number of Players", min_value=2, max_value=8, step=1)
        submit = st.form_submit_button("Start Game")
    players = []
    for i in range(int(num_players)):
        player_name = st.text_input(f"Enter name for Player {i+1}", f"Player {i+1}")
        players.append(player_name)
    submit = st.form_submit_button("Start Game")
    

def new_game():
    st.title("Continental Card Game")
    if st.button("Start New Game"):
            start_new_game()


