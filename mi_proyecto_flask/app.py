import os
from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from forms import ContactoForm


load_dotenv()
app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///proyecto.db"

bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template ("index.html")



@app.route("/about")
def about():
    return render_template("about.html", proyecto="Mi primer app Flask")


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
   form = ContactoForm()
   if form.validate_on_submit():
      flash(f"¡Gracias, {form.nombre.data}! Recibimos tus datos.", "success")
      return redirect(url_for("contacto"))
   return render_template("contacto.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

