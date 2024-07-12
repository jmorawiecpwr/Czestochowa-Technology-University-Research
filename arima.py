import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
from statsmodels.tsa.arima.model import ARIMA

warnings.filterwarnings("ignore")

sciezka = 'czestochowa_publikacje.csv'
df = pd.read_csv(sciezka)

df_publications = df.groupby('Rok')['Tytuł'].count()
df_publications = df_publications.reset_index()
df_publications.set_index('Rok', inplace=True)

model_publications = ARIMA(df_publications, order=(5, 1, 0))
model_fit_publications = model_publications.fit()

forecast_publications = model_fit_publications.forecast(steps=5)
forecast_years_publications = np.arange(df_publications.index[-1] + 1, df_publications.index[-1] + 1 + len(forecast_publications))

combined_index_publications = np.concatenate([df_publications.index, forecast_years_publications])
combined_values_publications = np.concatenate([df_publications.values.flatten(), forecast_publications])

plt.figure(figsize=(12, 6))
plt.plot(df_publications.index, df_publications.values, label='Liczba publikacji (rzeczywiste)', marker='o')
plt.plot(combined_index_publications, combined_values_publications, label='Liczba publikacji (prognoza)', linestyle='--', marker='o', color='orange')
plt.xlabel('Rok')
plt.ylabel('Liczba publikacji')
plt.title('Prognoza liczby publikacji na kolejne 5 lat (ARIMA)')
plt.legend()
plt.show()

df_citations = df.groupby('Rok')['Cytowania'].sum()
df_citations = df_citations.reset_index()
df_citations.set_index('Rok', inplace=True)

model_citations = ARIMA(df_citations, order=(5, 1, 0))
model_fit_citations = model_citations.fit()

forecast_citations = model_fit_citations.forecast(steps=5)
forecast_years_citations = np.arange(df_citations.index[-1] + 1, df_citations.index[-1] + 1 + len(forecast_citations))

combined_index_citations = np.concatenate([df_citations.index, forecast_years_citations])
combined_values_citations = np.concatenate([df_citations.values.flatten(), forecast_citations])

plt.figure(figsize=(12, 6))
plt.plot(df_citations.index, df_citations.values, label='Liczba cytowań (rzeczywiste)', marker='o')
plt.plot(combined_index_citations, combined_values_citations, label='Liczba cytowań (prognoza)', linestyle='--', marker='o', color='orange')
plt.xlabel('Rok')
plt.ylabel('Liczba cytowań')
plt.title('Prognoza liczby cytowań na kolejne 5 lat (ARIMA)')
plt.legend()
plt.show()
