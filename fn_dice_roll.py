import random
from flask import Blueprint, render_template

dice_bp = Blueprint('dice_bp', __name__)


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    return die1, die2, total


@dice_bp.route("/roll")
def roll_dice():
    # Dice logic here
    return render_template("roll.html")
