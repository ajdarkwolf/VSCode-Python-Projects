import tkinter as tk
from itertools import permutations
import importlib.resources

try:
    with importlib.resources.open_text("wordlist", "dictionary.txt") as f:
        englishWords = [line.strip() for line in f]
except FileNotFoundError:
    print("Oops! Something went wrong.")
    englishWords = []

root = tk.Tk()
root.title("Wordscapes Solver")

def FindNLetterWords(lettersInWord: list, n: int) -> list:
    if not isinstance(n, int):
        return
    if len(lettersInWord) != 6:
        return
    
    possibleWords = []
    permutes = list(permutations(lettersInWord, n))
    joinedPermutes = []

    for i in permutes:
        joined = ""
        for j in i:
            joined += j
        joinedPermutes.append(joined)
            
    for i in joinedPermutes:
        if i in englishWords:
            possibleWords.append(i)
    
    return possibleWords

def RemoveDuplicates(l: list) -> list:
    templist = []
    for i in l:
        if not i in templist:
            templist.append(i)
    return templist

def Add_To_List():
    ThreeLetterWords.delete(0, tk.END)
    FourLetterWords.delete(0, tk.END)
    FiveLetterWords.delete(0, tk.END)
    SixLetterWords.delete(0, tk.END)

    if len(entry.get()) != 6:
        return
    
    letters = [i.lower() for i in entry.get()]
    words = []

    for i in range(3,7):
        words += FindNLetterWords(letters, i)
    words = RemoveDuplicates(words)
    for word in words:
        if len(word) == 3:
            ThreeLetterWords.insert(tk.END, word)
        if len(word) == 4:
            FourLetterWords.insert(tk.END, word)
        if len(word) == 5:
            FiveLetterWords.insert(tk.END, word)
        if len(word) == 6:
            SixLetterWords.insert(tk.END, word)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.rowconfigure(2, weight=1)

entry = tk.Entry(frame)
entry.grid(row=0, column=0, columnspan=3, sticky="ew")
entry.bind("<Return>", lambda event: Add_To_List())

entry_btn = tk.Button(frame, text="Solve", command=Add_To_List)
entry_btn.grid(row=0, column=3, sticky="ew")

ThreeLetterWords = tk.Listbox(frame)
ThreeLetterWords.grid(row=2,column=0, sticky="nsew")

FourLetterWords = tk.Listbox(frame)
FourLetterWords.grid(row=2,column=1, sticky="nsew")

FiveLetterWords = tk.Listbox(frame)
FiveLetterWords.grid(row=2,column=2, sticky="nsew")

SixLetterWords = tk.Listbox(frame)
SixLetterWords.grid(row=2,column=3, sticky="nsew")

lbl0 = tk.Label(frame, text="Three Letter Words")
lbl0.grid(row=1, column=0)

lbl1 = tk.Label(frame, text="Four Letter Words")
lbl1.grid(row=1, column=1)

lbl2 = tk.Label(frame, text="Five Letter Words")
lbl2.grid(row=1, column=2)

lbl3 = tk.Label(frame, text="Six Letter Words")
lbl3.grid(row=1, column=3)

root.mainloop()
