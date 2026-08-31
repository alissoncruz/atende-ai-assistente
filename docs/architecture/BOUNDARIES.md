# Fronteiras dos módulos

Cada módulo é dono do próprio modelo e das próprias regras.

Nenhum módulo deve acessar diretamente entidades, repositories ou tabelas de outro módulo.

Exemplo síncrono:

```text
CRM -> Application Port -> Scheduling Contract
```

Exemplo assíncrono:

```text
Scheduling -> AppointmentScheduled -> Event Bus
                                      |-> Analytics
                                      |-> Follow-up
```

## Tenant isolation

Informações de negócio devem carregar contexto de tenant quando aplicável. A estratégia definitiva de isolamento será decidida antes da implementação da persistência.
