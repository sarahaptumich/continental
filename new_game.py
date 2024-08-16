import streamlit as st
import uuid
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Function to initialize the game and reset session state variables
def initialize_game():
    st.session_state.game_id = str(uuid.uuid4())  # Generate a unique game ID
    st.session_state.num_players = 0  # Number of players will be set by user
    st.session_state.players = []  # List to store player names
    st.session_state.scores = {}  # Dictionary to store player scores by round
    st.session_state.current_round = 1  # Start from round 1
    st.session_state.game_started = False  # Flag to check if the game has started
    st.session_state.game_completed = False  # Flag to check if the game is completed
    st.session_state.winner = None  # To store the winner's name after the game ends

# Function to start a new game using a form to input the number of players
def start_new_game():
    # Use a form to enter the number of players
    with st.form("player_count_form"):
        num_players = st.number_input("Number of Players", min_value=2, max_value=8, step=1)
        submit_players_count = st.form_submit_button("Submit")
    
    # If the number of players is submitted, proceed to enter player names
    if submit_players_count:
        st.session_state.num_players = int(num_players)
        st.session_state.players = [""] * st.session_state.num_players  # Initialize player names list
        st.session_state.scores = {}  # Reset scores to ensure they are initialized with actual names
        st.session_state.game_started = False  # Set game started to False to show player name inputs
        st.rerun()  # Trigger rerun to proceed to the next step

# Function to input player names using a container
def enter_player_names():
    st.write("### Enter Player Names")
    with st.form("player_names_form"):
        for i in range(st.session_state.num_players):
            st.session_state.players[i] = st.text_input(f"Enter name for Player {i+1}", key=f"player_name_{i+1}")
        submit_player_names = st.form_submit_button("Submit Player Names")
    
    # If player names are submitted, initialize scores with actual player names
    if submit_player_names:
        st.session_state.scores = {player: [0] * 7 for player in st.session_state.players}  # Initialize scores with actual names
        st.session_state.game_started = True  # Set flag to indicate that the game can start
        st.rerun()  # Trigger rerun to proceed to the game



def append_round_to_google_sheet():
    # Create a connection object to the Google Sheet
    conn = st.connection("gsheets", type=GSheetsConnection)

    # Prepare the data to be appended
    data = []
    for player in st.session_state.players:
        data.append({
            "Game_ID": st.session_state.game_id,
            "Round": st.session_state.current_round,
            "Player": player,
            "Score": st.session_state.scores[player][st.session_state.current_round - 1],
            "Status": "COMPLETED" if st.session_state.current_round <= 7 else "OPEN"
        })

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Append the DataFrame to the Google Sheet
    conn.write(df)

# Example usage in your main game function
def enter_scores():
    st.write(f"### Enter Scores for Round {st.session_state.current_round}")
    with st.form("score_entry_form"):
        for player in st.session_state.players:
            score = st.number_input(
                f"Enter score for {player}", min_value=0, step=1, key=f"score_{player}_round_{st.session_state.current_round}"
            )
            st.session_state.scores[player][st.session_state.current_round - 1] = score  # Store score in the correct round
        submit_scores = st.form_submit_button("Submit Scores")
    
    # If scores are submitted, move to the next round or end the game
    if submit_scores:
        # Append the round scores to the Google Sheet
        append_round_to_google_sheet()
        
        if st.session_state.current_round < 7:
            st.session_state.current_round += 1
        else:
            st.session_state.game_completed = True
            st.session_state.winner = calculate_winner()
        st.rerun()  # Trigger rerun to update the UI


# Function to calculate the winner after all rounds
def display_tally():
    st.write("### Current Tally")

    # Extract player names
    players = st.session_state.players
    
    # Prepare the data for each round
    rounds_data = {player: [] for player in players}
    rounds_data["Game_ID"] = []
    rounds_data["Status"] = []

    # Populate the data for each round
    for round_num in range(1, 8):
        for player in players:
            if round_num <= st.session_state.current_round:
                rounds_data[player].append(st.session_state.scores[player][round_num - 1])
            else:
                rounds_data[player].append("")
        
        # Add Game_ID and Status
        rounds_data["Game_ID"].append(st.session_state.game_id)
        
        if round_num < st.session_state.current_round:
            # If the round has already been completed
            rounds_data["Status"].append("COMPLETED")
        elif round_num == st.session_state.current_round:
            # If the round is currently ongoing
            is_completed = all(st.session_state.scores[player][round_num - 1] != 0 for player in players)
            rounds_data["Status"].append("COMPLETED" if is_completed else "OPEN")
        else:
            # Future rounds that have not occurred
            rounds_data["Status"].append("")

    # Add Total Points row
    for player in players:
        rounds_data[player].append(sum(st.session_state.scores[player][:st.session_state.current_round]))
    
    # Add empty cells for Game_ID and Status in Total Points row
    rounds_data["Game_ID"].append("")
    rounds_data["Status"].append("")

    # Create the DataFrame
    tally_df = pd.DataFrame(rounds_data, index=[f"Round {i}" for i in range(1, 8)] + ["Total Points"])

    # Display the DataFrame
    st.write(tally_df)

def calculate_winner():
    # Calculate the total points for each player based on completed rounds
    total_scores = {player: sum(st.session_state.scores[player][:st.session_state.current_round]) for player in st.session_state.players}
    
    # Determine the winner by finding the player with the lowest total points
    winner = min(total_scores, key=total_scores.get)
    
    # Return the winner's name and their total points
    return winner, total_scores[winner]


# Function to display the final results
def display_final_results():
    st.write("### Final Results")
    
    # Calculate the winner
    winner, winner_points = calculate_winner()
    st.write(f"Winner: {winner}, Score: {winner_points}")
    
    # Extract player names
    players = st.session_state.players
    
    # Prepare the data for each round, similar to tally_df
    rounds_data = {player: [] for player in players}

    # Populate the data for each round
    for round_num in range(1, 8):
        for player in players:
            if round_num <= st.session_state.current_round:
                rounds_data[player].append(st.session_state.scores[player][round_num - 1])
            else:
                rounds_data[player].append("")
    
    # Add Total Points row
    for player in players:
        rounds_data[player].append(sum(st.session_state.scores[player][:st.session_state.current_round]))

    # Create the final DataFrame, identical to tally_df but without Game_ID and Status
    final_df = pd.DataFrame(rounds_data, index=[f"Round {i}" for i in range(1, 8)] + ["Total Points"])

    # Display the final DataFrame
    st.write(final_df)

    # Button to start a new game
    if st.button("Start New Game"):
        initialize_game()  # Reset the game state
        st.rerun()  # Trigger a rerun to begin the new game


# Main function to control the flow of the game
def new_game():
    st.title("Continental Card Game")
   
    # Check if the game has been initialized; if not, initialize it
    if 'game_id' not in st.session_state:
        initialize_game()
    else:
        st.write("Game ID: ",st.session_state.game_id)

    # If the game is not started and player names have not been entered, ask for the number of players
    if not st.session_state.game_started and not st.session_state.players:
        start_new_game()
    
    # If players have been entered but the game has not started, ask for player names
    elif not st.session_state.game_started and st.session_state.players:
        enter_player_names()

    # If the game has started but not completed, allow score entry and display current tally
    elif st.session_state.game_started and not st.session_state.game_completed:
        enter_scores()
        display_tally()

    # If the game is completed, display final results
    elif st.session_state.game_completed:
        display_final_results()
        st.write("Game Status: Completed")

if __name__ == "__main__":
    new_game()
