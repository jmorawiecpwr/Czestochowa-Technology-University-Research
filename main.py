import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interaktywne GUI do analizy danych")

        self.load_button = tk.Button(root, text="Załaduj dane", command=self.load_data)
        self.load_button.pack(pady=10)

        self.view_button = tk.Button(root, text="Wyświetl dane", command=self.view_data, state=tk.DISABLED)
        self.view_button.pack(pady=10)

        self.sort_button = tk.Button(root, text="Sortuj dane", command=self.sort_data, state=tk.DISABLED)
        self.sort_button.pack(pady=10)

        # Przycisk wyświetl wykres
        self.plot_button = tk.Button(root, text="Wyświetl wykres", command=self.plot_data, state=tk.DISABLED)
        self.plot_button.pack(pady=10)

        self.data = None

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Pliki CSV", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                messagebox.showinfo("Sukces", "Dane załadowane pomyślnie!")
                self.view_button.config(state=tk.NORMAL)
                self.sort_button.config(state=tk.NORMAL)
                self.plot_button.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się załadować danych: {e}")

    def view_data(self):
        if self.data is not None:
            top = tk.Toplevel(self.root)
            top.title("Wyświetl dane")

            text = tk.Text(top)
            text.pack(expand=1, fill='both')

            text.insert(tk.END, self.data.to_string())

    def sort_data(self):
        if self.data is not None:
            sort_column = simpledialog.askstring("Wprowadź", "Wprowadź nazwę kolumny do sortowania:")
            if sort_column and sort_column in self.data.columns:
                self.data = self.data.sort_values(by=sort_column)
                messagebox.showinfo("Sukces", f"Dane posortowane według kolumny: {sort_column}")
            else:
                messagebox.showerror("Błąd", "Nieprawidłowa nazwa kolumny")

    def plot_data(self):
        if self.data is not None:
            column = simpledialog.askstring("Wprowadź", "Wprowadź nazwę kolumny do wykresu:")
            if column and column in self.data.columns:
                top = tk.Toplevel(self.root)
                top.title("Wyświetl wykres")

                fig, ax = plt.subplots()
                ax.plot(self.data[column])
                ax.set_title(f'Wykres kolumny {column}')
                ax.set_xlabel('Indeks')
                ax.set_ylabel(column)

                canvas = FigureCanvasTkAgg(fig, master=top)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            else:
                messagebox.showerror("Błąd", "Nieprawidłowa nazwa kolumny")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
