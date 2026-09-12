from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.chamado import Chamado

class ChamadoRepository:
    @staticmethod
    def create(db: Session, chamado: Chamado) -> Chamado:
        db.add(chamado)
        db.commit()
        db.refresh(chamado)
        return chamado

    @staticmethod
    def list_all(db: Session) -> list[Chamado]:
        return list(db.scalars(select(Chamado).order_by(Chamado.id)).all())

    @staticmethod
    def get_by_id(db: Session, chamado_id: int) -> Chamado | None:
        return db.get(Chamado, chamado_id)

    @staticmethod
    def save(db: Session, chamado: Chamado) -> Chamado:
        db.add(chamado)
        db.commit()
        db.refresh(chamado)
        return chamado
