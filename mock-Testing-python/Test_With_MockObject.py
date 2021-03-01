##sudo -H pip install mock
##python -m unittest
##python -m unittest -v Test_With_MockObject
##

import unittest
from mock import patch
 
from MyClass import User

def function_test():
    return complex_function().upper()

class TestWithMockData(unittest.TestCase):
    def test_mock(self):
      # mock an object of class 
      with patch.object(User, 'sayhi', return_value="hi i'm from mock object") as patched:
      # the MyClass object used be replaced by a mock defined in the patch.object call 
       assert User.sayhi() == "hi i'm from mock object"
       patched.assert_called()

    def verifycall(self): 
      with patch("User.sayhi") as patched_function:
         User.sayhi()

      patched_function.assert_called()

if __name__ == '__main__':
    unittest.main()
