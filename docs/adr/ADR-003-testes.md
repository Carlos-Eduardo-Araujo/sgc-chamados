# ADR-003 - Test Harness com pytest
## Contexto
É obrigatório possuir infraestrutura automatizada cobrindo cenários principais e edge cases.
## Decisão
Usar pytest com FastAPI TestClient e banco SQLite em memória isolado por teste.
## Alternativas consideradas
unittest e testes exclusivamente manuais.
## Consequências
Execução simples (`pytest`), isolamento e boa integração com GitHub Actions e Docker.
