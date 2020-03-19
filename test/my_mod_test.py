import unittest
from lambdata.my_mod import Helper

helper = Helper()

class TestMyMod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(helper.enlarge(5), 500)

if __name__ == '__main__':
    unittest.main()