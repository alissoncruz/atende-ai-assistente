# ai-toolkit-atende

Este repositório é o contexto do Cursor para os projetos Atende. Não é a aplicação.

- Edite regras, skills e o gancho de modelo aqui.
- Rode `scripts/sync-into-project.sh <raiz-do-produto>` para publicar a cópia em `.cursor/` do produto.
- Leia `knowledge/INDEX.md` e abra só o arquivo da tarefa.
- Tarefa simples: faça no turno, sem subagente e sem modelo caro. A regra está em `.cursor/rules/token-economy.mdc`.
- Arquitetura herdada: monólito modular, hexagonal, DDD por módulo, CQRS só quando a leitura pedir. Domínio sem framework.
