import streamlit as st

def show_rules():
    st.title("Game Rules")
    st.write("""
    Continental is a game of combining cards like Gin Rummy, Remigio or Canasta. It has two peculiarities that make it unique: the plays that must be made after 
    each deal are fixed and it is possible to take another player's discard out of turn, taking another extra or "punishment" card when doing so.
    """)
    st.subheader("Game Objective", divider="red")
    st.write("""Link the cards in established
    combinations and expose them, scoring the cards that remain in the hand, combined or not. Whoever has the fewest points at the end of the game wins the game.""")
