import os
from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from forms import ContactoForm, LoginForm


load_dotenv()
app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///proyecto.db"

bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer , primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True , nullable=False)

@login_manager.user_loader
def cargar_usuario(user_id):
  return db.session.get(Usuario, int(user_id))

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

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(correo=form.correo.data).first()
        if usuario:
            login_user(usuario)
            return redirect(url_for("perfil"))
        flash("No encontramos ese correo. Regístrate primero en Contacto.", "warning")
    return render_template("login.html", form=form)

@app.route("/perfil")
@login_required
def perfil():
  return render_template("perfil.html")

@app.route("/logout")
def logout():
    logout_user()
    flash("Cerraste tu sesión.", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

