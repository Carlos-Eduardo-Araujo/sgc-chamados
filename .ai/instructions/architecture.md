# Regras de arquitetura
- Routes tratam HTTP e delegam regras ao Service.
- Service concentra regras de negócio.
- Repository concentra persistência.
- Schemas concentram validação de payload.
- Models representam persistência.
- Não acessar SQL diretamente nas rotas.
- Não colocar regra de negócio em testes para fazê-los passar artificialmente.
