import SQLALchemy as SQLALchemy
from flask import Flask, render_template

app= Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ismca2@localhost/ismca2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ismca2@localhost:5435/ismca2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLALchemy(app)

@app.route("/")
def home():
    return render_template('home.html', title="Home")

@app.route("/register")
def register():
    return render_template('register', title="Register")

if __name__ == "__main__":
    app.run()

