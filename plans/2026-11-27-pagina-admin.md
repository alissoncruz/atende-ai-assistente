# Plano: página inicial administrativa

Data: 2026-11-27
Repositório: produto
Status: proposto

## Objetivo

Uma página inicial administrativa agrupa as funcionalidades num menu. Feature nova com tela ganha um item nesse menu.

## Fora de escopo

Construir as funcionalidades, login, papéis, WhatsApp e o restante do MVP.

## Módulos

`apps/api` serve a página e guarda a lista do menu: nome e caminho. Nenhum módulo de negócio muda agora. A feature que vier depois acrescenta o próprio item nessa lista.

## Passos

1. A página abre e mostra a lista.
2. A lista começa vazia quando ainda não há outra tela.
3. Uma feature com página só termina quando o item dela está nessa lista.

## Como provar

Abrir a página mostra o menu. Incluir um item faz o nome aparecer. Remover o item tira o nome.

## Riscos

Dois lugares de menu fazem a página divergir. O item precisa entrar na mesma lista.
