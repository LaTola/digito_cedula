from cedula import Cedula
import unittest
# To reach parent dir
import sys
sys.path.append('../')
##


class testCedula(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        return super().setUp(self)

    @classmethod
    def tearDown(self) -> None:
        return super().tearDown(self)

    def test_cedula(self):
        print('-------- test de cedulas conocidas ------------')
        cedulas = ["945.450", 1756064, 1756066, "3.315.714",
                   5124957, 5664280, 5664277, "1.866.178", 1716676]
        verif = [3, 9, 1, 3, 0, 4, 9, 7, 4]
        count = 0
        for ncedula in cedulas:
            c = Cedula(ncedula)
            self.assertEqual(c.getVerifierDigit(), verif[count])
            count += 1


if __name__ == '__main__':
    unittest.main()
