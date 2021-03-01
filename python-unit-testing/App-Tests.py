#python App-Tests.py
#python -m unittest App-Tests
import unittest
from mycode import *

class UserTests(unittest.TestCase):
 def test_custom_num_list(self):
    print('Custom Test1')
    self.assertEqual(len(create_num_list(10)), 10)

 def test_hello(self):
   print('Hello World Test')
   self.assertEqual(hello_world(), 'hello world')

 def test_custom_func_x(self):
    print('Custom Test2')
    self.assertEqual(custom_func_x(3,2,3), 54)

 def test_custom_non_lin_num_list(self):
  print('Custom Test3')
  self.assertEqual(custom_non_lin_num_list(5,2,3)[2], 16)
  self.assertEqual(custom_non_lin_num_list(5,3,2)[4], 48)

if __name__ == '__main__':
    unittest.main()
