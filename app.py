from flask import Flask

from flask import Flask
from fn_dice_roll import dice_bp




app = Flask(__name__)
app.register_blueprint(dice_bp)

if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)

import fn_dice_roll
dice1_roll = fn_dice_roll.roll_dice
dice1_roll_value = dice1_roll
app = Flask(__name__)

print(dice1_roll_value)

@app.route("/")
def home():
    return "Welcome to Dice Duel!"

if __name__ == "__main__":
    app.run(debug=True)


bucket = 500.00

player_bet = input("Please enter amount to bet:")
def play_round(bucket):
    bet = 10.00  # static for now — could later allow custom bet per round
    # Simulate dice roll (player vs computer)
    # winner = some_logic()
    winner = "player"  # stub
    
    if winner == "player":
        bucket += bet
        print(f"You won! wallet value is now: ${bucket:.2f}")
    else:
        bucket -= bet
        print(f"You lost. wallet value is now: ${bucket:.2f}")
    
    return bucket

def play_round(bucket):
    bet = 10.00  # static for now — could later allow custom bet per round
    # Simulate dice roll (player vs computer)
    # winner = some_logic()
    winner = "player"  # stub
    
    if winner == "player":
        bucket += bet
        print(f"🎉 You won! Bucket now: ${bucket:.2f}")
    else:
        bucket -= bet
        print(f"😢 You lost. Bucket now: ${bucket:.2f}")
    
    return bucket


def play_round(bucket):
    bet = 10.00  # static for now — could later allow custom bet per round
    # Simulate dice roll (player vs computer)
    # winner = some_logic()
    winner = "player"  # stub
    
    if winner == "player":
        bucket += bet
        print(f"🎉 You won! Bucket now: ${bucket:.2f}")
    else:
        bucket -= bet
        print(f"😢 You lost. Bucket now: ${bucket:.2f}")
    
    return bucket


while bucket > 0:
    bucket = play_round(bucket)
    # add option to quit early if desired 