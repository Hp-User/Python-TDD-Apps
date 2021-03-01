import unittest

import awesome


class TestMethods(unittest.TestCase):
    def test_smile(self):
       print("smile")
       self.assertEqual(awesome.smile(), ":)")

    def test_frown(self):
       print("frown")
       self.assertEqual(awesome.frown(), "?(")


if __name__ == '__main__':
    unittest.main()
