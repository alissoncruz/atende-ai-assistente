# Plano: página de login

Data: 2026-11-27
Repositório: produto
Status: proposto

## Objetivo

Uma página pede usuário e senha, e a Identity aceita ou recusa.

## Fora de escopo

Cadastro, recuperação de senha, papéis, OAuth, WhatsApp e o restante do MVP.

## Módulos

Só a Identity muda. `apps/api` serve a página e guarda a sessão. Os outros módulos ficam como estão.

## Passos

1. A Identity guarda um usuário e a senha.
2. A página envia usuário e senha ao caso de uso.
3. Senha certa abre a sessão. Senha errada permanece na página e mostra a falha.

## Como provar

Teste de domínio: senha certa passa e senha errada falha, sem Spring. Na página, a senha certa entra e a senha errada fica na tela de login.

## Riscos

A senha não pode ir para o log. A sessão desta versão ainda não protege outras páginas.
