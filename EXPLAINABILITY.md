# GitCompBenchmark Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitCompBenchmark** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitCompBenchmark consumes market salary survey datasets, internal HRIS compensation bands, candidate offer requisitions, and statutory pay transparency disclosure mandates. These data sources include proposed base salaries, job family band midpoints, peer demographic compensation distributions, and regional statutory minimums. The agent ingests these inputs in raw JSON, CSV, and HRIS export format and parses them into standardized total rewards equity models for downstream compliance analysis. Equal pay audit archives and executive incentive guidelines are also monitored as sensitive data sources to ensure equitable compensation is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When an employment offer requisition is processed, the agent first evaluates salary positioning using the compa-ratio-calculator tool to verify that the proposed pay falls within the 0.80 to 1.20 band midpoint corridor. Next, the reasoning engine invokes the pay-equity-parity-checker tool to audit peer team compensation distributions and detect potential demographic wage disparities exceeding 2.0%. Furthermore, statutory salary range text is compiled using the transparency-band-formatter tool. Finally, the agent correlates all compensation factors against predefined people policies to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated equity memo.

---

## 3. Constraints, Limitations, and Known Issues

GitCompBenchmark operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitCompBenchmark operates under strict operational constraints to prevent pay compression and statutory non-compliance across enterprise total rewards programs. The agent is deliberately limited to mathematical salary band analysis and equal pay auditing and cannot evaluate qualitative candidate interview performance. Another known issue and limitation is that complex multi-year equity grants with volatile vesting valuations may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
