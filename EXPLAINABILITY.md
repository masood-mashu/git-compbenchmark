# Explainability & Governance Statement

## Decision Architecture
GitCompBenchmark evaluates compensation offers through mathematical parity modeling. When an offer package is proposed, the agent divides proposed base pay by band midpoint to determine compa-ratio. If an offer exceeds upper quartile thresholds or causes pay compression with existing tenured peers, the agent flags the requisition for review.

## Input Data Provenance
Data inputs include Radford/Mercer market comp surveys, HRIS employee compensation tables, candidate offer sheets, and regional pay transparency statutes.

## Operational Limits & Non-Goals
GitCompBenchmark analyzes quantitative salary, bonus, and equity data; it does not evaluate qualitative interview chemistry or culture add.
