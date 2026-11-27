---
name: add-use-case
description: Use somente ao adicionar um caso de uso hexagonal num módulo AtendeAI (porta de entrada, use case e teste de domínio). Não use para typo, rename, POM ou ajuste de texto.
paths:
  - "**/src/main/java/**/*.java"
  - "**/src/test/java/**/*.java"
---

# Criar caso de uso

1. Abra o plano em `plans/`. Sem a linha `Status: aceito`, pare e use a skill `plan-feature`. Não altere esse status.
2. Confirme o módulo dono. Se outro módulo entra na história, leia só `docs/architecture/BOUNDARIES.md`.
3. Nomeie o caso com a linguagem do negócio.
4. Porta de entrada em `application/port/in`. Implementação em `application/usecase`, dependendo da porta.
5. Porta de saída em `application/port/out` só se o caso precisar sair do módulo ou persistir.
6. Tipo de domínio só se houver invariante. Ele fica em `domain` e não importa framework.
7. Teste de domínio ou do caso de uso em `src/test/java`, sem Spring e sem banco.
8. Não crie adapter REST, JPA ou cliente externo, a menos que a tarefa peça.
9. Não chame repositório de outro módulo. Integração síncrona é porta; fato já ocorrido é domain event.
