import pandas as pd
import random

df = pd.read_csv('iris.csv')
columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

for c in columns:
    for o in df.index:
        i = random.randint(1, 21)
        if i == 3 and o > df.shape[0]-5:
            a = df.loc[o, columns] + df.loc[o+1, columns] + df.loc[o+2, columns] + df.loc[o+3, columns] \
                + df.loc[o, columns]
            df.loc[o, columns] = a/5

