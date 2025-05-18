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


def list_to_string(a_list: list) -> str:
    res: str = "["  # initial value
    for i in range(len(a_list)):
        if i == len(a_list) - 1:
            res += str(a_list[i])
        else:
            res += str(a_list[i]) + ", "

    return res + "]"


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
# MINIGAMES
###########################################


class Minigame:
    """
    This class contains attributes of a minigame in this game.
    """

    def __init__(self, name):
        # type: (str) -> None
        self.name: str = name

    def clone(self):
        # type: () -> Minigame
        return copy.deepcopy(self)


# TODO: add types of minigames here


###########################################
# MINIGAMES
###########################################


###########################################
# ADVENTURE MODE
###########################################


class Action:
    """
    This class contains attributes of an action which can be carried out during battles.
    """


class Battle:
    """
    This class contains attributes of a battle in this game.
    """


class City:
    """
    This class contains attributes of a city in this game.
    """


class CityTile:
    """
    This class contains attributes of a tile in a city.
    """

    def __init__(self):
        # type: () -> None
        self.__game_characters: list = []  # initial value

    def get_game_characters(self):
        # type: () -> list
        return self.__game_characters

    def add_game_character(self, game_character):
        # type: (GameCharacter) -> None
        self.__game_characters.append(game_character)

    def remove_game_character(self, game_character):
        # type: (GameCharacter) -> bool
        if game_character in self.__game_characters:
            self.__game_characters.remove(game_character)
            return True
        return False

    def __str__(self):
        # type: () -> str
        return "(" + str(type(self).__name__) + ")\nAND\n" + list_to_string(
            [game_character.name for game_character in self.__game_characters])

    def clone(self):
        # type: () -> CityTile
        return copy.deepcopy(self)


# TODO: add types of city tiles.


###########################################
# ADVENTURE MODE
###########################################


###########################################
# INVENTORY
###########################################


class LegendaryCreatureInventory:
    """
    This class contains attributes of an inventory containing legendary creatures.
    """


class ItemInventory:
    """
    This class contains attributes of an inventory containing items.
    """


###########################################
# INVENTORY
###########################################


###########################################
# LEGENDARY CREATURE
###########################################


class LegendaryCreature:
    """
    This class contains attributes of a legendary creature.
    """

    # TODO: include attributes of a legendary creature.


class Skill:
    """
    This class contains attributes of a skill legendary creatures have.
    """


###########################################
# LEGENDARY CREATURE
###########################################


###########################################
# ITEM
###########################################


class Item:
    """
    This class contains attributes of an item in this game.
    """


###########################################
# ITEM
###########################################


###########################################
# EXERCISE
###########################################


class ExerciseGym:
    """
    This class contains attributes of a gym where the player can improve his/her attributes.
    """


class TrainingOption:
    """
    This class contains attributes of a training option for fitness.
    """


###########################################
# EXERCISE
###########################################


###########################################
# PROPERTIES
###########################################


class Property:
    """
    This class contains attributes of a property the player can live in.
    """


class PropertyUpgrade:
    """
    This class contains attributes of an upgrade to a property a player owns.
    """


###########################################
# PROPERTIES
###########################################


###########################################
# JOBS AND SKILLS
###########################################


class JobRole:
    """
    This class contains attributes of a job role a player can get in this game.
    """


class Course:
    """
    This class contains attributes of a course the player can take in this game.
    """


###########################################
# JOBS AND SKILLS
###########################################


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


class Mission:
    """
    This class contains attributes of a mission in this game.
    """

    def __init__(self, name, description):
        # type: (str, str) -> None
        self.name: str = name
        self.description: str = description

        # TODO: add more attributes (e.g., reward for completing mission) to this class.

    def clone(self):
        # type: () -> Mission
        return copy.deepcopy(self)


class ItemShop:
    """
    This class contains attributes of an item shop selling items.
    """


class Reward:
    """
    This class contains attributes of a reward gained for accomplishing something in this game.
    """


class AdventureModeLocation:
    """
    This class contains attributes of the location of a player in adventure mode of this game.
    """

    def __init__(self, tile_x, tile_y):
        # type: (int, int) -> None
        self.tile_x: int = tile_x
        self.tile_y: int = tile_y

    def clone(self):
        # type: () -> AdventureModeLocation
        return copy.deepcopy(self)


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
