from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

class SquadForm(FlaskForm):
    squad_name = StringField("Squad Name", validators=[DataRequired()])
    game_name = StringField("Game Name", validators=[DataRequired()])
    size = IntegerField("Size", validators=[DataRequired(),
                                            NumberRange(min=1, max=10)])
    submit = SubmitField("Create Squad")
@app.route('/', methods=['GET', 'POST'])
def index():
    my_form = SquadForm(request.form)
    message = None
    if my_form.validate_on_submit():
        squadNameEntered = my_form.squad_name.data
        gameNameEntered = my_form.game_name.data
        sizeEntered = my_form.size.data
        message = (f"Squad {squadNameEntered} for {gameNameEntered} with {sizeEntered}"
                   f" players created SUCCESSFULLY!")
    return render_template("squad.html",form=my_form, message=message)

if __name__ == '__main__':
    app.run(debug=True)