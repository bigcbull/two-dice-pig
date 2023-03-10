#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Terminal module to implement decent graphical representation."""

import os
import platform
from pathlib import Path
from textwrap import dedent
import climage
import art
import tabulate


class Terminal:
    """Terminal Class."""

    def __init__(self):
        """Init constructor terminal class."""
        self.assets_path = (Path(__file__).parent).joinpath('img')

    def display_title(self):
        """Display game title."""
        return print(art.text2art("TWO  DICE  PIG", font="tarty3"))

    def display_intro_img(self):
        """Display game intro image."""
        return print(
            climage.convert(
                f'{self.assets_path}/dice_intro.jpg',
                is_unicode=True,
                width=61,
                palette="gruvbox"
            )
        )

    def display_prompt(self, text):
        """Display a prompt to enable user to input information."""
        value = input(f"{text} > ")
        return value

    def display_intro_menu(self):
        """Display game intro/main menu."""
        return print(dedent("""\
                    - Player vs Player | (multiplayer)
                    - Player vs Bot | (bot)
                    - View game rules | (rules)
                    - Exit | (exit)\n"""))

    def display_computer_menu(self):
        """Display computer difficulty menu."""
        return print("1. Easy\n2. Moderate\n3. Hard\n")

    def display_realtime_menu(self):
        """Display a realtime menu when playing."""
        return print(dedent("""\
                    1. Roll the dice
                    2. Pass
                    3. Change name
                    4. Exit current game\n"""))

    def display_rules(self):
        """Display rules of the game."""
        return print(dedent("""\
                    Here's a brief description of how to play the game:\n
                     - The game is played by two players or against the
                     computer, and each turn consists of a player rolling
                     two six-sided dice.\n
                     - The player's score for that turn is the sum of the
                     numbers rolled on the dice.\n
                     - The player can choose to roll again and add the new
                     sum to their current score, or they can choose to end
                     their turn and keep their current score.\n
                     - If the player rolls a one on either of the dice, their
                     turn ends and their score for that turn is zero.\n
                     - If the player rolls a one on both of the dice, their
                     turn ends and their entire score during that round will
                     be lost.\n
                     - The first player to reach a predetermined winning
                     score (100 points) wins the game.\n"""))

    def display_dice(self, faces_tuple):
        """Display the two dices a player gets."""
        dice1 = climage.convert(
            f'{self.assets_path}/dice_{faces_tuple[0]}.png',
            is_unicode=True,
            is_truecolor=True,
            is_256color=False,
            width=12
        )
        dice2 = climage.convert(
            f'{self.assets_path}/dice_{faces_tuple[1]}.png',
            is_unicode=True,
            is_truecolor=True,
            is_256color=False,
            width=12
        )
        return print(f'{dice1}\n{dice2}')

    def display_table(self, score_list):
        """Display a table which keeps track of the scoreboard."""
        table = score_list
        headers = ["Player", "Score"]
        parsed_table = tabulate.tabulate(
            table,
            headers,
            tablefmt="heavy_outline"
        )
        return print(f'{parsed_table}\n')

    def display_winner(self, player_name):
        """Display game winner."""
        return print(art.text2art(f"{player_name}  won!\n",
                                  font="tarty1"))

    def display_clear(self):
        """Clear the display."""
        match (platform.system()):
            case 'Windows' | 'windows':
                return os.system('cls')
            case _:
                return os.system('clear')
