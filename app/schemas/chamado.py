from datetime import datetime
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field, field_validator

class Prioridade(str, Enum):
    BAIXA = "BAIXA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"
    CRITICA = "CRITICA"

class Status(str, Enum):
    ABERTO = "ABERTO"
    EM_ANDAMENTO = "EM_ANDAMENTO"
    RESOLVIDO = "RESOLVIDO"
    CANCELADO = "CANCELADO"

class ChamadoCreate(BaseModel):
    titulo: str = Field(min_length=3, max_length=120)
    descricao: str = Field(min_length=5, max_length=2000)
    prioridade: Prioridade = Prioridade.MEDIA

    @field_validator("titulo", "descricao")
    @classmethod
    def not_blank(cls, value: str):
        if not value.strip():
            raise ValueError("campo não pode conter apenas espaços")
        return value.strip()

class StatusUpdate(BaseModel):
    status: Status

class PrioridadeUpdate(BaseModel):
    prioridade: Prioridade

class ResponsavelUpdate(BaseModel):
    responsavel: str = Field(min_length=2, max_length=120)

    @field_validator("responsavel")
    @classmethod
    def not_blank(cls, value: str):
        if not value.strip():
            raise ValueError("responsável não pode conter apenas espaços")
        return value.strip()

class ChamadoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    titulo: str
    descricao: str
    prioridade: Prioridade
    status: Status
    responsavel: str | None
    criado_em: datetime
