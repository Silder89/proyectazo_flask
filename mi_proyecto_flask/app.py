from flask import Flask, render_template
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route("/")
def index():
    return "Hola, Flask!"



@app.route("/about")
def about():
    return render_template("about.html", proyecto="Mi primer app Flask")

if __name__ == "__main__":
    app.run(debug=True)

