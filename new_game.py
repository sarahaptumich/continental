import streamlit as st
import uuid

# Function to initialize the game and reset session state variables
def initialize_game():
    st.session_state.game_id = str(uuid.uuid4())  # Generate a unique game ID
    st.session_state.num_players = 0  # Number of players will be set by user
    st.session_state.players = []  # List to store player names
    st.session_state.game_started = False  # Flag to check if the game has started
    st.session_state.current_round = 1  # Start from round 1

# Function to start a new game
def start_new_game():
    # Show the game ID
    st.write(f"Game ID: {st.session_state.game_id}")
    
    # Form to input the number of players
    with st.form("player_count_form"):
        st.session_state.num_players = st.number_input("Number of Players", min_value=2, max_value=8, step=1)
        submit_players_count = st.form_submit_button("Submit Number of Players")
    
    # If the number of players is submitted, initialize the player names list
    if submit_players_count:
        st.session_state.players = [""] * st.session_state.num_players  # Initialize player names
        st.session_state.game_started = False  # Set game started to False to show player name inputs
        st.experimental_rerun()  # Force rerun to show the player name inputs

# Function to input player names
def enter_player_names():
    st.write("### Enter Player Names")
    with st.form("player_names_form"):
        for i in range(st.session_state.num_players):
            st.session_state.players[i] = st.text_input(f"Enter name for Player {i+1}", key=f"player_name_{i+1}")
        submit_player_names = st.form_submit_button("Submit Player Names")
    
    # If player names are submitted, mark the game as started
    if submit_player_names:
        st.session_state.game_started = True  # Set flag to indicate that the game can start
        st.experimental_rerun()  # Force rerun to proceed to the game

# Function to play the game (initial setup)
def play_game():
    st.write("### Game Started")
    st.write(f"Current Round: {st.session_state.current_round}")
    st.write(f"Players: {', '.join(st.session_state.players)}")
    # Add game logic here for each round or other actions

# Main function to control the flow of the game
def new_game():
    st.title("Continental Card Game")
    
    # Check if the game has been initialized; if not, initialize it
    if 'game_id' not in st.session_state:
        initialize_game()

    # If the game is not started and player names have not been entered, ask for the number of players
    if not st.session_state.game_started and not st.session_state.players:
        start_new_game()
    
    # If players have been entered but the game has not started, ask for player names
    elif not st.session_state.game_started and st.session_state.players:
        enter_player_names()

    # If the game has started, begin the game logic
    elif st.session_state.game_started:
        play_game()

if __name__ == "__main__":
    new_game()