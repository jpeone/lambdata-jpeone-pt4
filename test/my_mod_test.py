import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from lambdata.my_mod import Helper


class TestMyMod(unittest.TestCase):

    def test_enlarge(self):

        helper = Helper()

        self.assertEqual(helper.enlarge(5), 500)

    def test_tocol(self):

        helper = Helper()

        # a dataframe to validate against
        val = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6], 'z': [7, 8, 9]})

        # a dataframe to test the method with
        test = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})

        test = helper.tocol(test, [7, 8, 9], 'z')

        assert_frame_equal(test, val)


if __name__ == '__main__':
    unittest.main()
