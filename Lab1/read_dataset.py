import pandas as pd


def get_breast_cancer_dataset():
    df = pd.read_csv(r'Breast_cancer_data_for_ML.csv')
    df = df.drop(['Unnamed: 32'], axis='columns')
    df.loc[df['diagnosis'] == 'M', 'diagnosis'] = 1
    df.loc[df['diagnosis'] == 'B', 'diagnosis'] = 0
    return df.drop('diagnosis', axis=1), df['diagnosis']
