import streamlit as st
import random

# Initialize session state for scores and current round if not already set
if 'scores' not in st.session_state:
    st.session_state.scores = {'Team 1': 0,
                               'Team 2': 0, 'Team 3': 0, 'Team 4': 0}

if 'current_round' not in st.session_state:
    st.session_state.current_round = 1

# Path to the dice images
dice_images = {
    1: 'dice-1.png',
    2: 'dice-2.png',
    3: 'dice-3.png',
    4: 'dice-4.png',
    5: 'dice-5.png',
    6: 'dice-6.png'
}


def roll_dice():
    """Simulate rolling a dice, returning a random number between 1 and 6."""
    return random.randint(1, 6)


def play_turn(team_name):
    """Play a turn for the given team."""
    roll = roll_dice()
    st.session_state.scores[team_name] += roll
    # Display the dice image larger and to the right of the buttons
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("")  # This is just to create some space
    with col2:
        st.image(dice_images[roll], width=200,
                 caption=f"{team_name} rolled a {roll}")
    st.write(
        f"{team_name} now has {st.session_state.scores[team_name]} points.")


st.title('Dice Rolling App for 4 Teams')

# Display the current round
st.header(f"Round {st.session_state.current_round}")

# Create a button for each team to roll the dice
for team in st.session_state.scores.keys():
    if st.button(f'Roll Dice for {team}', key=team):
        play_turn(team)

# Button to proceed to the next round
if st.button('Next Round'):
    st.session_state.current_round += 1  # Increment the round

# Display the current scores
st.subheader('Current Scores')
for team, score in st.session_state.scores.items():
    st.text(f"{team}: {score} points")

# Indicate the next round
st.write(f"Upcoming Round: {st.session_state.current_round}")
