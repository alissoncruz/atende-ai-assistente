# Arquitetura

## Visão geral

O AtendeAI começa como um **Modular Monolith**, com fronteiras explícitas entre módulos. Cada módulo segue Hexagonal Architecture.

```text
Adapters In
    |
    v
Application (Use Cases / Input Ports)
    |
    v
Domain (Entities / Value Objects / Services / Events)
    |
    v
Application (Output Ports)
    |
    v
Adapters Out (DB / APIs / Messaging)
```

## Regra de dependência

```text
Adapters -> Application -> Domain
```

O domínio não conhece Spring, banco, HTTP, AWS, WhatsApp ou provedor de IA.

## Estrutura

```text
atendeai/
├── apps/api/
├── modules/
│   ├── identity/
│   ├── whatsapp/
│   ├── ai/
│   ├── crm/
│   ├── scheduling/
│   ├── followup/
│   ├── analytics/
│   ├── billing/
│   ├── onboarding/
│   └── shared/
├── docs/
│   ├── architecture/
│   ├── adr/
│   └── modules/
└── pom.xml
```

## Estrutura interna de módulo

```text
module/
├── domain/
│   ├── model/
│   ├── service/
│   └── event/
├── application/
│   ├── port/in/
│   ├── port/out/
│   ├── usecase/
│   └── dto/
├── adapters/
│   ├── in/
│   │   ├── rest/
│   │   ├── messaging/
│   │   ├── webhook/
│   │   └── scheduler/
│   └── out/
│       ├── persistence/
│       ├── messaging/
│       └── external/
└── configuration/
```

## Patterns e princípios

### DDD
O domínio representa conceitos e regras reais do negócio.

### Ports & Adapters
Casos de uso dependem de interfaces; infraestrutura é substituível.

### Domain Events
Fatos relevantes podem ser publicados, por exemplo `LeadCaptured`, `AppointmentScheduled` e `ConversationTransferred`.

### CQRS
Aplicado somente quando separar leitura/escrita trouxer benefício real.

### Anti-Corruption Layer
Modelos de WhatsApp, IA e pagamentos ficam isolados do domínio.

### Transaction Boundary
Cada caso de uso define sua fronteira transacional. Evitar transações atravessando módulos indiscriminadamente.

## Comunicação entre módulos

Preferência:
1. contratos de aplicação para operações síncronas;
2. eventos para fatos assíncronos;
3. mensageria externa quando necessária.

**Nunca acessar diretamente o banco ou repository de outro módulo.**

## Evolução para microserviços

Um módulo só deve ser extraído quando houver necessidade concreta de escala independente, deploy independente, isolamento de falhas, tecnologia específica ou ownership independente.
