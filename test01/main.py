import streamlit as st
import random

# List of positive affirmations
positive_affirmations = [
    "I am confident and capable.",
    "I believe in my abilities and potential.",
    "I am worthy of success and happiness.",
    "I attract positive energy into my life.",
    "I am resilient and can overcome any challenges.",
    "I am grateful for the opportunities that come my way.",
    "I am surrounded by love and support.",
    "I trust in my journey and the process of life.",
    "I am constantly growing and evolving.",
    "I radiate positivity and kindness.",
]

def get_random_affirmation(previous_affirmation):
    new_affirmation = previous_affirmation
    while new_affirmation == previous_affirmation:
        new_affirmation = random.choice(positive_affirmations)
    return new_affirmation

def main():
    st.title("Positive Affirmations")

    # Display a random affirmation
    affirmation = get_random_affirmation("")
    st.header("Positive Affirmation:")
    st.write(f"\"{affirmation}\"")

    # Button to get a new affirmation
    if st.button("Next Affirmation"):
        affirmation = get_random_affirmation(affirmation)
        st.header("Positive Affirmation:")
        st.write(f"\"{affirmation}\"")

if __name__ == "__main__":
    main()

