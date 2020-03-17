# lambdata/assignment.py (functional approach)

import pandas

def main():
    print('-------------------------------')
    df = pandas.DataFrame({"abbrev": ['ca', 'ct', 'co', 'tx', 'dc']})
    print(df.head())

    new_df = add_state_name(df)
    print(new_df.head())

    print('-------------------------------')
    df2 = pandas.DataFrame({'abbrev': ['oh', 'mi', 'id', 'wa', 'wi']})
    print(df2.head())
    
    new_df2 = add_state_name(df2)
    print(new_df2.head())

    print('-------------------------------')
#state abbreviation -? Ful Name and visa versa. 

def add_state_name(my_df):
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

    new_df = my_df.copy()

    new_df['name'] = new_df['abbrev'].map(names_map)
    return new_df




if __name__ == '__main__':
    main()