import sys, os

project_root = sys.path.append(os.path.abspath(".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import unittest

import verifiable_mpc.ac20.circuit_sat_cb as cs
from demos import demo_zkp_mpc_ac20
from mpyc.runtime import mpc


class CircuitSat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_cs_pivot_elliptic(self):
        verification = mpc.run(demo_zkp_mpc_ac20.main(cs.PivotChoice.pivot, "Elliptic", 10))
        self.assertEqual(all(check == True for check in verification.values()), True)

    def test_cs_compressed_elliptic(self):
        verification = mpc.run(
            demo_zkp_mpc_ac20.main(cs.PivotChoice.compressed, "Elliptic", 10)
        )
        self.assertEqual(all(check == True for check in verification.values()), True)

    def test_cs_pivot_quadratic_residues(self):
        verification = mpc.run(demo_zkp_mpc_ac20.main(cs.PivotChoice.pivot, "QR", 10))
        self.assertEqual(all(check == True for check in verification.values()), True)

    def test_cs_compressed_quadratic_residues(self):
        verification = mpc.run(demo_zkp_mpc_ac20.main(cs.PivotChoice.compressed, "QR", 10))
        self.assertEqual(all(check == True for check in verification.values()), True)


if __name__ == "__main__":
    unittest.main()
