from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.vuelo import Vuelo
from tda.tda_lista_doble import ListaDoblementeEnlazada

router = APIRouter(prefix="/vuelos", tags=["vuelos"])
lista_vuelos = ListaDoblementeEnlazada()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_vuelos(db: Session = Depends(get_db)):
    return db.query(Vuelo).all()

@router.post("/")
def agregar_vuelo(vuelo: dict, db: Session = Depends(get_db)):
    nuevo_vuelo = Vuelo(**vuelo)
    db.add(nuevo_vuelo)
    db.commit()
    db.refresh(nuevo_vuelo)
    lista_vuelos.insertar_al_final(nuevo_vuelo)
    return nuevo_vuelo

@router.get("/{id}")
def obtener_vuelo(id: int, db: Session = Depends(get_db)):
    vuelo = db.query(Vuelo).filter(Vuelo.id == id).first()
    if not vuelo:
        raise HTTPException(status_code=404, detail="Vuelo no encontrado")
    return vuelo

@router.delete("/{id}")
def eliminar_vuelo(id: int, db: Session = Depends(get_db)):
    vuelo = db.query(Vuelo).filter(Vuelo.id == id).first()
    if not vuelo:
        raise HTTPException(status_code=404, detail="Vuelo no encontrado")
    db.delete(vuelo)
    db.commit()
    return {"ok": True}

@router.post("/insertar_posicion")
def insertar_en_posicion(data: dict, db: Session = Depends(get_db)):
    vuelo = Vuelo(**data["vuelo"])
    db.add(vuelo)
    db.commit()
    db.refresh(vuelo)
    lista_vuelos.insertar_en_posicion(vuelo, data["posicion"])
    return vuelo

@router.delete("/eliminar_posicion/{pos}")
def eliminar_por_posicion(pos: int):
    vuelo = lista_vuelos.extraer_de_posicion(pos)
    return vuelo