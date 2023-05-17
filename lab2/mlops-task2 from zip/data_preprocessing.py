import pandas as pd
from sklearn.preprocessing import StandardScaler
import os


def main():
    # Загрузка данных
    train_data = pd.read_csv('train/train_data.csv')
    test_data = pd.read_csv('test/test_data.csv')

    # Извлечение признаков и меток
    X_train = train_data.drop('Temperature', axis=1)
    y_train = train_data['Temperature']
    X_test = test_data.drop('Temperature', axis=1)
    y_test = test_data['Temperature']

    # Применение StandardScaler
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Сохранение предобработанных данных в файлы
    if not os.path.exists('train_processed'):
        os.makedirs('train_processed')
    if not os.path.exists('test_processed'):
        os.makedirs('test_processed')

    pd.DataFrame(X_train).to_csv('train_processed/X_train.csv', index=False)
    pd.DataFrame(y_train).to_csv('train_processed/y_train.csv', index=False)
    pd.DataFrame(X_test).to_csv('test_processed/X_test.csv', index=False)
    pd.DataFrame(y_test).to_csv('test_processed/y_test.csv', index=False)


if __name__ == "__main__":
    main()
