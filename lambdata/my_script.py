#lambdata/my_script.py

import pandas as pd
from lambdata.my_mod import enlarge, train_val_test_split, tocol

print('Happy Tuesday Night.')

df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
print(df.head())

x = 5
print('Enlarge', x, 'to', enlarge(x))

print('Testing train_val_test_split')

df2 = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
'c': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]})

df2 = pd.concat([df2, df2])

X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(df2.drop(columns = 'c'), df2['c'], stratify = df2['c'])

print(df2.shape)
print(X_train.shape, X_val.shape, X_test.shape, y_train.shape, y_val.shape, y_test.shape)
print('The train, val, test split has the right shape:')
print(X_train.shape[0] + X_val.shape[0] + X_test.shape[0] == df2.shape[0])

df3 = tocol(df, [7, 8, 9], 'z')
print(df3)