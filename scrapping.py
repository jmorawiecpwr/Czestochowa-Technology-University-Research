import pandas as pd
from serpapi import GoogleSearch

API_KEY = 'd9305b4020a9742b6da2c0d7f4a4d32cf89586bfd655ecf64c658b273e13a396'


def pobierz_dane_scholarly(nazwa_autora):
    params = {
        "engine": "google_scholar",
        "q": nazwa_autora,
        "api_key": API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    if "error" in results:
        print(f"Błąd podczas pobierania danych dla {nazwa_autora}: {results['error']}")
        return []

    publikacje = []
    for pub in results.get("organic_results", []):
        publikacje.append({
            'Autor': nazwa_autora,
            'Tytuł': pub.get('title', ''),
            'Rok': pub.get('publication_info', {}).get('year', ''),
            'Cytowania': pub.get('cited_by', {}).get('value', 0)
        })

    return publikacje


def main():
    with open('naukowcy.txt', 'r') as plik:
        naukowcy = [linia.strip() for linia in plik]

    wszystkie_publikacje = []

    for naukowiec in naukowcy:
        print(f"Pobieranie danych dla {naukowiec}")
        publikacje_naukowca = pobierz_dane_scholarly(naukowiec)
        if publikacje_naukowca:
            wszystkie_publikacje.extend(publikacje_naukowca)

    if wszystkie_publikacje:
        df = pd.DataFrame(wszystkie_publikacje)
        df.to_csv('czestochowa_publikacje.csv', index=False)
        print("Pobieranie zakończone. Dane zapisane do pliku 'czestochowa_publikacje.csv'.")
    else:
        print("Nie znaleziono danych.")


if __name__ == "__main__":
    main()
