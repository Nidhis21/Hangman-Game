# Hangman Game

A fun and interactive **Hangman Game** built using **Python**. Players are challenged to guess a hidden word from a chosen category by suggesting one letter at a time. The game offers hints and keeps track of incorrect guesses.

---

## How to Play

1. **Choose a Category:**

   - Categories include Animals, Sports, Countries, Desserts, etc.

2. **Guess the Word:**

   - A random word from the selected category will be shown as dashes (e.g., `_ _ _ _`).
   - Guess one letter at a time.

3. **Get Hints:**

   - Type `hint` if you need help (maximum 2 hints per game).
   - The correct letter at a position you choose will be revealed.

4. **Win or Lose:**

   - You win if you guess the full word before running out of attempts.
   - You lose if your attempts reach zero.

---

## Rules

- You have a limited number of attempts: **word length + 5 chances**.
- Correct guesses do not reduce your attempts.
- Incorrect guesses will reduce your attempts by **1**.
- You can use **up to 2 hints** by typing `hint`.
- Repeating letters you have already guessed **won't cost attempts**.
- The game ends when:
  - You guess all the letters (**You Win!**)
  - You run out of attempts (**You Lose!**)

---

## How to Run

1. Ensure you have **Python** installed ([Download](https://www.python.org/downloads/)).
2. Download or clone this repository.


---

## Categories Available

1. Colors
2. Animals
3. Countries
4. Sports
5. Vehicles
6. Shapes
7. Musical Instruments
8. Languages
9. Planets
10. Occupations
11. Desserts
12. Clothing
13. Furniture
14. Emotions
15. Gadgets

---

## Features

- Interactive terminal-based gameplay
- Dynamic hint system
- Automatic letter reveal for all occurrences
- Multiple categories for variety
- Friendly messages and progress display

---

## Future Improvements (Optional Ideas)

- Add levels of difficulty
- Implement graphics using `tkinter` or `pygame`
- Track high scores or game history

---




