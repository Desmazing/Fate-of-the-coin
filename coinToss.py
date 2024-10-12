"""
This program is designed to simulate a classic coin toss
Phase 1: getting the functionality right
Phase 2: Design the GUI
Phase 3: Improve the UI
Phase 4: Add-ons
"""


import random
import numpy as np
from tkinter import *
from PIL import Image, ImageTk


def coin_toss(prediction):
    """
    Function to simulate a coin toss with either heads or tails as the result

    Args: str > user prrediction of either heads or tails
    Return: str > random result of the coin toss
    """

    prediction = input("HEADS OR TAILS?:\n")
    possible_choices = ["HEADS", "TAILS"]
    toss_result = random.choice(possible_choices)
    # answer_variations = ['tails', 'heads', 't', 'h']

    if prediction.upper() == toss_result:
        return f"{toss_result.upper()}! You won the flip!"
    else:
        return f"{toss_result.upper()}! You lose!"

print(repr(coin_toss("heads")))
