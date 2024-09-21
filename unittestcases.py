import unittest
from multiply import multiplication
class MultiplyTestCase(unittest.TestCase):
  def test_1(self):
    result = multiplication(2,3)
    self.assertEqual(result,6)
 def test_2(self):
   result = multiplication(-2,3)
   self.assertEqual(result,-6)
 def test_3(self):
   result = multiplication(2,-3)
   self.assertEqual(result,-6)
def test_4(self):
   result = multiplication(-2,-3)
   self.assertEqual(result,6)


if __name__ == '__main__':
  unittest.main()
