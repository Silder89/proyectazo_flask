from app import Usuario, app, db
with app.app_context():
  print("Antes:", Usuario.query.count())
  prueba = Usuario(nombre="Prueba", correo="prueba@ejemplo.com")
  db.session.add(prueba)
  db.session.commit()
  print("Después de guardar:", Usuario.query.count())
  db.session.delete(prueba)
  db.session.commit()
  print("Después de borrar:", Usuario.query.count())
