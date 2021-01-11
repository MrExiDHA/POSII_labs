import pandas as pd


def get_client_dataset():
    df = pd.read_csv(r'client_data_set.csv')
    df = df.drop(['Unnamed: 32'], axis='columns')
    df.loc[df['diagnosis'] == 'M', 'diagnosis'] = 1
    df.loc[df['diagnosis'] == 'B', 'diagnosis'] = 0
    x, y = df.drop('diagnosis', axis=1), df['diagnosis']
    y = y.astype('int')
    return x, y
