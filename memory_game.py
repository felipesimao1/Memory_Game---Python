import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")

        self.letters = [chr(i) for i in range(ord("A"), ord("O") + 1)] * 2
        random.shuffle(self.letters)

        self.buttons = []
        self.pairs_found = 0

        self.create_interface()

    def restart_game(self):
        self.letters = [chr(i) for i in range(ord("A"), ord("O") + 1)] * 2
        random.shuffle(self.letters)
        self.pairs_found = 0

        for button in self.buttons:
            button.config(text="", state=tk.NORMAL)

    def create_interface(self):
        for i in range(5):
            for j in range(6):
                button = tk.Button(self.root, text="", width=4, height=2, command=lambda i=i, j=j: self.click_card(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

        start_button = tk.Button(self.root, text="Start", command=self.restart_game)
        start_button.grid(row=5, column=0, columnspan=6, pady=10)

    def click_card(self, row, column):
        index = row * 6 + column
        button = self.buttons[index]

        if button.cget("text") == "":
            button.config(text=self.letters[index])

            if not hasattr(self, "previous_card"):
                self.previous_card = (row, column)
            else:
                previous_row, previous_column = self.previous_card
                current_letter = self.letters[index]
                previous_letter = self.letters[previous_row * 6 + previous_column]

                if current_letter == previous_letter:
                    button.config(state=tk.DISABLED)
                    self.buttons[previous_row * 6 + previous_column].config(state=tk.DISABLED)
                    self.pairs_found += 1

                    if self.pairs_found == 15:
                        messagebox.showinfo("Congratulations!", "You found all pairs!")
                        self.restart_game()
                else:
                    self.root.after(1000, lambda: self.hide_cards(row, column, previous_row, previous_column))

                delattr(self, "previous_card")

    def hide_cards(self, row, column, previous_row, previous_column):
        self.buttons[row * 6 + column].config(text="")
        self.buttons[previous_row * 6 + previous_column].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
