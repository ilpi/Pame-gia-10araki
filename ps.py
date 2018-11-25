import pandas as pd
from random import sample


df = pd.read_csv('yo.csv', names=['Age', 'Gender', 'tb', 'db', 'AAP', 'SAA', 'SGAA', 'TP', 'ALB', 'A-G', 'Ok'], delimiter=',')
changes = {'Male': 0, 'Female': 1}
df['Gender'] = df['Gender'].replace(changes)


def kfoldcv(f, k):
    h = f.values.tolist()
    test_set = []
    size = len(h)
    elem_size = int(size / k)

    for i in range(k):
        new_sample = sample(h, elem_size)
        test_set.append(new_sample)

        for row in new_sample:
            h.remove(row)

    if len(h) != 0:
        for rows in range(len(h)):
            test_set[rows].append(h[rows])
        h.clear()


    print(test_set)


kfoldcv(df, 5)
