"""
This file contains code for the life simulation game "AI Life Simulation".
Author: SoftwareApkDev
"""


# Game version: 1


# Importing necessary libraries


import sys
import time
import uuid
import pickle
import copy
import google.generativeai as genai
import random
from datetime import datetime
import os
from dotenv import load_dotenv
from functools import reduce
from mpmath import mp, mpf
from tabulate import tabulate
from google.generativeai import GenerativeModel
import subprocess
mp.pretty = True


# Creating static variables to be used throughout the game.


# Creating static functions to be used in this game.


def is_number(string: str) -> bool:
    try:
        mpf(string)
        return True
    except ValueError:
        return False


def ai_response(model: GenerativeModel, prompt: str) -> str:
    return str(model.generate_content(prompt).text)


def load_game_data(file_name):
    # type: (str) -> SavedGameData
    return pickle.load(open(file_name, "rb"))


def save_game_data(game_data, file_name):
    # type: (SavedGameData, str) -> None
    pickle.dump(game_data, open(file_name, "wb"))


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating necessary classes.


# TODO: add more features into this game (e.g., adventure mode, city tiles, missions, etc)


###########################################
# GENERAL
###########################################


class GameCharacter:
    """
    This class contains attributes of a game character.
    """

    def __init__(self, name):
        # type: (str) -> None
        self.character_id: str = str(uuid.uuid1())
        self.name: str = name

    def clone(self):
        # type: () -> GameCharacter
        return copy.deepcopy(self)


class NPC(GameCharacter):
    """
    This class contains attributes of a non-player character in this game.
    """

    def __init__(self, name):
        # type: (str) -> None
        GameCharacter.__init__(self, name)


class Player(GameCharacter):
    """
    This class contains attributes of the player in this game.
    """

    def __init__(self, name):
        # type: (str) -> None
        GameCharacter.__init__(self, name)
        self.level: int = 1

        # TODO: add more attributes and functions related to the player of this game.


class AIPlayer(Player):
    """
    This class contains attributes of an AI controlled player in this game.
    """

    def __init__(self, name):
        # type: (str) -> None
        Player.__init__(self, name)


class SavedGameData:
    """
    This class contains attributes of the saved game data in this game.
    """


###########################################
# GENERAL
###########################################


# Creating main function used to run the game.


def main() -> int:
    """
    This main function is used to run the game.
    :return: an integer
    """

    # Loading Gemini API Key
    load_dotenv()
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])

    # Gemini Generative Model
    model: GenerativeModel = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")


if __name__ == "__main__":
    main()
