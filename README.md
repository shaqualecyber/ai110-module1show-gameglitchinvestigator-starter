# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

Game Purpose

The purpose of this project is to create a number guessing game where players attempt to guess a randomly generated secret number. The game provides hints to help guide the player, tracks attempts, and adjusts the valid guessing range based on the selected difficulty level.

Bugs Found

During testing, I discovered that the game accepted guesses that were outside the valid range for the selected difficulty. For example, when Easy mode was selected, the valid range was 1–20, but the game still accepted values such as 25, 0, and 1000. This created inconsistent gameplay because the difficulty limits were not being enforced.

Fixes Applied

To fix this issue, I refactored the parse_guess() logic into logic_utils.py and added range validation. The updated function now checks whether a guess falls within the active difficulty range before accepting it. If a player enters a value outside the allowed range, the game displays an error message instead of processing the guess.

I also added a regression test in test_game_logic.py to verify that out-of-range guesses are rejected correctly. Finally, I tested the application in the browser by entering values such as 25, 0, and 1000 while using Easy mode and confirmed that the game displayed the message "Guess must be between 1 and 20."

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

The game is started on Easy difficulty, which sets the valid range to 1–20.
The player enters a guess of 25.
The game rejects the guess and displays the message: "Guess must be between 1 and 20."
The player enters a guess of 0.
The game again rejects the guess and displays the same range validation message.
The player enters a valid guess within the allowed range.
The game accepts the guess and provides the appropriate hint based on the secret number.
Additional valid guesses continue to update the game normally.
The player eventually guesses the correct number and wins the game.
The game records the result and allows a new game to be started.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
