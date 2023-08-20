import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра Виселица")

        self.word_list = ["привет", "мир", "питон", "программирование", "разработка"]
        self.secret_word = random.choice(self.word_list)
        self.guesses = []
        self.remaining_attempts = 6

        self.word_label = tk.Label(root, text=self.get_display_word())
        self.word_label.pack()

        self.guess_label = tk.Label(root, text="Угаданные буквы:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()

        self.attempts_label = tk.Label(root, text=f"Осталось попыток: {self.remaining_attempts}")
        self.attempts_label.pack()

        self.guess_button = tk.Button(root, text="Угадать", command=self.make_guess)
        self.guess_button.pack()

    def get_display_word(self):
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                display_word += letter
            else:
                display_word += "_"
        return display_word

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if guess in self.guesses:
            return

        self.guesses.append(guess)

        if guess not in self.secret_word:
            self.remaining_attempts -= 1

        self.attempts_label.config(text=f"Осталось попыток: {self.remaining_attempts}")
        self.word_label.config(text=self.get_display_word())
        self.guess_label.config(text=f"Угаданные буквы: {' '.join(self.guesses)}")

        if self.remaining_attempts == 0:
            self.word_label.config(text=f"Вы проиграли. Загаданное слово: {self.secret_word}")
            self.guess_button.config(state=tk.DISABLED)
        elif "_" not in self.get_display_word():
            self.word_label.config(text=f"Поздравляем, вы выиграли! Загаданное слово: {self.secret_word}")
            self.guess_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
