# lambdata/assignment.py (functional approach)

import pandas

def main():
    print('-------------------------------')
    df = CustomFrame({"abbrev": ['ca', 'ct', 'co', 'tx', 'dc']})

    print(df.head())

    df.add_state_name()
    print(df.head())

    print('-------------------------------')
    df2 = CustomFrame({'abbrev': ['oh', 'mi', 'id', 'wa', 'wi']})

    print(df2.head())
    
    df2.add_state_name()
    print(df2.head())

    print('-------------------------------')

class CustomFrame(pandas.DataFrame):

    def add_state_name(self):
        '''
        param:
            my_df (pandas.DataFrame) containing a colum called 'abbrev'
        '''
        names_map = {
            'ca': 'California',
            'ct': 'Connecticut',
            'co': 'Colorado',
            'tx': 'Texas',
            'dc': 'Washington DC',
            'oh': 'Ohio',
            'mi': 'Michigan',
            'id': 'Idaho',
            'wa': 'Washington',
            'wi': 'Wisconsin'
        }

        self['name'] = self['abbrev'].map(names_map)


if __name__ == '__main__':
    main()