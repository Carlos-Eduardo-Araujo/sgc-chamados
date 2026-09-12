# Refinamento por Feedback

Este documento não afirma que reuniões ou revisões externas ocorreram. Ele registra um **cenário de validação/revisão proposto**, conforme permitido pela documentação da entrega.

## Versão inicial
A proposta inicial previa somente criação, listagem e alteração livre de status de chamados.

## Pontos identificados no cenário de revisão
1. Alteração livre de status permitiria pular etapas sem controle.
2. Chamados encerrados ainda poderiam ser alterados, prejudicando consistência.
3. Não havia endpoint simples para verificar disponibilidade da aplicação.
4. Não havia limites explícitos para tamanho dos campos.

## Alterações realizadas
- Foram definidas transições de status permitidas (RN02-RN04).
- Foi proibida alteração de prioridade/responsável após encerramento (RN05).
- Foi criado `/health` (RNF05).
- Foram definidos limites e validações de título/descrição/responsável (RN07/RF07).

## Justificativa
As mudanças tornam o comportamento verificável por testes automatizados e evitam estados inconsistentes.

## Versão final
A versão final é a documentada em `docs/specification/specification.md` e implementada no código atual.
