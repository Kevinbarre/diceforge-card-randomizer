#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Projet: diceforge-card-randomizer
# Author: Kévin Barré
# Creation date: 13/04/2018

from flask import Flask, render_template

from dcr.models.cards import CardList

app = Flask(__name__)


@app.route('/')
def get_randomization():
    my_card_list = CardList()
    my_setup = my_card_list.randomize()
    return render_template('randomizer.html', setup=my_setup)