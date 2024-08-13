import streamlit as st
from PIL import Image
from rules import show_rules
from new_game import new_game
from stats import show_stats

# Load the logo image
logo = Image.open('continental_logo.png')

# Function for the landing page
def landing_page():
    st.title("Welcome to Continental")
    st.image(logo, use_column_width=True)
    st.write("Get ready to play the ultimate card game experience. Navigate through the menu to read the rules, start a new game, or view your stats!")

# Streamlit app structure using page imports
def main():
    pages = {
        "Landing Page": landing_page,
        "Rules": show_rules,
        "New Game": new_game,
        "Stats": show_stats
    }

    st.sidebar.markdown("### What is Continental?")
    st.sidebar.image('continental_logo.png', use_column_width=True)
    st.sidebar.write('Continental is a fun, family-friendly card game that can be enjoyed by everyone. This site will explain how to play and can also serve to keep track of games.')

    # Capture the user's choice from the sidebar
    selection = st.sidebar.radio("Navigate", list(pages.keys()))

    # Run the selected page function from the respective module
    pages[selection]()

if __name__ == "__main__":
    main()
