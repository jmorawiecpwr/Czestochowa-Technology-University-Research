import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


file_path = 'czestochowa_publikacje.csv'
data = pd.read_csv(file_path)
publications_per_year = data.groupby('Rok').size()
citations_per_year = data.groupby('Rok')['Cytowania'].sum()
aggregated_data = pd.DataFrame({
    'Publikacje': publications_per_year,
    'Cytowania': citations_per_year
}).reset_index()

X = aggregated_data['Rok'].values.reshape(-1, 1)
y_publications = aggregated_data['Publikacje'].values
y_citations = aggregated_data['Cytowania'].values

model_publications = LinearRegression()
model_publications.fit(X, y_publications)
model_citations = LinearRegression()
model_citations.fit(X, y_citations)
future_years = np.arange(aggregated_data['Rok'].max() + 1, aggregated_data['Rok'].max() + 6).reshape(-1, 1)
forecast_publications = model_publications.predict(future_years)
forecast_citations = model_citations.predict(future_years)
all_years = np.concatenate((X, future_years))
all_publications = np.concatenate((y_publications, forecast_publications))
all_citations = np.concatenate((y_citations, forecast_citations))
plt.figure(figsize=(14,7))
plt.plot(all_years, all_publications, label='Liczba publikacji', marker='o', linestyle='-')
plt.plot(future_years, forecast_publications, label='Prognoza publikacji', linestyle='--', marker='o')
plt.plot(all_years, all_citations, label='Liczba cytowań', marker='o', linestyle='-')
plt.plot(future_years, forecast_citations, label='Prognoza cytowań', linestyle='--', marker='o')
plt.xlabel('Rok')
plt.ylabel('Liczba')
plt.title('Prognoza liczby publikacji naukowych i cytowań')
plt.legend()
plt.grid(True)
plt.show()
