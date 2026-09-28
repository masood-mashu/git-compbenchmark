"""
pay_equity_parity_checker.py - Audits internal peer group salary variance to prevent demographic pay disparities
"""
import sys
import json


def check_pay_equity(salaries_json: str, max_allowed_gap_pct: float = 2.0):
    import json
    data = json.loads(salaries_json) if isinstance(salaries_json, str) else salaries_json
    a = data.get("group_a_mean", 100000.0)
    b = data.get("group_b_mean", 100000.0)
    gap = (abs(a - b) / max(min(a, b), 1.0)) * 100.0
    passed = gap <= max_allowed_gap_pct
    return {
        "group_a_mean": a,
        "group_b_mean": b,
        "pay_gap_pct": round(gap, 2),
        "equitable": passed,
        "status": "PAY_EQUITY_VERIFIED" if passed else "PAY_DISPARITY_ALERT"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "pay-equity-parity-checker"}))
