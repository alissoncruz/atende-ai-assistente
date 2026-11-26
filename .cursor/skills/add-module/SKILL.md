---
name: add-module
description: Use somente ao criar um módulo Maven novo no monólito AtendeAI. Não use para editar código dentro de um módulo que já existe.
paths:
  - "pom.xml"
  - "modules/**/pom.xml"
  - "apps/**/pom.xml"
---

# Criar módulo

1. Confira o nome em `MODULES.md`. Artifact `atendeai-<nome>`, pacote `com.atendeai.<nome>`, pasta `modules/<nome>`.
2. Crie `modules/<nome>/pom.xml` com parent `com.atendeai:atendeai:0.1.0-SNAPSHOT` e `<relativePath>../../pom.xml</relativePath>`.
3. Inclua `<module>modules/<nome></module>` no `pom.xml` da raiz.
4. Crie a árvore vazia, com `.gitkeep`, espelhando `modules/identity`:
   - `domain/model`, `domain/service`, `domain/event`
   - `application/port/in`, `application/port/out`, `application/usecase`, `application/dto`
   - `adapters/in/rest`, `adapters/in/messaging`, `adapters/in/webhook`, `adapters/in/scheduler`
   - `adapters/out/persistence`, `adapters/out/messaging`, `adapters/out/external`
   - `configuration`
   - testes em `src/test/java/com/atendeai/<nome>/{domain,application,adapters}`
5. Não crie classe Java nem dependência de framework, a menos que a tarefa peça.
6. Rode `mvn -B -ntp -N install` e depois `mvn -B -ntp -pl modules/<nome> -am verify`.
