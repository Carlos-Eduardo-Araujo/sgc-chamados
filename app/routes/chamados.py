from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.chamado import (
    ChamadoCreate, ChamadoResponse, StatusUpdate, PrioridadeUpdate, ResponsavelUpdate
)
from app.services.chamado import ChamadoService

router = APIRouter(prefix="/chamados", tags=["Chamados"])

@router.post("", response_model=ChamadoResponse, status_code=status.HTTP_201_CREATED)
def criar_chamado(payload: ChamadoCreate, db: Session = Depends(get_db)):
    return ChamadoService.criar(db, payload)

@router.get("", response_model=list[ChamadoResponse])
def listar_chamados(db: Session = Depends(get_db)):
    return ChamadoService.listar(db)

@router.get("/{chamado_id}", response_model=ChamadoResponse)
def obter_chamado(chamado_id: int, db: Session = Depends(get_db)):
    return ChamadoService.obter(db, chamado_id)

@router.patch("/{chamado_id}/status", response_model=ChamadoResponse)
def alterar_status(chamado_id: int, payload: StatusUpdate, db: Session = Depends(get_db)):
    return ChamadoService.alterar_status(db, chamado_id, payload.status)

@router.patch("/{chamado_id}/prioridade", response_model=ChamadoResponse)
def alterar_prioridade(chamado_id: int, payload: PrioridadeUpdate, db: Session = Depends(get_db)):
    return ChamadoService.alterar_prioridade(db, chamado_id, payload.prioridade)

@router.patch("/{chamado_id}/responsavel", response_model=ChamadoResponse)
def atribuir_responsavel(chamado_id: int, payload: ResponsavelUpdate, db: Session = Depends(get_db)):
    return ChamadoService.atribuir_responsavel(db, chamado_id, payload.responsavel)
