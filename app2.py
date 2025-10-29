from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, RadioField, SelectField, SubmitField
import os
app = Flask(__name__)
app.secret_key = os.urandom(16)

class SignUpForm(FlaskForm):
    first_name = StringField("Enter your first name")
    last_name = StringField("Enter your last name")
    email = EmailField("Enter your email")
    pid = IntegerField("Enter your pantherID")
    campus = RadioField("Campus",choices=[
        ("mmc","Modesto Maidique Campus"),
        ("bbc","Biscayne Bay Campus"),
        ("ec","Engineering Center"),
        ("dc","FIU in DC")
    ])
    major = SelectField("Major", choices=[
        ("ds","Data Science and AI"),
        ("it","Information Technology"),
        ("cs","Computer Science"),
        ("cys","Cybersecurity")
    ])
    submit = SubmitField("Sign Up")
@app.route('/', methods=['GET', 'POST'])
def index():
    my_form = SignUpForm(request.form)
    if request.method == "POST":
        # Here, I can get the user's input data!!!
        first_name_entered = my_form.first_name.data
        last_name_entered = my_form.last_name.data
        email_entered = my_form.email.data
        pid_entered = my_form.pid.data
        campus_entered = my_form.campus.data
        major_entered = my_form.major.data
        full_name = first_name_entered+" "+last_name_entered
        return render_template("success.html",name=full_name)
    else:
        return render_template("index.html", form=my_form)

if __name__ == '__main__':
    app.run(debug=True)