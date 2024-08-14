import streamlit as st
import pandas as pd
import uuid
import os

# Initialize a global session state for tracking rounds and scores
if 'round' not in st.session_state:
    st.session_state.round = 1
if 'scores' not in st.session_state:
    st.session_state.scores = {}
if 'game_id' not in st.session_state:
    st.session_state.game_id = None

# Function to start a new game
def start_new_game():
    st.session_state.round = 1
    st.session_state.scores = {}
    st.session_state.game_id = str(uuid.uuid4())
    st.success(f"New game started with Game ID: {st.session_state.game_id}")

# Function to add players and record scores
def new_game():
    st.title("Continental Card Game")
    
    if st.session_state.round == 1:
        # Start a new game
        if st.button("Start New Game"):
            start_new_game()
        
        if st.session_state.game_id:
            st.write(f"Game ID: {st.session_state.game_id}")
            
            # Input fields for Player Names
            num_players = st.number_input("Number of Players", min_value=2, max_value=8, step=1)
            
            if 'players' not in st.session_state:
                st.session_state.players = [st.text_input(f"Enter name for Player {i+1}") for i in range(int(num_players))]
                
            # Button to start entering scores
            if st.button("Proceed to Enter Scores"):
                for player in st.session_state.players:
                    st.session_state.scores[player] = []
                st.session_state.round = 1
    else:
        st.write(f"Entering scores for Game ID: {st.session_state


