"""
This program is designed to simulate a classic coin toss
Phase 1: getting the functionality right
Phase 2: Design the GUI
Phase 3: Improve the UI
Phase 4: Add-ons
"""


import random

def coin_toss(prediction):
    """
    Function to simulate a coin toss bearing either heads or tails as the result

    Args: str; user prrediction of either heads or tails
    Returns: str; random result of the coin toss
    """

    user_selection = input("Pick either heads or tails then press enter:\n")
    possible_choices = ["HEADS", "TAILS"]
    toss_result = random.choice(possible_choices)

    if user_selection.upper() == toss_result:
        print(f"{toss_result.upper()}! You won the flip!")
    else:
        print(f"{toss_result.upper()}! You lose!")


coin_toss("heads")
