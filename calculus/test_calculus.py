import unittest
from newtonsAlgorithm import newtonsAlgorithm

class calculusTests(unittest.TestCase):
    

    def function(self, x0: float):
        return x0**2 
        
    def test_NewtonsAlgo(self):
        aprox = newtonsAlgorithm(20, self.function)
        print(aprox)
        self.assertAlmostEquals(aprox, 0)


