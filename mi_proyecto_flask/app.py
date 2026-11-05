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


class Usuario(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True , nullable=False)


with app.app_context():
   db.create_all()

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
        existente = Usuario.query.filter_by(correo=form.correo.data).first()
        if existente:
            flash("Ese correo ya está registrado. Prueba con otro.", "warning")
        else:
            nuevo = Usuario(nombre=form.nombre.data, correo=form.correo.data)
            db.session.add(nuevo)
            db.session.commit()
            flash(f"¡Registro guardado con éxito, {nuevo.nombre}!", "success")
            return redirect(url_for("contacto"))
    return render_template("contacto.html", form=form)

@app.route("/usuarios")
def usuarios():
    lista = Usuario.query.order_by(Usuario.id).all()
    return render_template("usuarios.html", usuarios=lista)

if __name__ == "__main__":
    app.run(debug=True)

