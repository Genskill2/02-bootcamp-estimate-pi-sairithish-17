import math
import unittest
import random

def wallis(n1):  
    pi=1
    n=1
    while n<=n1:
        pi=float(pi)*((4*n*n)/((4*n*n)-1))
        n+=1
    pi=2*float(pi)
    return pi

def monte_carlo(n):
  circle=0
  square=0
  n2=0
  while  n2<n:
      x=random.uniform(-1,1)
      y=random.uniform(-1,1)
      d=float(((x*x)+(y*y))**(0.5))
      if d>1:
        square+=1
      if d<1:
        circle+=1
        square+=1      
      n2+=1      
  pi=float(4*(circle/square))   
  return pi    

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
