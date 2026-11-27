# Plano: chatbot de WhatsApp

Data: 2026-11-27
Repositório: produto
Status: proposto

## Objetivo

Receber um texto no WhatsApp e devolver um texto.

## Fora de escopo

Identity, modelo de IA, histórico, mídia, grupo, CRM e o restante do MVP.

## Módulos

Só o WhatsApp muda. Os outros módulos ficam como estão.

## Passos

1. O adapter recebe o webhook de texto e chama o caso de uso.
2. O caso de uso devolve uma resposta fixa para esse texto.
3. O adapter envia a resposta ao mesmo número.

## Como provar

Teste de domínio: "oi" devolve o texto fixo, sem Spring.

## Riscos

A resposta fixa não interpreta a mensagem. O log não grava o texto da conversa.
