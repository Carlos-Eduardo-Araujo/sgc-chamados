# ADR-002 - Arquitetura em camadas
## Contexto
A especificação pede decomposição em unidades independentes e testáveis.
## Decisão
Separar routes, schemas, services, repositories, models e database.
## Alternativas consideradas
Arquivo único e arquitetura hexagonal completa.
## Consequências
Melhor testabilidade que arquivo único, sem complexidade excessiva de uma arquitetura mais pesada.
