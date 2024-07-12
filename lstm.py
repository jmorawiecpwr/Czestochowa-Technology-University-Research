import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

df = pd.read_csv('czestochowa_publikacje.csv')
df['Rok'] = pd.to_numeric(df['Rok'], errors='coerce')
df = df.dropna(subset=['Rok'])

publikacje_per_year = df.groupby('Rok').size().values.reshape(-1, 1)
cytowania_per_year = df.groupby('Rok')['Cytowania'].sum().values.reshape(-1, 1)

scaler_publikacje = MinMaxScaler(feature_range=(0, 1))
publikacje_scaled = scaler_publikacje.fit_transform(publikacje_per_year)

scaler_cytowania = MinMaxScaler(feature_range=(0, 1))
cytowania_scaled = scaler_cytowania.fit_transform(cytowania_per_year)

def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 5
X_p, y_p = create_dataset(publikacje_scaled, look_back)
X_c, y_c = create_dataset(cytowania_scaled, look_back)

X_p = np.reshape(X_p, (X_p.shape[0], look_back, 1))
X_c = np.reshape(X_c, (X_c.shape[0], look_back, 1))

model_publikacje = Sequential()
model_publikacje.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))
model_publikacje.add(LSTM(50))
model_publikacje.add(Dense(1))
model_publikacje.compile(loss='mean_squared_error', optimizer='adam')
model_publikacje.fit(X_p, y_p, epochs=100, batch_size=1, verbose=2)

model_cytowania = Sequential()
model_cytowania.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))
model_cytowania.add(LSTM(50))
model_cytowania.add(Dense(1))
model_cytowania.compile(loss='mean_squared_error', optimizer='adam')
model_cytowania.fit(X_c, y_c, epochs=100, batch_size=1, verbose=2)

def predict_future(model, data, look_back, steps):
    pred_output = []
    input_seq = data[-look_back:]
    for _ in range(steps):
        prediction = model.predict(input_seq.reshape(1, look_back, 1))
        pred_output.append(prediction[0, 0])
        input_seq = np.append(input_seq[1:], prediction)
        input_seq = input_seq[-look_back:]
    return np.array(pred_output)

pred_publikacje_lstm = predict_future(model_publikacje, publikacje_scaled, look_back, 5)
pred_cytowania_lstm = predict_future(model_cytowania, cytowania_scaled, look_back, 5)

pred_publikacje_lstm = scaler_publikacje.inverse_transform(pred_publikacje_lstm.reshape(-1, 1))
pred_cytowania_lstm = scaler_cytowania.inverse_transform(pred_cytowania_lstm.reshape(-1, 1))

publikacje_extended = np.concatenate((publikacje_per_year, pred_publikacje_lstm))
cytowania_extended = np.concatenate((cytowania_per_year, pred_cytowania_lstm))

print("Predykcje liczby publikacji na kolejne 5 lat (LSTM):")
print(pred_publikacje_lstm)
print("Predykcje liczby cytowań na kolejne 5 lat (LSTM):")
print(pred_cytowania_lstm)

plt.figure(figsize=(12, 6))
plt.plot(range(len(publikacje_extended)), publikacje_extended, label='Liczba publikacji (rzeczywiste i prognoza)')
plt.axvline(x=len(publikacje_per_year) - 1, color='r', linestyle='--', label='Początek prognozy')
plt.title('Prognoza liczby publikacji na kolejne 5 lat (LSTM)')
plt.xlabel('Rok')
plt.ylabel('Liczba publikacji')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(range(len(cytowania_extended)), cytowania_extended, label='Liczba cytowań (rzeczywiste i prognoza)')
plt.axvline(x=len(cytowania_per_year) - 1, color='r', linestyle='--', label='Początek prognozy')
plt.title('Prognoza liczby cytowań na kolejne 5 lat (LSTM)')
plt.xlabel('Rok')
plt.ylabel('Liczba cytowań')
plt.legend()
plt.show()
