# Entrega Inicial - Ambiente, Especificação Técnica e Test Harness

## 1. Identificação

- Disciplina: [NOME DA DISCIPLINA]
- Professor: [NOME DO PROFESSOR]
- Projeto: SGC - Sistema de Gerenciamento de Chamados
- Integrante: [NOME COMPLETO DO ALUNO] - RA [RA]

## 2. Repositório

https://github.com/Carlos-Eduardo-Araujo/sgc-chamados

## 3. Problema e solução

O projeto trata a falta de rastreabilidade de solicitações de suporte mantidas em mensagens ou planilhas.

A solução desenvolvida é uma API REST para registrar, consultar e acompanhar chamados, utilizando estados e prioridades controlados por regras de negócio.

## 4. Arquitetura

A aplicação utiliza arquitetura em camadas:

FastAPI Routes -> Services -> Repositories -> SQLAlchemy -> SQLite

Os schemas Pydantic são utilizados para validação dos contratos de entrada e saída.

## 5. Especificação Técnica (SDD)

A especificação localizada em `docs/specification/specification.md` define:

- RF01-RF07: requisitos funcionais;
- RNF01-RNF06: requisitos não funcionais;
- RN01-RN07: regras de negócio;
- contratos de entrada e saída;
- decomposição da solução em unidades testáveis;
- arquitetura e responsabilidades dos componentes.

A implementação e os testes foram organizados para permitir a validação dos requisitos definidos.

## 6. Refinamento por feedback e testes

Durante o desenvolvimento foram realizados ajustes na especificação e na implementação a partir da validação automatizada.

Um caso concreto ocorreu na alteração do endpoint `/health`: após a inclusão dos campos `service` e `version`, o teste existente passou a falhar porque ainda esperava somente `{"status": "ok"}`.

O teste foi então atualizado para validar o novo contrato completo do endpoint.

Após o ajuste, a suíte voltou a apresentar resultado aprovado:

`16 passed`

O histórico detalhado encontra-se em `docs/refinement/refinement.md`.

## 7. Agente de IA

Agente adotado no projeto: Codex CLI.

As regras e orientações utilizadas no desenvolvimento estão versionadas no repositório:

- `.ai/instructions/`
- `.ai/prompts/`

As instruções orientam o agente a considerar a especificação, arquitetura, padrões de código e testes antes de propor alterações.

## 8. Ambiente e execução

Ambiente padronizado do projeto:

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- pytest
- Docker
- Docker Compose
- GitHub Actions

Execução local dos testes utilizada durante o desenvolvimento:

```bash
###python -m pytest

###Resultado real obtido:

###16 passed, 9 warnings

###O ambiente Docker foi validado pelo GitHub Actions por meio do workflow específico da branch feature/docker.

## 9. Test Harness

O Test Harness utiliza `pytest` e `FastAPI TestClient`.

A suíte contempla, entre outros:

- criação de chamados;
- listagem;
- consulta por ID;
- alteração de status;
- fluxo válido e inválido de status;
- alteração de prioridade;
- atribuição de responsável;
- validação de dados;
- recurso inexistente;
- bloqueio de alterações em chamados encerrados;
- contrato do endpoint `/health`.

Também existe relatório JUnit em:

`docs/test-results/junit.xml`

e registro da execução em:

`docs/test-results/pytest.log`

## 10. Governança Git e GitHub

O projeto utiliza:

- branch `main`;
- branch `develop`;
- branches de trabalho `feature/*`;
- Pull Requests para integração;
- GitHub Issues;
- GitHub Projects;
- GitHub Actions;
- proteção da branch principal.

O desenvolvimento foi realizado individualmente. Portanto, não foi registrada aprovação fictícia de outro integrante.

As Pull Requests utilizadas no desenvolvimento documentam as integrações realizadas entre as branches.

## 11. Evidências

As evidências da entrega devem corresponder exclusivamente a execuções e configurações reais.

São utilizadas evidências de:

- repositório público;
- branches;
- GitHub Projects e Issues;
- Pull Requests;
- GitHub Actions;
- execução local dos testes;
- resultado do Test Harness;
- validação Docker pelo GitHub Actions;
- estrutura de documentação;
- arquivos de regras e prompts do agente de IA.

## 12. Conclusão

O projeto contempla os elementos solicitados para a Entrega Inicial:

- governança Git;
- especificação técnica SDD;
- requisitos funcionais e não funcionais;
- regras de negócio;
- contratos de entrada e saída;
- arquitetura em camadas;
- agente de IA e arquivos de contexto;
- Test Harness automatizado;
- Docker e Docker Compose;
- GitHub Actions;
- documentação e evidências.

As evidências finais apresentadas na submissão devem ser somente aquelas efetivamente produzidas durante o desenvolvimento.