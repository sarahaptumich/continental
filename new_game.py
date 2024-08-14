import streamlit as st
import pandas as pd
import os
import uuid

# Function to add a new game
def new_game():
    st.title("Add a New Game")
    
   # Generate a unique Game ID
    game_id = str(uuid.uuid4())
    st.write(f"Game ID: {game_id}")
    
    num_players = st.number_input("Number of Players", min_value=2, max_value=8, step=1)
    
    players = []
    for i in range(int(num_players)):
        player_name = st.text_input(f"Enter name for Player {i+1}", f"Player {i+1}")
        players.append(player_name)
    
    st.write("### Enter the points for each round")
    
    rounds = [f"Round {i+1}" for i in range(7)]
    results = {}
    
    # for player in players:
    #     results[player] = {}
    #     for rnd in rounds:
    #         points = st.number_input(f"Points for {player} in {rnd}", min_value=0, step=1)
    #         results[player][rnd] = points

    for rnd in rounds:
        results[rnd] = {}
        for player in players:
            points = st.number_input(f"Points for {rnd}  in  {player}", min_value=0, step=5)
            results[rnd][player] = points
    
    if st.button("Save Game"):
        # Create a DataFrame to store the results
        data = {"Game ID": game_id}
        # for player in players:
        #     for rnd in rounds:
        #         data[f"{player} - {rnd}"] = results[player][rnd]

        for rnd in rounds:
            for player in players:
                data[f"{rnd} - {player}"] = results[rnd][player]
        
        df = pd.DataFrame([data])
        
        # Display the results as a table
        st.write("### Game Results")
        st.write(df)
        
        # Define the file name
        file_name = "game_results.csv"
        
        # Check if the file already exists
        if not os.path.isfile(file_name):
            # If the file does not exist, write the header
            df.to_csv(file_name, index=False)
        else:
            # If the file exists, append without writing the header
            df.to_csv(file_name, mode='a', header=False, index=False)
        
        st.success("Game results saved successfully!")

# Example usage within a Streamlit app
if __name__ == "__main__":
    new_game()

