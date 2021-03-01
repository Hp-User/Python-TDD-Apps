##sudo -H pip install mock
##python -m unittest## 
####python -m unittest -v Verify_MockInvocation
##

import unittest
from mock import Mock
 

# this function takes an object as argument and calls a method on it

def function_with_call(obj, argument):
    print("The unction_with_call")
    return obj.update(argument)

class TestWithMock(unittest.TestCase):
 def test_verify_call_onMock():
    mock = Mock()
    mock.update = Mock(return_value=None)
    function_with_call(mock, "Mybar")
    # will return true if method was called one or more times
    mock.some_method.assert_called()

if __name__ == '__main__':
    unittest.main()
