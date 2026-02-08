# ARC Raiders Event Tracker

Tracker de eventos em tempo real para **ARC Raiders**.

Este projeto monitora a agenda de eventos do jogo através da API pública do MetaForge, processa os dados e identifica:

- Eventos ativos no momento
- Próximos eventos
- Mudanças de estado (início / término)

O objetivo é evoluir para um sistema completo com:

- Alertas automáticos (ex.: Discord)
- Cache de estado
- Monitoramento contínuo

O desenvolvimento segue **TDD (Test Driven Development)** e boas práticas de arquitetura em Python.

---

## Ideia Geral do Projeto

O sistema é estruturado em camadas:

- **Domain** → Modelos e regras de negócio (Event)
- **Services** → Lógica de processamento de eventos
- **Infra** → Integração com API externa
- **Scheduler** (futuro) → Monitoramento periódico
- **Interface (Discord)** (futuro) → Alertas e comandos

Principais responsabilidades atuais:

- Converter dados da API em objetos de domínio
- Determinar eventos ativos
- Calcular tempo restante
- Garantir integridade temporal (UTC)

---

## Requisitos

- Python 3.12+
- Poetry

---

## Instalação

Clone o repositório:

```bash
git remote add origin https://github.com/amarcossousa/arc-raiders-tracker.git
cd arc-raiders-tracker
