# lambdata/assignment.py (functional approach)

import pandas

def main():
    df = pandas.DataFrame({"abbrev": ['ca', 'ct', 'co', 'tx', 'dc']})
    print(df.head())

    df2 = pandas.DataFrame({'abbrev': ['oh', 'mi', 'id', 'wa', 'wi']})
    print(df2.head())
#state abbreviation -? Ful Name and visa versa. 

def add_state_name():
    pass



if __name__ == '__main__':
    main()