# Evidências

Esta pasta reúne referências às evidências reais produzidas durante o desenvolvimento do projeto.

## Evidências disponíveis

### Testes locais

A suíte foi executada com:

```bash
python -m pytest

```

Resultado:

```text
16 passed, 9 warnings

```

O resultado também está registrado em:
`docs/test-results/pytest.log`

### Relatório JUnit

O relatório automatizado está disponível em:
`docs/test-results/junit.xml`

### GitHub Actions

O CI foi executado pelo GitHub Actions e apresentou checks aprovados nas Pull Requests.
A validação Docker também foi executada pelo GitHub Actions por meio do workflow:
`.github/workflows/docker.yml`

### GitHub Projects

O projeto possui Issues organizadas em um GitHub Project, permitindo acompanhar as etapas de desenvolvimento.

### Pull Requests

As integrações foram realizadas por Pull Requests entre branches de desenvolvimento e a branch develop.

### Agente de IA

As regras e prompts utilizados pelo agente estão versionados em:

* `.ai/instructions/`
* `.ai/prompts/`

### Regra de integridade

Nenhum print, log, commit, Pull Request, aprovação, teste ou execução deve ser apresentado como evidência se não tiver ocorrido realmente.
