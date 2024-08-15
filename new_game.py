import streamlit as st
import uuid

# Function to initialize the game and reset session state variables
def initialize_game():
    st.session_state.game_id = str(uuid.uuid4())  # Generate a unique game ID
    st.session_state.num_players = 0  # Number of players will be set by user
    st.session_state.players = []  # List to store player names
    st.session_state.game_started = False  # Flag to check if the game has started
    st.session_state.current_round = 1  # Start from round 1

# Function to start a new game using st.dialog to input the number of players
def start_new_game():
    st.session_state.game_id = str(uuid.uuid4())
    
    # Use a dialog to enter the number of players
    with st.dialog("Enter Number of Players"):
        num_players = st.number_input("Number of Players", min_value=2, max_value=8, step=1)
        submit_players_count = st.button("Submit")
    
    # If the number of players is submitted, initialize the player names list
    if submit_players_count:
        st.session_state.num_players = num_players
        st.session_state.players = [""] * int(num_players)  # Initialize player names
        st.session_state.game_started = False  # Set game started to False to show player name inputs

# Function to input player names using a container
def enter_player_names():
    st.write("### Enter Player Names")
    with st.container():
        with st.form("player_names_form"):
            for i in range(int(st.session_state.num_players)):
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

    # If the game is not started and player names have not been entered, use dialog to ask​⬤