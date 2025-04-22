from sqlalchemy import Column, Integer, String
from db.database import Base

class Vuelo(Base):
    __tablename__ = "vuelos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)
    tipo = Column(String)  # Ej: "Emergencia", "Regular", "Retrasado"
    prioridad = Column(Integer)  # Puede usarse como campo adicional para ordenar