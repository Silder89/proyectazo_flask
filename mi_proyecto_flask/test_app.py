import unittest
import uuid

from app import Usuario, app, db

class PruebasApp(unittest.TestCase):
  def setUp(self):
    app.config["WTF_CSRF_ENABLED"] = False
    self.cliente = app.test_client()

  def test_modelo_usuario(self):
    usuario = Usuario(nombre="Ana", correo="ana@ejemplo.com")
    self.assertEqual(usuario.nombre, "Ana")
    self.assertEqual(usuario.correo, "ana@ejemplo.com")

  def test_pagina_principal(self):
    respuesta = self.cliente.get("/")
    self.assertEqual(respuesta.status_code, 200)

  def test_pagina_inexistente(self):
    respuesta = self.cliente.get("/no-existe")
    self.assertEqual(respuesta.status_code, 404)

  def test_formulario_vacio(self):
    respuesta = self.cliente.post("/contacto", data={})
    texto = respuesta.get_data(as_text=True)
    self.assertEqual(respuesta.status_code, 200)
    self.assertIn("Escribe tu nombre", texto)

  def test_registro_valido_se_guarda(self):
    correo = f"prueba_{uuid.uuid4().hex[:8]}@ejemplo.com"
    datos = {"nombre": "Prueba", "correo": correo}
    respuesta = self.cliente.post("/contacto", data=datos,
follow_redirects=True)
    self.assertIn("Registro guardado con éxito",respuesta.get_data(as_text=True))
    with app.app_context():
      usuario = Usuario.query.filter_by(correo=correo).first()
      self.assertIsNotNone(usuario)
      db.session.delete(usuario)
      db.session.commit()
  

if __name__ == "__main__":
  unittest.main()
