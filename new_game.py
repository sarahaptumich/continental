import streamlit as st
import pandas as pd
import uuid
import os

def start_new_game():
    # Generate and save the game_id in session state
    if 'game_id' not in st.session_state:
        st.session_state.game_id = str(uuid.uuid4())
    
    st.write(f"Game ID: {st.session_state.game_id}")
    
    with st.form("new_game_form"):
        # Input for the number of players
        num_players = st.number_input("Number of Players", min_value=2, max_value=8, step=1)
        submit = st.form_submit_button("Enter players names")
    
    # Check if the form was submitted
    if submit:
        # Save the number of players to session state
        st.session_state.num_players = int(num_players)
        
        # Trigger a rerun to show the player name inputs
        st.experimental_rerun()

    # If the number of players has been set, display text inputs for player names
    if 'num_players' in st.session_state:
        st.write("### Enter Player Names")
        st.session_state.players = []
        for i in range(st.session_state.num_players):
            player_name = st.text_input(f"Enter name for Player {i+1}", key=f"player_name_{i+1}")
            st.session_state.players.append(player_name)

        if st.button("Start Game"):
            st.write("Game has started!")
            st.write(f"Players: {', '.join(st.session_state.players)}")

def new_game():
    st.title("Continental Card Game")
    if st.button("Start New Game"):
        start_new_game()

if __name__ == "__main__":
    new_game()



