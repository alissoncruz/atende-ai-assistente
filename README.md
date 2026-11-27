# AtendeAI

Plataforma SaaS de atendimento e vendas via WhatsApp com IA para pequenos negócios.

## Status
Estrutura arquitetural inicial — sem regras de negócio implementadas.

## Arquitetura
- Modular Monolith
- Hexagonal Architecture (Ports & Adapters)
- Domain-Driven Design (DDD)
- SOLID e Dependency Inversion
- Domain Events
- CQRS seletivo
- Anti-Corruption Layer
- Testabilidade e Clean Code

## Módulos
Identity & Access, WhatsApp, AI/Atendimento, CRM/Leads, Scheduling, Follow-up, Analytics, Billing e Onboarding.

Veja [ARCHITECTURE.md](ARCHITECTURE.md) e [MODULES.md](MODULES.md).

## Contexto de IA

Regras, skills e o gancho de modelo do Cursor estão no repositório exclusivo [ai-toolkit-minions](https://github.com/alissoncruz/ai-toolkit-minions).
