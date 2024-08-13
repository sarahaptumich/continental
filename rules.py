import streamlit as st

def show_rules():
    st.title("Game Rules")
    st.write("""
    Here are the rules of the game:
    1. The game is played between two players.
    2. Players take turns to make a move.
    3. The objective of the game is to achieve a specific goal.
    4. The player who reaches the goal first wins the game.
    5. If all moves are exhausted without a winner, the game ends in a draw.
    
    You can customize these rules based on the specific game you are developing.
    """)
