<div align="center">

<img src="assets/laszlo-banner.png" alt="LASZLO" width="720" />

### Institutional on-chain alpha infrastructure

*From on-chain noise to executable alpha — on Base L2*

[![Whitepaper](https://img.shields.io/badge/Whitepaper-v2.0-FFB24D?style=for-the-badge&logo=readthedocs&logoColor=0B0D10)](https://wisdomechoes.net/blog/laszlo-whitepaper-v2)
[![Progress](https://img.shields.io/badge/Progress-2026-0B0D10?style=for-the-badge&logo=calendar&logoColor=FFB24D)](https://wisdomechoes.net/blog/laszlo-status-2026-06)
[![Chain](https://img.shields.io/badge/Chain-Base_L2-0052FF?style=for-the-badge&logo=ethereum&logoColor=white)](https://base.org)
[![Site](https://img.shields.io/badge/Site-wisdomechoes.net-15181D?style=for-the-badge&logo=firefoxbrowser&logoColor=FFB24D)](https://wisdomechoes.net)

</div>

---

## Who we are

**LASZLO Quantification** builds closed-loop infrastructure for on-chain markets — the kind of system an operator actually runs, not another charting layer.

We are named after **Laszlo Hanyecz**, who executed the first real on-chain exchange. The point is not nostalgia; it is **execution discipline** in a world of noise.

---

## The gap

On-chain markets never sleep. Event volume is enormous; **signal density is not**.

Most products stop at visibility — alerts, dashboards, copy-trading shells. The hard problem remains:

> How do you turn filtered signal into **repeatable, risk-bounded execution** — with an audit trail?

Retail tooling is fragmented. Institutional workflows are slow to adapt to L2 reality. **LASZLO exists in that gap.**

---

## What we build

**LASZLO** is an alpha terminal and execution stack for EVM chains — **Base L2** first, architected to extend.

| Layer | Role |
|-------|------|
| **Ingest** | Low-latency on-chain event capture |
| **Infer** | Feature engineering + ML signal generation |
| **Execute** | Unified routing, position management, risk gates |
| **Learn** | Data flywheel — collect → label → retrain → deploy |

```text
┌─────────────┐     Redis Streams      ┌─────────────┐     signals      ┌─────────────┐
│  Ingestor   │ ────────────────────► │  Strategy   │ ───────────────► │  Executor   │
│   (Rust)    │      market_ticks     │  (Python)   │                  │   (Rust)    │
└─────────────┘                       └─────────────┘                  └─────────────┘
       │                                      │                                │
       └────────────────── Base L2 · Uniswap V3 ───────────────────────────────┘
```

**One pipeline. One operator surface. Risk before return.**

---

## Design principles

| Principle | What it means |
|-----------|----------------|
| **Signal over volume** | Only decision-grade data enters the loop |
| **Heterogeneous by design** | Rust where latency matters; Python where research velocity matters |
| **Risk-first execution** | Automated stops, conservative entry policy, operator kill-switches |
| **Infrastructure, not hype** | Built to harden and measure — not to demo |

We are **not** a block explorer, a meme signal channel, or a copy-trading app.

---

## Stack at a glance

| | |
|---|---|
| Ingestion & execution | **Rust** |
| Strategy & ML | **Python** |
| Message bus | **Redis Streams** |
| Target chain | **Base L2** (EVM-extensible) |
| DEX focus | **Uniswap V3** spot |
| Orchestration | **Docker Compose** |

---

## Where we are

LASZLO is in **active engineering** on Base L2: the full ingest → signal → execute loop is implemented. Current work centers on data quality, model calibration, and production hardening.

We ship like an infrastructure team — **measurable pipelines, explicit risk gates, reproducible research cycles**.

---

## Read more

| | |
|---|---|
| 📄 **Whitepaper v2** | [wisdomechoes.net/blog/laszlo-whitepaper-v2](https://wisdomechoes.net/blog/laszlo-whitepaper-v2) |
| 📈 **Engineering progress** | [wisdomechoes.net/blog/laszlo-status-2026-06](https://wisdomechoes.net/blog/laszlo-status-2026-06) |
| 🌐 **Home** | [wisdomechoes.net](https://wisdomechoes.net) |

---

## Open vs. private

This organization maintains **public research and brand artifacts** here on GitHub.

Core engineering repositories are **private during active development**. Follow **[@LASZLO-Quantification](https://github.com/LASZLO-Quantification)** for selective public releases, design notes, and partner-facing tooling as we open the stack.

*Interested in early access or research collaboration? Reach out via [wisdomechoes.net](https://wisdomechoes.net).*

---

<div align="center">

<img src="assets/laszlo-mark.png" alt="LASZLO mark" width="64" />

**LASZLO** · *Signal to execution*

</div>
