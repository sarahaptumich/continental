import streamlit as st
import pandas as pd

def show_rules():
    st.title("Game Rules")
    st.write("""
    Continental is a game of combining cards like Gin Rummy, Remigio or Canasta. It has two peculiarities that make it unique: the plays that must be made after 
    each deal are fixed and it is possible to take another player's discard out of turn, taking another extra or "punishment" card when doing so.
    """)
    st.subheader("Game Objective", divider="red")
    st.write("""Link the cards in established
                combinations and expose them, scoring the cards that remain in the hand, combined or not. Whoever has the fewest points at the end of the game wins the game.""")
    st.subheader("Deck of Cards", divider="red")
    st.write("""Continental is played with various 52-card Spanish poker decks, although English poker decks with the same number of cards are also accepted.
                 Two jokers are necessary per deck. For four players, you have to     start with two decks and end with three. For five to eight players,
                 it is advisable to start with two decks, adding one after the first two partial games and another after the next two.""")
    st.subheader("Number of players", divider="red")
    st.write("""From two to eight players and the game is always individual, without forming pairs or teams.""")
    st.subheader("Order and value of cards", divider="red")
    st.write("""The order of the cards is the usual one, from ace to king consecutively. The value of the cards is as follows:""")

    data = {
    "Cards": ["Wild Card", "Ace", "K, Q, J, 10, 9 and 8", "7, 6, 5, 4, 3 and 2"],
    "Points": ["50 Points", "20 Points", "10 Points", "5 Points"]
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.subheader("Cards' Distribution", divider="red")
    st.write("""Cards are drawn to determine who will be the player to start the game as dealer for the first round. The dealer will shuffle them, 
                cut them and distribute six to each player, one at a time, clockwise. Then the top card from the deck is revealed and the game begings """)
    st.subheader("Start and run of the game", divider="red")
    st.write("""Each player, in their turn starting by the dealer, can take the face-up card from the pool or the top card from the deck. 
    He ends his turn by discarding one of his cards, which he will leave on the pot. If he does not take the card from the pool, any of the following players may do so
    with clockwise priority, but also drawing the top one as punishment. During his turn, the player who has the combinations that correspond to the game in progress
    can expose them, event is he does not close the     game.""")
    st.write("The advantages of displaying the combined cards are:")
    bullet_points = [
        "Decrease the penalty points if someone closes.",
        "Being able to place the uncombined cards in the exposed foreign combinations, without being able to undo and divide the ladders and without putting repeated cards in these.",
        "Be able to use exposed wildcards. After knocking down, any player can replace an exposed wild card with the card it represents and can use it on any other ladder.",
        "The only reason to place it in another trio is to not be able to be used by other players.",
        "On the other hand, exposing has the disadvantage of facilitating the closure of another player."
    ]
    st.write("\n".join(f"- {point}" for point in bullet_points))
    st.write(""" When someone closes, each player proceeds to record the value of the cards remaining in their hand. The cards are then collected and the turn of distribution
    passes to the next player,     who will give the corresponding cards, and so on. At the end of the last hand, the player with the fewest accumulated points will be the winner
    of the game. """)
    st.subheader("Plays or combinations", divider="red")
    st.write("Players can make the following two combinations")
    bullet_points_2=[
    "Three of a kind (TK): Three cards of the same index, regardless of suit.",
    "Straight: Four consecutive cards of the same suit."]
    st.write("\n".join(f"- {point}" for point in bullet_points_2))
    st.write("""The wild card or joker is a special card that replaces any other card in the deck. You can make a trio with two jokers and a natural card, 
    but not a trio of jokers.""")
    st.write(""" In Continental, the rounds that must be made are fixed and the order in which they must be played is as explained below:""")
    bullet_points_3=[
    "First game: Six cards are dealt and two TK must be made.",
    "Second game: Seven cards are dealt and you have to make a TK and a straight.",
    "Third game: With eight cards, two straights.",
    "Fourth game: Dealing nine cards, three TK.",
    "Fifth game: Ten cards are dealt to make two TK and a straight.",
    "Sixth game: With eleven cards, a trio and two straights.",
    "Seventh game: With twelve cards, three straights."]
    st.write("\n".join(f"- {point}" for point in bullet_points_3))
    st.subheader("Penalty Cards", divider="red")
    st.write(""" In Continental, players can take another player's discard, if two or more players want the same card the order of precendent is clockwise. 
                 If the player who takes the discarded card is the one whose turn it is, play continues as normal. If it is someone else, they must also take 
                 a penalty card from the stack. This double draw can cause a player, after making the combinations, to have uncombined cards left in his hand. The player who discarded
                 the card can not take it back""")
    st.subheader("Closing a round", divider="red")
    st.write(""" A player closes the round when he was able to combined all his cards. At that point the other players must count all cards using the points' system and recorded it. 
                 """)
    st.subheader("End of the Game", divider="red")
    st.write("""At the end of all seven round the winner is the person with the least points.""")
