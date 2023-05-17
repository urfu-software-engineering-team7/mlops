import numpy as np
import pandas as pd
import os


def main():
    if not os.path.exists('train'):
        os.makedirs('train')
    if not os.path.exists('test'):
        os.makedirs('test')

    # Генерация данных для обучающей выборки
    train_data = pd.DataFrame({'Day': range(1, 31), 'Temperature': np.random.normal(20, 5, 30)})
    # Добавление аномалии в данные
    train_data.loc[15, 'Temperature'] = 0

    # Сохранение данных в файл
    train_data.to_csv('train/train_data.csv', index=False)

    # Генерация данных для тестовой выборки
    test_data = pd.DataFrame({'Day': range(31, 41), 'Temperature': np.random.normal(25, 5, 10)})
    # Добавление шума в данные
    test_data['Temperature'] += np.random.normal(0, 2, 10)

    test_data.to_csv('test/test_data.csv', index=False)


if __name__ == "__main__":
    main()
