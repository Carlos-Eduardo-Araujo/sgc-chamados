# SGC - Sistema de Gerenciamento de Chamados

Projeto acadêmico da **Entrega Inicial - Ambiente, Especificação Técnica e Test Harness**.

## Visão geral
O SGC é uma API REST para registrar e acompanhar chamados de suporte. O escopo foi deliberadamente mantido pequeno para demonstrar SDD, arquitetura testável, automação, reprodutibilidade e governança Git sem complexidade artificial.

## Problema solucionado
Solicitações mantidas em mensagens e planilhas dificultam rastreabilidade, prioridade e acompanhamento. O SGC centraliza esses dados e aplica regras explícitas de status.

## Objetivos
- Especificar o comportamento antes da implementação.
- Decompor a solução em unidades testáveis.
- Disponibilizar ambiente reproduzível.
- Automatizar validação por Test Harness.
- Documentar uso de agente de IA e governança GitHub.

## Tecnologias
Python 3.12, FastAPI, Pydantic, SQLAlchemy, SQLite, pytest, Docker, Docker Compose e GitHub Actions.

## Arquitetura
`Routes -> Services -> Repositories -> SQLAlchemy -> SQLite`, com schemas Pydantic para validação. Consulte `docs/adr/ADR-002-arquitetura.md`.

## Estrutura de pastas
```text
app/                aplicação
  routes/           endpoints HTTP
  services/         regras de negócio
  repositories/     persistência
  schemas/          contratos/validação
  models/           modelos SQLAlchemy
tests/              suíte automatizada
docs/specification/ especificação SDD
docs/refinement/    refinamento proposto
docs/adr/           decisões arquiteturais
docs/evidence/      evidências reais a coletar
docs/test-results/  relatórios do harness
.ai/                regras e prompts do agente
.github/             CI, issues e PR template
```

## Pré-requisitos
### Com Docker
Docker + Docker Compose.

### Sem Docker
Python 3.12 e pip.

## Instalação local
```bash
git clone [LINK DO GITHUB]
cd sgc-chamados
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

## Execução da aplicação
```bash
uvicorn app.main:app --reload
```
API: `http://localhost:8000`  
Swagger: `http://localhost:8000/docs`  
Health: `http://localhost:8000/health`

## Docker
```bash
docker compose build
docker compose up api
```

## Test Harness
O harness usa pytest + FastAPI TestClient e banco SQLite em memória por teste.

Execução local:
```bash
pytest
```

Com relatório JUnit:
```bash
pytest --junitxml=docs/test-results/junit.xml
```

Via ambiente padronizado:
```bash
docker compose run --rm tests
```

Sucesso: pytest termina sem falhas e retorna código 0. Falhas mostram teste, asserção e traceback. O relatório automatizado fica em `docs/test-results/junit.xml`.

## Matriz teste x requisito
| Teste/categoria | Requisito/regra | Resultado esperado |
|---|---|---|
| criação válida | RF01/RN01 | 201, status ABERTO |
| listagem com/sem dados | RF02 | 200 e lista coerente |
| consulta existente/inexistente | RF03 | 200 / 404 |
| fluxo de status | RF04/RN02-RN04 | 200 em transição válida |
| transição inválida | RN02-RN04 | 409 |
| prioridade | RF05/RN06 | 200 para prioridade válida |
| responsável | RF06 | 200 com responsável |
| entradas inválidas | RF07/RN07 | 422 |
| alterar encerrado | RN05 | 409 |
| health | RNF05 | 200 `{status: ok}` |

## SDD
A fonte técnica é `docs/specification/specification.md`. O fluxo esperado é:
1. Selecionar requisito.
2. Revisar contrato e regras.
3. Criar/ajustar teste.
4. Implementar a menor alteração coerente.
5. Executar harness.
6. Atualizar documentação se o comportamento mudou.
7. Abrir PR para revisão.

## Refinamento
`docs/refinement/refinement.md` registra um **cenário de revisão proposto**, sem afirmar reuniões inexistentes.

## Agente de IA
Agente de referência: **Codex CLI**. As regras ficam em `.ai/instructions/` e os prompts em `.ai/prompts/`. O agente não deve modificar requisitos silenciosamente, remover testes para obter sucesso ou declarar execuções inexistentes.

### Uso sugerido do agente
1. Instalar/configurar o Codex CLI conforme a documentação oficial disponível no ambiente da equipe.
2. Fornecer ao agente `docs/specification/specification.md` e `.ai/instructions/*` como contexto.
3. Usar os prompts versionados.
4. Registrar uma evidência real da utilização para a submissão.

## Git/GitHub e branching
- `main`: versão estável, protegida.
- `develop`: integração da sprint.
- `feature/*`: desenvolvimento independente.

Fluxo: Issue -> `feature/*` -> commits -> Pull Request para `develop` -> revisão/aprovação -> merge -> PR `develop` para `main`.

**Não usar commits diretos na `main` como fluxo normal.** Configurar proteção de branch no GitHub quando possível.

## Issues / Project - backlog inicial sugerido
| Issue | Tarefa | Requisito | Responsável |
|---|---|---|---|
| #1 | Estruturar repositório e branches | Governança | [INTEGRANTE] |
| #2 | Especificação SDD | RF/RNF/RN | [INTEGRANTE] |
| #3 | Implementar criação/listagem/consulta | RF01-RF03 | [INTEGRANTE] |
| #4 | Implementar regras de status | RF04/RN01-RN04 | [INTEGRANTE] |
| #5 | Prioridade e responsável | RF05-RF06/RN05-RN06 | [INTEGRANTE] |
| #6 | Validações e edge cases | RF07/RN07 | [INTEGRANTE] |
| #7 | Test Harness | RNF02 | [INTEGRANTE] |
| #8 | Docker | RNF01/RNF04 | [INTEGRANTE] |
| #9 | CI e evidências | Entrega | [INTEGRANTE] |
| #10 | Revisão final e PDF | Entrega | [INTEGRANTE] |

## Pull Requests e Code Review
Use `.github/pull_request_template.md`. Todo PR deve apontar requisito/Issue, informar testes, receber comentário/revisão e aprovação de outro integrante antes do merge.

## ADRs
- ADR-001: stack tecnológica.
- ADR-002: arquitetura em camadas.
- ADR-003: pytest como harness.
- ADR-004: agente de IA.

## CI
`.github/workflows/ci.yml` executa testes em push/PR para `develop` e `main` e publica `junit.xml` como artefato.

## Evidências
Somente evidências reais devem ser adicionadas em `docs/evidence/`. Consulte `docs/evidence/README.md` e `docs/submission/entrega-inicial.md`.

## Integrantes
- [NOME DO ALUNO 1] - [RA DO ALUNO 1]
- [NOME DO ALUNO 2] - [RA DO ALUNO 2]

## Comandos importantes
```bash
uvicorn app.main:app --reload
pytest
pytest --junitxml=docs/test-results/junit.xml
docker compose build
docker compose up api
docker compose run --rm tests
```

## Status da entrega
Código, documentação, Test Harness, Docker e CI estão preparados neste pacote. A suíte foi executada localmente neste ambiente em 08/09/2026, com **16 testes aprovados**; o log real está em `docs/test-results/pytest.log` e o JUnit em `docs/test-results/junit.xml`. A equipe ainda precisa criar a governança real no GitHub, executar Docker/CI em seu ambiente, registrar uso real do agente, coletar evidências e preencher os dados de identificação.
