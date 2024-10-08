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
    toss_result = random.choice(["heads", "tails"])
    if user_selection == toss_result:
        print("You won the flip!")
    else:
        print("The house wins this time!")


coin_toss("heads")
