# ADR-001 - Stack tecnológica
## Contexto
A entrega exige ambiente reproduzível, SDD e testes automatizados, sem necessidade de grande interface.
## Decisão
Usar Python 3.12, FastAPI, SQLAlchemy, SQLite e pytest.
## Alternativas consideradas
Node/Express e Django REST Framework.
## Consequências
Stack enxuta, documentação automática da API e baixo custo de configuração; SQLite é adequado à entrega inicial, mas não representa escolha final para alta escala.
