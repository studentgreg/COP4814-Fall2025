import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField, #TODO
from wtforms.validators import InputRequired

app = #TODO

app.secret_key = os.urandom(16)

HOUSES = {
    "gryffindor": {
        "name": "Gryffindor",
        "colors": "Red and Gold",
        "traits": "Courage, daring, and chivalry.",
        "emoji": "🦁",
        "hex": "#b31b1b",
    },
    "slytherin": {
        "name": "Slytherin",
        "colors": "Green and Silver",
        "traits": "Ambition, resourcefulness, and determination.",
        "emoji": "🐍",
        "hex": "#1f6f43",
    },
    "ravenclaw": {
        "name": "Ravenclaw",
        "colors": "Blue and Bronze",
        "traits": "Wisdom, creativity, and curiosity.",
        "emoji": "🦅",
        "hex": "#1f4e8c",
    },
    "hufflepuff": {
        "name": "Hufflepuff",
        "colors": "Yellow and Black",
        "traits": "Kindness, patience, and loyalty.",
        "emoji": "🦡",
        "hex": "#d4a10b",
    },
}

# ---- WTForms form ----
class QuizForm(#TODO):
    q1 = RadioField(
        "What matters most to you?",
        choices=[
            ("bravery", "Bravery & doing what's right"),
            ("ambition", "Achieving greatness & success"),
            ("wisdom", "Knowledge & understanding"),
            ("kindness", "Loyalty & fairness to others"),
        ],
        validators=[InputRequired()],
    )
    q2 = RadioField(
        "In a group project, you usually:",
        choices=[
            ("lead", "Take the lead and motivate everyone"),
            ("strategize", "Plan the strategy and next steps"),
            ("research", "Dive into the research and details"),
            ("support", "Help wherever you're needed most"),
        ],
        validators=[InputRequired()],
    )
    q3 = RadioField(
        "Your ideal free time activity:",
        choices=[
            ("adventure", "Exploring, traveling, or trying something bold"),
            ("plan", "Working on a long-term goal or side project"),
            ("read", "Reading, learning, or solving puzzles"),
            ("friends", "Hanging out and relaxing with friends"),
        ],
        validators=[InputRequired()],
    )
    submit = #TODO("Get my house")

def score_to_house(q1, q2, q3):
    scores = {k: 0 for k in HOUSES.keys()}

    # Q1
    if q1 == "bravery": scores["gryffindor"] += 1
    elif q1 == "ambition": scores["slytherin"] += 1
    elif q1 == "wisdom": scores["ravenclaw"] += 1
    elif q1 == "kindness": scores["hufflepuff"] += 1

    # Q2
    if q2 == "lead": scores["gryffindor"] += 1
    elif q2 == "strategize": scores["slytherin"] += 1
    elif q2 == "research": scores["ravenclaw"] += 1
    elif q2 == "support": scores["hufflepuff"] += 1

    # Q3
    if q3 == "adventure": scores["gryffindor"] += 1
    elif q3 == "plan": scores["slytherin"] += 1
    elif q3 == "read": scores["ravenclaw"] += 1
    elif q3 == "friends": scores["hufflepuff"] += 1

    # deterministic tie-breaker by declared order
    best = max(scores.items(), key=lambda kv: (kv[1], -list(HOUSES.keys()).index(kv[0])))
    return best[0]

@app.route("/", #TODO)
def index():
    form = QuizForm()
    if form.validate_on_submit():
        chosen_key = score_to_house(form.q1.data, form.q2.data, form.q3.data)
        return #TODO("harry.html", #TODO=form, house=HOUSES[chosen_key])
    return #TODO("harry.html", #TODO=form, house=None)

if __name__ == "__main__":
    #TODO