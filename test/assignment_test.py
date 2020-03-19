import unittest
from lambdata.assignment import CustomFrame

class TestCustomFrame(unittest.TestCase):

    def test_add_state_names(self):
        custom_df = CustomFrame({'abbrev': ['ca', 'ct', 'co', 'tx', 'dc']})
        self.assertTrue('name' not in list(custom_df.columns))

        custom_df.add_state_name()

        self.assertTrue('name' in list(custom_df.columns))

        self.assertEqual(custom_df['name'][0], 'California')
        self.assertEqual(custom_df['abbrev'][0], 'ca')
        

if __name__ == '__main__':
    unittest.main()