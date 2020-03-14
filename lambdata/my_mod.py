#lamdata/my_mod.py
#Rushing to MVP.  Two more helper functions

from sklearn.model_selection import train_test_split
import pandas as pd

class Helper:

    def __init__(self):
        #nothing to go in here yet
        pass

    def train_val_test_split(self, X, y, test_size = .3, val_size = .1, train_size = .6, 
    random_state = None, shuffle = True, stratify = None):
        '''
        Fragile, no exception handling for the sum of test_size, val_size, train_size.
        We're all adults here.  Make the sum of them equal = 1
        '''

        X_train, X_temp, y_train, y_temp = train_test_split(X, y, train_size = train_size,
            random_state = random_state, shuffle = shuffle, stratify = stratify)

        split = 1 / ((test_size + val_size) * 10)

        split = split * val_size * 10

        if stratify is not None:
            strat = y_temp
        else:
            strat = None
        
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, train_size = split,
            random_state = random_state, shuffle = shuffle, stratify = strat)

        return(X_train, X_val, X_test, y_train, y_val, y_test)

    def tocol(self, df, colist, column):
        '''
        turn a list into a column
        params:
            df - dataframe to add column to
            colist - list to be turned into a column
            column - string of the column name
        '''
        df[column] = pd.Series(colist)
        return df


    def enlarge(self, n):
        return n * 100


def main():
    print("junk")
    print('global_scope')

    helper = Helper()

    y = float(input('please input a number to enlarge:'))
    print(helper.enlarge(y))

if __name__ == "__main__":
    main()