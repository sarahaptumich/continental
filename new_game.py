import streamlit as st
import uuid

def start_new_game():
    # Generate and save the game_id in session state
    if 'game_id' not in st.session_state:
        st.session_state.game_id = str(uuid.uuid4())
    
    st.write(f"Game ID: {st.session_state.game_id}")
    
    # Form to input number of players
    with st.form("new_game_form"):
        num_players = st.number_input("Number of Players", min_value=2, max_value=8, step=1)
        submit = st.form_submit_button("Enter players names")
    
    # If the form is submitted, store the number of players in session state
    if submit:
        st.session_state.num_players = int(num_players)
        st.session_state.players = [""] * st.session_state.num_players  # Initialize empty player names list

def enter_player_names():
    # Display text inputs for player names
    st.write("### Enter Player Names")
    for i in range(st.session_state.num_players):
        st.session_state.players[i] = st.text_input(f"Enter name for Player {i+1}", key=f"player_name_{i+1}")

    if st.button("Start Game"):
        st.write("Game has started!")
        st.write(f"Players: {', '.join(st.session_state.players)}")

def new_game():
    st.title("Continental Card Game")
    
    if 'game_id' not in st.session_state:
        if st.button("Start New Game"):
            start_new_game()

    # If the number of players has been set, show the player name input fields
    if 'num_players' in st.session_state:
        enter_player_names()

if __name__ == "__main__":
    new_game()



