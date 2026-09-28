"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitCompBenchmark.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.compa_ratio_calculator import *
from tools.pay_equity_parity_checker import *
from tools.transparency_band_formatter import *

class TestGitCompBenchmarkPredictability(unittest.TestCase):

    def test_compa_ratio_calculator(self):
        res = calculate_compa_ratio('{"proposed_salary": 105000, "band_midpoint": 100000}')
        self.assertTrue(res["in_band"])
        self.assertEqual(res["status"], "IN_BAND_APPROVED")

    def test_pay_equity_parity_checker(self):
        res = check_pay_equity('{"group_a_mean": 120000, "group_b_mean": 121000}')
        self.assertTrue(res["equitable"])
        self.assertEqual(res["status"], "PAY_EQUITY_VERIFIED")

    def test_transparency_band_formatter(self):
        res = format_transparency_band('{"min_salary": 90000, "max_salary": 130000}')
        self.assertIn("$90,000", res["disclosure_text"])
        self.assertEqual(res["status"], "DISCLOSURE_READY")


if __name__ == "__main__":
    unittest.main()
