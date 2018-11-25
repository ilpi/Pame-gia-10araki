import pandas as pd
import os.path


def initialization(filename):
    df = pd.read_csv(filename, names=['Age', 'Gender', 'tb', 'db', 'AAP', 'SAA', 'SGAA', 'TP', 'ALB', 'A-G', 'Ok'],delimiter=',')
    changes = {'Male': 0, 'Female': 1}
    df['Gender'] = df['Gender'].replace(changes)
    return df


def general_info(df):
    summ = df.shape
    mill = df[(df['Gender'] == 0) & (df['Ok'] == 2)]
    fill = df[(df['Gender'] == 1) & (df['Ok'] == 2)]
    male = len(df[df['Gender'] == 0])
    female = len(df[df['Gender'] == 1])
    print("\n\t\t################### Γενικές πληροφορίες του DataSet ###################\n")
    print("   \t\tΤο αρχείο περιέχει", summ[0], "δείγματα των", summ[1],
          "χαρακτηριστικών εκ των οποίων:\n""\t\t • Άνδρες:", male, "\n\t\t\t • ασθενείς:",
          len(mill),
          "\n\t\t • Γυναίκες:", female, "\n\t\t\t • ασθενείς:", len(fill))


def normalize(df, tup):
    nans = df.isnull().any(1).nonzero()[0]
    if nans:
        df[tup] = df[tup].fillna(df[tup].mean())

    df[tup] = df[tup].apply(lambda x: round(2 * (x - min(df[tup])) / (max(df[tup]) - min(df[tup])) - 1, 3))


def main():
    print("\n\t############################ PRE-PROCESSING STAGE #############################")
    r = input("\n\t\t Δώστε το όνομα του φακέλου που θέλετε να προεπεξεργαστείται: ")

    if os.path.isfile(r):
        i = initialization(r)
        general_info(i)
        for t in i.columns:
            normalize(i, t)

        print("\n\t######################### END OF PRE-PROCESSING STAGE ##########################")
    else:
        print("\n\t\tΣΦΑΛΜΑ-> Δεν υπάρχει φάκελος με όνομα:", r)


main()
