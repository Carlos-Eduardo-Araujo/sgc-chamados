def novo_chamado(client, prioridade="MEDIA"):
    return client.post("/chamados", json={
        "titulo": "Erro no sistema",
        "descricao": "Usuário não consegue acessar o painel principal.",
        "prioridade": prioridade,
    })

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["service"] == "sgc-chamados"
    assert response.json()["version"] == "1.0.0"

def test_rf01_criar_chamado_valido(client):
    response = novo_chamado(client, "ALTA")
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Erro no sistema"
    assert data["prioridade"] == "ALTA"
    assert data["status"] == "ABERTO"

def test_rf02_listar_chamados(client):
    novo_chamado(client)
    response = client.get("/chamados")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_rf02_lista_vazia(client):
    response = client.get("/chamados")
    assert response.status_code == 200
    assert response.json() == []

def test_rf03_consultar_chamado_existente(client):
    chamado_id = novo_chamado(client).json()["id"]
    response = client.get(f"/chamados/{chamado_id}")
    assert response.status_code == 200
    assert response.json()["id"] == chamado_id

def test_rf03_consultar_inexistente(client):
    response = client.get("/chamados/999")
    assert response.status_code == 404

def test_rf04_fluxo_status_valido(client):
    chamado_id = novo_chamado(client).json()["id"]
    r1 = client.patch(f"/chamados/{chamado_id}/status", json={"status": "EM_ANDAMENTO"})
    assert r1.status_code == 200
    assert r1.json()["status"] == "EM_ANDAMENTO"
    r2 = client.patch(f"/chamados/{chamado_id}/status", json={"status": "RESOLVIDO"})
    assert r2.status_code == 200
    assert r2.json()["status"] == "RESOLVIDO"

def test_rn01_transicao_status_invalida(client):
    chamado_id = novo_chamado(client).json()["id"]
    response = client.patch(f"/chamados/{chamado_id}/status", json={"status": "RESOLVIDO"})
    assert response.status_code == 409

def test_rf05_alterar_prioridade(client):
    chamado_id = novo_chamado(client).json()["id"]
    response = client.patch(f"/chamados/{chamado_id}/prioridade", json={"prioridade": "CRITICA"})
    assert response.status_code == 200
    assert response.json()["prioridade"] == "CRITICA"

def test_rf06_atribuir_responsavel(client):
    chamado_id = novo_chamado(client).json()["id"]
    response = client.patch(f"/chamados/{chamado_id}/responsavel", json={"responsavel": "Equipe N1"})
    assert response.status_code == 200
    assert response.json()["responsavel"] == "Equipe N1"

def test_rf07_rejeitar_titulo_vazio(client):
    response = client.post("/chamados", json={"titulo": "   ", "descricao": "Descrição válida", "prioridade": "MEDIA"})
    assert response.status_code == 422

def test_rf07_rejeitar_descricao_curta(client):
    response = client.post("/chamados", json={"titulo": "Falha válida", "descricao": "abc", "prioridade": "MEDIA"})
    assert response.status_code == 422

def test_rf07_rejeitar_prioridade_invalida(client):
    response = novo_chamado(client, "URGENTE")
    assert response.status_code == 422

def test_rn02_impedir_alteracao_de_chamado_encerrado(client):
    chamado_id = novo_chamado(client).json()["id"]
    client.patch(f"/chamados/{chamado_id}/status", json={"status": "CANCELADO"})
    response = client.patch(f"/chamados/{chamado_id}/prioridade", json={"prioridade": "ALTA"})
    assert response.status_code == 409


def test_rf07_rejeitar_titulo_curto_apos_remover_espacos(client):
    response = client.post("/chamados", json={
        "titulo": "  a  ",
        "descricao": "Descrição válida",
        "prioridade": "MEDIA",
    })
    assert response.status_code == 422
    assert client.get("/chamados").json() == []


def test_rf07_rejeitar_descricao_curta_apos_remover_espacos(client):
    response = client.post("/chamados", json={
        "titulo": "Título válido",
        "descricao": "    a",
        "prioridade": "MEDIA",
    })
    assert response.status_code == 422
    assert client.get("/chamados").json() == []


def test_rf06_rejeitar_responsavel_curto_apos_remover_espacos(client):
    chamado_id = novo_chamado(client).json()["id"]
    response = client.patch(
        f"/chamados/{chamado_id}/responsavel",
        json={"responsavel": "  a  "},
    )
    assert response.status_code == 422
    detalhe = client.get(f"/chamados/{chamado_id}").json()
    assert detalhe["responsavel"] is None


def test_rn02_aberto_pode_ser_cancelado(client):
    chamado_id = novo_chamado(client).json()["id"]
    response = client.patch(
        f"/chamados/{chamado_id}/status",
        json={"status": "CANCELADO"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "CANCELADO"


def test_rn03_em_andamento_pode_ser_cancelado(client):
    chamado_id = novo_chamado(client).json()["id"]
    client.patch(f"/chamados/{chamado_id}/status", json={"status": "EM_ANDAMENTO"})
    response = client.patch(
        f"/chamados/{chamado_id}/status",
        json={"status": "CANCELADO"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "CANCELADO"


def test_rn04_cancelado_e_estado_final(client):
    chamado_id = novo_chamado(client).json()["id"]
    client.patch(f"/chamados/{chamado_id}/status", json={"status": "CANCELADO"})
    response = client.patch(
        f"/chamados/{chamado_id}/status",
        json={"status": "EM_ANDAMENTO"},
    )
    assert response.status_code == 409


def test_rn04_resolvido_e_estado_final(client):
    chamado_id = novo_chamado(client).json()["id"]
    client.patch(f"/chamados/{chamado_id}/status", json={"status": "EM_ANDAMENTO"})
    client.patch(f"/chamados/{chamado_id}/status", json={"status": "RESOLVIDO"})
    response = client.patch(
        f"/chamados/{chamado_id}/status",
        json={"status": "CANCELADO"},
    )
    assert response.status_code == 409


def test_rn05_resolvido_nao_permite_alterar_responsavel(client):
    chamado_id = novo_chamado(client).json()["id"]
    client.patch(f"/chamados/{chamado_id}/status", json={"status": "EM_ANDAMENTO"})
    client.patch(f"/chamados/{chamado_id}/status", json={"status": "RESOLVIDO"})
    response = client.patch(
        f"/chamados/{chamado_id}/responsavel",
        json={"responsavel": "Equipe N2"},
    )
    assert response.status_code == 409
