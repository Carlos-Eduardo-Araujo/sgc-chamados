# Entrega Inicial - Ambiente, Especificação Técnica e Test Harness

## 1. Identificação
- Disciplina: [NOME DA DISCIPLINA]
- Professor: [PROFESSOR]
- Projeto: SGC - Sistema de Gerenciamento de Chamados
- Integrante 1: [NOME DO ALUNO 1] - RA [RA DO ALUNO 1]
- Integrante 2: [NOME DO ALUNO 2] - RA [RA DO ALUNO 2]

## 2. Repositório
[LINK DO GITHUB]

## 3. Problema e solução
O projeto trata a falta de rastreabilidade de solicitações de suporte mantidas em mensagens ou planilhas. A solução é uma API REST para registrar, consultar e acompanhar chamados com estados e prioridades controlados.

## 4. Arquitetura
Arquitetura em camadas: FastAPI Routes -> Services -> Repositories -> SQLAlchemy -> SQLite, com schemas Pydantic para contratos e validação.

## 5. SDD
A especificação em `docs/specification/specification.md` define RF01-RF07, RNF01-RNF06 e RN01-RN07, contratos HTTP, decomposição e arquitetura. O código e os testes foram estruturados para rastrear esses itens.

## 6. Agente de IA
Agente escolhido: Codex CLI. Regras versionadas em `.ai/instructions` e prompts em `.ai/prompts`. O agente deve ler a especificação antes de mudanças e validar alterações com testes.

## 7. Ambiente
- Python 3.12
- FastAPI
- SQLAlchemy + SQLite
- pytest
- Docker / Docker Compose
- GitHub Actions

## 8. Test Harness
Execução local: `pytest --junitxml=docs/test-results/junit.xml`
Execução Docker: `docker compose run --rm tests`
O relatório JUnit é gerado em `docs/test-results/junit.xml`.

## 9. Testes
A suíte cobre criação, listagem, consulta, fluxo válido e inválido de status, alteração de prioridade, atribuição de responsável, dados inválidos, recurso inexistente e bloqueio de alteração em chamados encerrados.

## 10. Evidências a inserir antes da submissão
**AÇÃO NECESSÁRIA PELO ALUNO:** inserir prints reais de:
1. Repositório público e árvore de arquivos.
2. Branches `main`, `develop` e `feature/*`.
3. GitHub Project/Issues com divisão da sprint.
4. Pull Request com comentários e aprovação de outro integrante.
5. Configuração/uso real do agente de IA.
6. `docker compose up` com API em execução.
7. `docker compose run --rm tests` ou `pytest` com suíte aprovada.
8. Artefato/relatório JUnit.
9. GitHub Actions concluído com sucesso.

## 11. Conclusão
A solução contempla governança Git, especificação SDD, ambiente padronizado, regras de agente de IA e Test Harness automatizado. Evidências dependentes do GitHub/equipe devem ser produzidas pela equipe e não são falsificadas neste material.
