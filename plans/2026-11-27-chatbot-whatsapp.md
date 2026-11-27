# Plano: chatbot de WhatsApp

Data: 2026-11-27
Repositório: produto
Status: proposto

## Objetivo

Receber um texto no WhatsApp, devolver um texto e mostrar essa troca numa página.

## Fora de escopo

Identity, login, modelo de IA, mídia, grupo, CRM e o restante do MVP.

## Módulos

WhatsApp guarda as falas e envia a resposta. `apps/api` serve uma página que só lê essas falas. Os outros módulos ficam como estão.

## Passos

1. O adapter recebe o webhook de texto e chama o caso de uso.
2. O caso de uso devolve uma resposta fixa e guarda as duas falas: a do cliente e a do chat, com o número.
3. O adapter envia a resposta ao mesmo número.
4. Uma página lista o número, a fala do cliente e a fala do chat.

## Como provar

Teste de domínio: "oi" devolve o texto fixo e as duas falas ficam disponíveis para leitura, sem Spring. Abrir a página mostra essas falas.

## Riscos

A resposta fixa não interpreta a mensagem. A página não tem login, então quem abre a URL vê o texto. O log não grava a conversa.
