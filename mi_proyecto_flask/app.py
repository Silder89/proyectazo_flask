from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hola, Flask!"


@app.route("/about")
def about():
    return render_template("about.html", proyecto="Mi primer app Flask")


if __name__ == "__main__":
    app.run(debug=True)

