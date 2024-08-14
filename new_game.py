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
        st.write(f"Entering scores for Game ID: {st.session_state.game_id}")
        st.write(f"Round: {st.session_state.round}")
        
        # Enter scores for each player
        for player in st.session_state.players:
            points = st.number_input(f"Points for {player} in Round {st.session_state.round}", min_value=0, step=1)
            st.session_state.scores[player].append(points)
        
        # Button to save the scores for the round
        if st.button("Save Scores for This Round"):
            # Save the scores to the CSV file
            data = []
            for player in st.session_state.players:
                data.append({
                    "game_id": st.session_state.game_id,
                    "players name": player,
                    "round": st.session_state.round,
                    "points": st.session_state.scores[player][-1]
                })
            
            df = pd.DataFrame(data)
            file_name = "game_scores.csv"
            
            if not os.path.isfile(file_name):
                df.to_csv(file_name, index=False)
            else:
                df.to_csv(file_name, mode='a', header=False, index=False)
            
            # Update the round
            st.session_state.round += 1
            
            # Check if all rounds are completed
            if st.session_state.round > 7:
                st.success("All rounds completed! Starting a new game.")
                st.session_state.round = 1
                st.session_state.scores = {}
                st.session_state.game_id = None
            else:
                st.experimental_rerun()
        
        # Display current tally
        st.write("### Current Tally")
        tally_data = {player: sum(st.session_state.scores[player]) for player in st.session_state.players}
        tally_df = pd.DataFrame(list(tally_data.items()), columns=["Player", "Total Points"])
        st.write(tally_df)

if __name__ == "__main__":
    new_game()
