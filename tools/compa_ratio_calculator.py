"""
compa_ratio_calculator.py - Calculates compa-ratio of proposed candidate salary against job band midpoint
"""
import sys
import json


def calculate_compa_ratio(comp_data_json: str):
    import json
    data = json.loads(comp_data_json) if isinstance(comp_data_json, str) else comp_data_json
    proposed = data.get("proposed_salary", 100000.0)
    midpoint = max(data.get("band_midpoint", 100000.0), 1.0)
    ratio = proposed / midpoint
    in_band = 0.80 <= ratio <= 1.20
    return {
        "proposed_salary": proposed,
        "band_midpoint": midpoint,
        "compa_ratio": round(ratio, 2),
        "in_band": in_band,
        "status": "IN_BAND_APPROVED" if in_band else "OUT_OF_BAND_REQUIRES_EXCEPTION"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "compa-ratio-calculator"}))
