class Estudiante:
  def __init__(self, id, nombre, edad, direccion, telefono):
    self.id = id
    self.nombre = nombre
    self.edad = edad
    self.direccion = direccion
    self.telefono = telefono

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'nombre': self.nombre,
      'edad': self.edad,
      'direccion':self.direccion,
      'telefono': self.telefono
    }