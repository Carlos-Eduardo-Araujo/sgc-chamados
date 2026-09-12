# ADR-004 - Agente de IA
## Contexto
A atividade exige configuração e uso documentado de ao menos um agente de auxílio/geração de código.
## Decisão
Adotar Codex CLI como agente de referência e manter regras independentes em `.ai/`.
## Alternativas consideradas
Cursor, Claude Code e Antigravity.
## Consequências
As instruções ficam versionadas e auditáveis. A execução real do agente deve ser registrada pela equipe como evidência; este repositório não falsifica sessões de uso.
