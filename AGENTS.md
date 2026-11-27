# AtendeAI

Monólito modular em Java 21 e Maven. A aplicação ainda não tem caso de uso executável.

- Invariantes e economia de tokens estão em `.cursor/rules/`. Siga as duas regras sempre ligadas.
- O índice de leitura está em https://github.com/alissoncruz/ai-toolkit-minions/blob/main/knowledge/INDEX.md. Abra só o arquivo indicado.
- Módulo novo: skill `add-module`. Caso de uso: skill `add-use-case`.
- Dependência: adapters → application → domain. Domínio sem Spring, banco, HTTP, WhatsApp ou SDK de IA.
- Módulo não acessa tabela nem repositório de outro. Síncrono por porta. Assíncrono por domain event.
- Teste de domínio sem Spring. Log sem texto de conversa e sem credencial.
- Tarefa simples não abre subagente e não usa Opus, Fable, GPT-5, `fast`, `xhigh` ou `max`.
- Feature, caso de uso ou módulo novo: skill `plan-feature` e `Status: proposto`. Código só com a linha `Status: aceito`, editada pela pessoa.
