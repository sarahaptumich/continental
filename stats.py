import streamlit as st

def show_stats():
    st.title("Game Statistics")
    st.write("This section will show the game statistics.")
    
    # Example stats
    games_played = 10
    player1_wins = 4
    player2_wins = 3
    draws = 3
    
    st.write(f"Games played: {games_played}")
    st.write(f"{player1_wins} games won by Player 1")
    st.write(f"{player2_wins} games won by Player 2")
    st.write(f"Draws: {draws}")
    
    # Here you can insert code to display more detailed statistics
