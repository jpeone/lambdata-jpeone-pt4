# lamdata/my_mod.py
# Rushing to MVP.  Two more helper functions

from sklearn.model_selection import train_test_split
import pandas as pd


def main():
    print("junk")
    print('global_scope')

    helper = Helper()

    y = float(input('please input a number to enlarge:'))
    print(helper.enlarge(y))


class Helper:

    def __init__(self):
        # nothing to go in here yet
        pass

    def train_val_test_split(self, X, y, test_size=.3, val_size=.1,
                             train_size=.6, random_state=None, shuffle=True,
                             stratify=None):
        '''
        An extension of sklearn train_test_split, to include a validation set.
        Fragile, no exception handling. test_size + val_size+train_size = 1.0
        We're all adults here, use like the sklearn method

        params:
            X - DataFrame, to be split into three parts
            y - Series, to be split into three parts
            test_size - float,  the percentage of data split into test set
            val_size - float,  the percentage of data split into val set
            train_size - float,  the percentag of data split into the train set
            random_state - int or None, setting the seed for random
            shuffle - boolean, to determine if the sets should be shuffled
            stratify - Series or None, to stratify the splits on

        return - three DataFrames and three Series split from the passed in
            DataFrame and Series
        '''

        X_train, X_temp, y_train, y_temp = train_test_split(
            X,
            y,
            train_size=train_size,
            random_state=random_state,
            shuffle=shuffle,
            stratify=stratify)

        split = 1 / ((test_size + val_size) * 10)

        split = split * val_size * 10

        if stratify is not None:
            strat = y_temp
        else:
            strat = None

        X_val, X_test, y_val, y_test = train_test_split(
            X_temp,
            y_temp,
            train_size=split,
            random_state=random_state,
            shuffle=shuffle,
            stratify=strat)

        return(X_train, X_val, X_test, y_train, y_val, y_test)

    def tocol(self, df, colist, column):
        '''
        A method to turn a list into a column
        params:
            df - pandas DataFrame to add a new column to
            colist - list to be turned into a column
            column - string of the column name
        return - DataFrame with the new column added
        '''
        df[column] = pd.Series(colist)
        return df

    def enlarge(self, n):
        '''
        returns the passed in value multiplied by 100
        '''
        return n * 100


if __name__ == "__main__":
    main()
