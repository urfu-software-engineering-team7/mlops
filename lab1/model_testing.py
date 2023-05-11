import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error

# Загрузка тестовых данных
X_test = pd.read_csv('test_processed/X_test.csv')
y_test = pd.read_csv('test_processed/y_test.csv')

# Загрузка обученной модели из файла
with open('trained_model.pickle', 'rb') as f:
    model = pickle.load(f)

    # Тестирование модели на данных из папки test
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    # Вывод результатов тестирования
    print("Mean squared error: %.2f" % mse)
