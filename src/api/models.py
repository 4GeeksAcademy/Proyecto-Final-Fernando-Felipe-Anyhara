from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

db = SQLAlchemy()
Base = declarative_base()

class Apoderado(db.Model):
    __tablename__ = 'apoderado'
    id = db.Column(db.Integer, primary_key=True)  
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    correo_electronico = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(80), nullable=False)
    esta_activo = db.Column(db.Boolean, nullable=False, default=False)
    telefono = db.Column(db.String(20), nullable=True)
    direccion = db.Column(db.Text, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo_electronico": self.correo_electronico,
            "esta_activo": self.esta_activo,
        }
        
class Profesor(db.Model):
    __tablename__ = 'profesor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    correo_electronico = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(80), nullable=False)
    esta_activo = db.Column(db.Boolean, nullable=False, default=False)
    titulo = db.Column(db.String(120), nullable=True)
    especializacion = db.Column(db.String(120), nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo_electronico": self.correo_electronico,
            "esta_activo": self.esta_activo,
        }

class Asignatura(db.Model):
    __tablename__ = 'asignatura'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    id_profesor = db.Column(db.Integer, db.ForeignKey('profesor.id'))

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }
        
class Alumno(db.Model):
    __tablename__ = 'alumno'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    id_apoderado = db.Column(db.Integer, db.ForeignKey('apoderado.id'), nullable=False)
    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id'), nullable=False)
    esta_activo = db.Column(db.Boolean, nullable=False, default=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "esta_activo": self.esta_activo,
        }
        
def to_dict(self):
    return {}

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
