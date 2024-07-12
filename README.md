# Interactive Data Analysis Application

This project is an interactive GUI application built with Tkinter for loading, viewing, sorting, and plotting CSV data. It also includes predictive modeling features using LSTM, ARIMA, and linear regression models to forecast future data trends.

## Features

- **Load CSV Data:** Easily load CSV files into the application.
- **View Data:** Display the loaded data in a new window.
- **Sort Data:** Sort the data based on a selected column.
- **Plot Data:** Visualize the data by plotting selected columns.
- **Predictive Modeling:** Forecast future data trends using LSTM, ARIMA, and linear regression models.
- **Google Scholar Scraping:** Retrieve publication data from Google Scholar using SerpAPI.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/data-analysis-app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd data-analysis-app
    ```
3. Install the required dependencies:
    ```sh
    pip install pandas matplotlib tensorflow scikit-learn statsmodels serpapi
    ```

## Usage

1. Run the main application script:
    ```sh
    python main.py
    ```
2. Use the GUI to load data, view data, sort data, and plot data.
3. Run predictive modeling scripts to forecast future data trends:
    ```sh
    python lstm_forecasting.py
    python arima_forecasting.py
    python regresja_liniowa.py
    ```
4. Retrieve publication data from Google Scholar using the scraping script:
    ```sh
    python scrapping.py
    ```

## Code Explanation

### Main Application (Tkinter GUI)

- `DataApp`: Main class for the application, handling UI creation, event binding, and core functionality.
- `load_data()`: Function to load CSV data into the application.
- `view_data()`: Function to display the loaded data in a new window.
- `sort_data()`: Function to sort the data based on a selected column.
- `plot_data()`: Function to plot the data based on a selected column.

### Predictive Modeling

- **LSTM Model** (`lstm_forecasting.py`):
  - Data preparation, model training, and future predictions using LSTM for both publication count and citation count.
- **ARIMA Model** (`arima_forecasting.py`):
  - Data preparation, model fitting, and future predictions using ARIMA for both publication count and citation count.
- **Linear Regression Model** (`regresja_liniowa.py`):
  - Data preparation, model training, and future predictions using linear regression for both publication count and citation count.

### Google Scholar Data Retrieval (`scrapping.py`)

- `pobierz_dane_scholarly(nazwa_autora)`: Function to retrieve publication data from Google Scholar for a given author using the SerpAPI.
- `main()`: Main function to read a list of authors, retrieve their publication data, and save it to a CSV file.
