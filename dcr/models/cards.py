#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Projet: diceforge-card-randomizer
# Author: Kévin Barré
# Creation date: 13/04/2018
import random
from enum import Enum


class CardType(Enum):
    SOLAR = 1
    LUNAR = 2
    BOSS = 3

    def __gt__(self, other):
        return self.value > other.value


class CardSlot(object):
    def __init__(self, card_type, slot_number=None):
        self.card_type = card_type
        if card_type is not CardType.BOSS:
            self.slot_number = slot_number

    def __gt__(self, other):
        return self.card_type > other.card_type


class CardList(object):
    def __init__(self):
        self.card_list = {
            CardSlot(CardType.SOLAR, 1): ("L'ancien",),
            CardSlot(CardType.SOLAR, 2): ("Les herbes folles",),
            CardSlot(CardType.SOLAR, 3): ("Les ailes de la gardienne", "La voile celeste"),
            CardSlot(CardType.SOLAR, 4): ("Le minotaure", "Le bouclier de la gardienne"),
            CardSlot(CardType.SOLAR, 5): ("La méduse", "Le triton"),
            CardSlot(CardType.SOLAR, 6): ("Le miroir abyssal",),
            CardSlot(CardType.SOLAR, 7): ("L'énigme", "Le cyclope"),
            CardSlot(CardType.LUNAR, 1): ("Le marteau du forgeron",),
            CardSlot(CardType.LUNAR, 2): ("Le coffre du forgeron",),
            CardSlot(CardType.LUNAR, 3): ("Les sabots d'argent", "La grande ourse"),
            CardSlot(CardType.LUNAR, 4): ("Les satyres", "Le sanglier acharné"),
            CardSlot(CardType.LUNAR, 5): ("Le passeur", "Le cerbère"),
            CardSlot(CardType.LUNAR, 6): ("Le casque d'invisibilité",),
            CardSlot(CardType.LUNAR, 7): ("La pince", "La sentinelle"),
            CardSlot(CardType.BOSS): ("L'hydre", "Le typhon")
        }

    def __str__(self):
        return str(self.card_list)

    def randomize(self):
        card_setup = {card_slot: (random.choice(possible_values), len(possible_values) == 1)
                      for card_slot, possible_values in self.card_list.items()}
        return card_setup
