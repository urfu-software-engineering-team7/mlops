import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Загрузка обучающих данных
X_train = pd.read_csv('train_processed/X_train.csv')
y_train = pd.read_csv('train_processed/y_train.csv')

# Создание модели и ее обучение
model = LinearRegression()
model.fit(X_train, y_train)

# Сохранение модели в файл
with open('trained_model.pickle', 'wb') as f:
    pickle.dump(model, f)
