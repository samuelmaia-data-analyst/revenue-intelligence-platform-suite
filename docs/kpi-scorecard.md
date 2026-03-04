# KPI Scorecard - Revenue and Retention

## How To Use

- Atualize semanalmente os valores atuais.
- Revise metas mensalmente com leadership.
- Mantenha owner e plano de acao para cada KPI fora da meta.

## Executive KPIs

| KPI | Formula | Baseline | Target 6M | Target 12M | Current | Status | Owner |
|---|---|---:|---:|---:|---:|---|---|
| Net Revenue Retention (NRR) | (MRR retained + expansion - contraction) / starting MRR | 86.69% | 90.00% | 94.00% | 86.69% | Risk | Revenue Lead |
| Gross Revenue Churn | lost revenue / starting revenue | 13.31% | 10.50% | 8.00% | 13.31% | Risk | Retention Lead |
| Churn Model Precision@K | true churn in top-K / K | 0.62 | 0.70 | 0.78 | 0.62 | Risk | ML Lead |
| Action Adoption Rate | actions executed / actions recommended | 28% | 45% | 60% | 28% | Risk | CRM Ops |
| Incremental Revenue | observed uplift - control group | $0 | $120K | $350K | $0 | Off Track | Growth Lead |
| Time-to-Insight | tempo da ingestao ate insight acionavel | 2 days | 8 hours | 2 hours | 2 days | Risk | Analytics Eng |
| Data Contract Pass Rate | contracts aprovados / total contracts | 92% | 97% | 99% | 92% | Risk | Data Platform |
| Pipeline Reliability | runs bem-sucedidos / runs totais | 95% | 98% | 99.5% | 95% | Risk | Data Platform |

## Baseline Notes

- Baseline values marked here are initial executive targets for steering cadence.
- Replace with production telemetry after first monthly review cycle.
- Recommended refresh cadence: weekly `Current`, monthly `Target` review.

## Weekly Review Block (Template)

### Wins

- Monorepo consolidation completed with 5 integrated modules.
- Executive dashboard baseline running with unified architecture narrative.

### Risks

- KPI telemetry still partially manual in some modules.
- Action adoption depends on playbook rollout in CRM/Sales ops.

### Decisions Needed

- Approve retention campaign budget for top-risk segments.
- Approve owner allocation for KPI data automation.

### Actions Next 7 Days

- Connect scorecard KPIs to automated metric exports in CI artifacts.
- Publish executive dashboard demo URL in flagship README.
