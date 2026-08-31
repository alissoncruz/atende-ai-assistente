# Estratégia de testes

## Pirâmide

- **Domain:** maior cobertura, testes unitários rápidos e sem infraestrutura.
- **Application:** casos de uso, ports e orquestração.
- **Adapters:** testes de integração para banco, APIs e mensageria.
- **API:** contratos e integrações dos endpoints críticos.

O domínio não deve precisar subir Spring, banco ou containers para ser testado.

Adicionar testes arquiteturais para impedir dependências indevidas e ciclos entre módulos.
