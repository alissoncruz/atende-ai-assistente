# Plano: teste fácil da aplicação

Data: 2026-11-27
Repositório: produto
Status: proposto

## Objetivo

Um comando sobe a API e roda os testes de integração dos adapters e dos endpoints.

## Fora de escopo

Teste de domínio, CI/CD, outra nuvem, WhatsApp, login e página administrativa.

## Módulos

Um script na raiz. `apps/api` sobe nesse comando. Os testes de adapter e de contrato da API usam banco, API externa e mensageria locais, e desligam no fim. Nenhum módulo de negócio muda agora.

## Passos

1. `scripts/testar-aplicacao.sh` sobe a API e as dependências locais.
2. O teste de API chama o endpoint e confere o contrato.
3. O teste de adapter exercita banco, API externa e mensageria.
4. O teste de domínio continua sem Spring e fora desse comando.

## Como provar

O script termina verde numa máquina limpa, sem instalar banco ou broker à mão. Um teste de domínio segue sem container.

## Riscos

Subir a aplicação deixa o teste lento. Segredo de integração não entra no repositório. Enquanto não houver endpoint, o script só prova que a API sobe.
