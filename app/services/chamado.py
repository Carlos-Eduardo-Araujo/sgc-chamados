from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.chamado import Chamado
from app.repositories.chamado import ChamadoRepository
from app.schemas.chamado import ChamadoCreate, Status, Prioridade

TRANSICOES_VALIDAS = {
    Status.ABERTO: {Status.EM_ANDAMENTO, Status.CANCELADO},
    Status.EM_ANDAMENTO: {Status.RESOLVIDO, Status.CANCELADO},
    Status.RESOLVIDO: set(),
    Status.CANCELADO: set(),
}

class ChamadoService:
    @staticmethod
    def criar(db: Session, data: ChamadoCreate) -> Chamado:
        chamado = Chamado(
            titulo=data.titulo,
            descricao=data.descricao,
            prioridade=data.prioridade.value,
            status=Status.ABERTO.value,
        )
        return ChamadoRepository.create(db, chamado)

    @staticmethod
    def listar(db: Session) -> list[Chamado]:
        return ChamadoRepository.list_all(db)

    @staticmethod
    def obter(db: Session, chamado_id: int) -> Chamado:
        chamado = ChamadoRepository.get_by_id(db, chamado_id)
        if chamado is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chamado não encontrado")
        return chamado

    @staticmethod
    def alterar_status(db: Session, chamado_id: int, novo_status: Status) -> Chamado:
        chamado = ChamadoService.obter(db, chamado_id)
        atual = Status(chamado.status)
        if novo_status not in TRANSICOES_VALIDAS[atual]:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Transição inválida: {atual.value} -> {novo_status.value}",
            )
        chamado.status = novo_status.value
        return ChamadoRepository.save(db, chamado)

    @staticmethod
    def alterar_prioridade(db: Session, chamado_id: int, prioridade: Prioridade) -> Chamado:
        chamado = ChamadoService.obter(db, chamado_id)
        if chamado.status in {Status.RESOLVIDO.value, Status.CANCELADO.value}:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Chamado encerrado não pode ser alterado")
        chamado.prioridade = prioridade.value
        return ChamadoRepository.save(db, chamado)

    @staticmethod
    def atribuir_responsavel(db: Session, chamado_id: int, responsavel: str) -> Chamado:
        chamado = ChamadoService.obter(db, chamado_id)
        if chamado.status in {Status.RESOLVIDO.value, Status.CANCELADO.value}:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Chamado encerrado não pode ser alterado")
        chamado.responsavel = responsavel
        return ChamadoRepository.save(db, chamado)
