# Plano: chatbot de WhatsApp

Data: 2026-11-27
Repositório: produto
Status: proposto

## Objetivo

Receber uma mensagem de WhatsApp, entender o contexto e responder. É a fase 1 do MVP: Identity, WhatsApp e AI.

## Fora de escopo

CRM, agendamento, follow-up, analytics, billing e onboarding. Sem mídia, grupo, campanha ou tela.

## Módulos

Identity diz de quem é o número. WhatsApp recebe e envia. AI compreende e redige a resposta. Os outros módulos não entram.

## Passos

1. Identity guarda o tenant dono do número. Sem login completo.
2. O adapter de WhatsApp recebe o webhook, valida a origem e entrega um comando ao caso de uso. O domínio não vê HTTP nem o SDK do WhatsApp.
3. O caso de uso pede à porta de AI uma resposta para o texto recebido. A chamada ao modelo fica no adapter de AI.
4. O adapter de WhatsApp envia essa resposta para o mesmo número.
5. Teste de domínio: texto de entrada vira texto de saída, sem Spring.

## Como provar

Um teste do caso de uso com portas falsas: a mensagem "oi" produz uma resposta de texto. O domínio não importa Spring, WhatsApp nem SDK de IA.

## Riscos

Webhook sem validação aceita mensagem forjada. A resposta pode sair no tenant errado se o número não estiver ligado à Identity. O log não grava o texto da conversa.
