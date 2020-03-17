# lambdata/assignment.py (functional approach)

import pandas

def main():
    print('-------------------------------')
    df = pandas.DataFrame({"abbrev": ['ca', 'ct', 'co', 'tx', 'dc']})

    # new_df = add_state_name(df)
    # print(new_df.head())
    processor = DataProcessor(df)

    print(processor.df.head())

    processor.add_state_name()
    print(processor.df.head())

    print('-------------------------------')
    df2 = pandas.DataFrame({'abbrev': ['oh', 'mi', 'id', 'wa', 'wi']})
    processor2 = DataProcessor(df2)
    

    print(processor2.df.head())
    
    processor2.add_state_name()
    print(processor2.df.head())

    print('-------------------------------')
#state abbreviation -? Ful Name and visa versa. 

class DataProcessor():

    def __init__(self, my_df):
        '''
        param:
            my_df (pandas.DataFrame) containing a colum called 'abbrev'
        '''
        self.df = my_df.copy()


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

        self.df['name'] = self.df['abbrev'].map(names_map)


if __name__ == '__main__':
    main()