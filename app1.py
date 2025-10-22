from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello FIU!'

@app.route('/aboutUs')
def aboutUs():
    firstName = "Greg"
    lastName = "Reis"
    return f"<h1>My name is {firstName} {lastName}.</h1>"

@app.route('/contact/<string:name>')
def contact(name):
    return f"{name}'s phone number is 305-248-7852."

if __name__ == '__main__':
    app.run(debug=True, port=8080)