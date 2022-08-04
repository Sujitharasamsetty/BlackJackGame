from flask import Flask
from flask import render_template
import random

app=Flask(__name__)


CARD_SCORES = {
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Valet': 2,
    'Dama': 3,
    'Korol': 4,
    'Tuz': 11
}


