import pandas as pd
from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    df = df.dropna()

    train, test = train_test_split(df, test_size=0.3, random_state=42)
    vali, test = train_test_split(test, test_size=0.6, random_state=42)


    train.to_csv('train.csv', index=False)
    test.to_csv('test.csv', index=False)
    vali.to_csv('vali.csv', index=False)
