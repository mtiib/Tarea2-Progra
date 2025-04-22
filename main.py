from fastapi import FastAPI
from routers import vuelos
from db.database import Base, engine

app = FastAPI()

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Incluir las rutas
app.include_router(vuelos.router)