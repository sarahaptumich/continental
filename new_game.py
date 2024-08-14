import streamlit as st
import pandas as pd
import uuid
import os

# Initialize session state variables
if 'game_state' not in st.session_state:
    st.session_state.game_state = 'start'  # start, players, game
if 'round' not in st.session_state:
    st.session_state.round = 1
if 'scores' not in st.session_state:
    st.session_state.scores = {}
if 'game_id' not in st.session_state:
    st.session_state.game_id = None
if 'players' not in st.session_state:
    st.session_state.players = []

# Function to reset session state and start a new game
def start_new_game():
    st.session_state.game_state = 'players'
    st.session_state.round = 1
    st.session_state.scores = {}
    st.session_state.game_id = str(uuid.uuid4())
    st.session_state.players = []

# Function to display and handle player entry
def enter_players():
    st.title("Enter Players")
    num_players = st.number_input("Number of Players", min_value=2, max_value=8, step=1)
    
    if len(st.session_state.players) == 0:
        for i in range(int(num_players)):
            st.session_state.players.append(st.text_input(f"Enter name for Player {i+1}", key=f"player_name_{i+1}"))
    
    if st.button("Start Game"):
        st.session_state.game_state = 'game'
        for player in st.session_state.players:
            st.session_state.scores[player] = []
        st.experimental_rerun()

# Function to manage game rounds and score input
def play_game():
    st.title(f"Round {st.session_state.round}")
    st.write(f"Game ID: {st.session_state.game_id}")
    
    for player in st.session_state.players:
        points = st.number_input(f"Points for {player} in Round {st.session_state.round}", min_value=0, step=1, key=f"points_{player}_round_{st.session_state.round}")
        if len(st.session_state.scores[player]) < st.session_state.round:
            st.session_state.scores[player].append(points)
        else:
            st.session_state.scores[player][st.session_state.round - 1] = points
    
    if st.button("Save and Proceed to Next Round"):
        st.session_state.round += 1
        
        # Save scores to CSV
        data = []
        for player in st.session_state.players:
            data.append({
                "game_id": st.session_state.game_id,
                "players name": player,
                "round": st.session_state.round - 1,
                "points": st.session_state.scores[player][-1]
            })
        
        df = pd.DataFrame(data)
        file_name = "game_scores.csv"
        
        if not os.path.isfile(file_name):
            df.to_csv(file_name, index=False)
        else:
            df.to_csv(file_name, mode='a', header=False, index=False)
        
        if st.session_state.round > 7:
            st.success("Game completed!")
            st.session_state.game_state = 'start'
        else:
            st.experimental_rerun()
    
    # Display current tally
    st.write("### Current Tally")
    tally_data = {player: sum(st.session_state.scores[player]) for player in st.session_state.players}
    tally_df = pd.DataFrame(list(tally_data.items()), columns=["Player", "Total Points"])
    st.write(tally_df)

# Main application logic
def main():
    if st.session_state.game_state == 'start':
        st.title("Continental Card Game")
        if st.button("Start New Game"):
            start_new_game()
    elif st.session_state.game_state == 'players':
        enter_players()
    elif st.session_state.game_state == 'game':
        play_game()

if __name__ == "__main__":
    main()
