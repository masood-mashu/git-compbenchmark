"""
transparency_band_formatter.py - Formats legally compliant salary range disclosures for job requisition descriptions
"""
import sys
import json


def format_transparency_band(band_extremes_json: str):
    import json
    data = json.loads(band_extremes_json) if isinstance(band_extremes_json, str) else band_extremes_json
    s_min = data.get("min_salary", 80000)
    s_max = data.get("max_salary", 120000)
    disclosure = f"The estimated base salary range for this role is ${s_min:,} - ${s_max:,} USD per year."
    return {
        "min": s_min,
        "max": s_max,
        "disclosure_text": disclosure,
        "status": "DISCLOSURE_READY"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "transparency-band-formatter"}))
