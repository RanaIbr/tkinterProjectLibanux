import tkinter as tk
from tkinter import scrolledtext
r = tk.Tk()
r.title("Word Frequencies")
r.geometry('500x500')

def count_word_occurrences(filename):
    word_counts = {}

    with open(filename, "r") as f:
        for line in f:
            line = line.strip().lower()
            words = line.split()

            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts

def display_word_frequencies(filename):
    word_counts = count_word_occurrences(filename)

    text_area = scrolledtext.ScrolledText(r, width=40, height=20)
    text_area.pack(padx=10, pady=10)

    text_area.insert(tk.INSERT, "Word Frequencies:\n\n")
    for word, count in word_counts.items():
        text_area.insert(tk.END, f"{word}: {count}\n")

    text_area.configure(state='disabled')
    r.mainloop()

filename = r"C:\Users\User\OneDrive\Desktop\rana.txt"

display_word_frequencies(filename)


