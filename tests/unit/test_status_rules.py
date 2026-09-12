from app.schemas.chamado import Status
from app.services.chamado import TRANSICOES_VALIDAS

def test_rn01_aberto_pode_ir_para_em_andamento_ou_cancelado():
    assert TRANSICOES_VALIDAS[Status.ABERTO] == {Status.EM_ANDAMENTO, Status.CANCELADO}

def test_rn01_resolvido_nao_pode_mudar_de_status():
    assert TRANSICOES_VALIDAS[Status.RESOLVIDO] == set()
