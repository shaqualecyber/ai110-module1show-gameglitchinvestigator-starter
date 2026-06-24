# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I launched the game for the first time, the interface appeared to work, but it didn't take long to notice several inconsistencies. The first thing that stood out was that Hard mode displayed a range of 1–50 in the settings panel while the game instructions still told me to guess between 1–100. As I continued testing, I discovered that some of the hints pointed me in the wrong direction, making it difficult to trust the feedback the game was providing. I was also able to submit values that should have been considered invalid, including negative numbers, decimals, and guesses outside the stated range, which suggested the input validation was not working as expected.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Hard difficulty selected | Hard mode should be harder than Normal and the displayed range should match everywhere. | Sidebar showed range 1 to 50, but the main prompt still said guess between 1 and 100. | None |
| Guess of 101 | Game should reject the guess because it is outside the 1 to 100 range. | Game accepted the guess and gave a hint instead of showing an invalid range message. | None |
| Guess of -11 | Game should reject negative numbers because they are outside the valid range. | Game accepted the negative number and gave a hint. | None |
| Developer Debug Info opened | The secret number should stay hidden from the player. | The secret number was visible in the debug section. | None |
| Guess of 2 when the secret was 82 | Game should say “Go higher” because 2 is lower than 82. | Game said “Go lower,” which was the wrong direction. | None |

---

## 2. How did you use AI as a teammate?

I used ChatGPT and the VS Code AI assistant during this project. One suggestion that seemed accurate involved the incorrect hint direction bug. The AI explained that the game might be comparing values as strings instead of numbers, which could cause the hint logic to behave incorrectly. I tested several guesses and noticed the game sometimes told me to go lower even when my guess was already below the secret number. The explanation helped me better understand how inconsistent data types can affect program behavior.

One AI suggestion that turned out to be misleading happened while I was troubleshooting a Streamlit error. The AI suggested that a problematic line was still present in app.py, but when I checked that location, I couldn't find anything wrong. After digging deeper and using terminal commands to inspect the file, I discovered that the actual issue was a command that had accidentally been saved at the end of the script. That experience reminded me that AI can be helpful for troubleshooting, but its suggestions still need to be tested and verified.

---

## 3. Debugging and testing your fixes

I tested the range validation fix manually in Streamlit. I switched the game to Easy mode, where the valid range is 1–20, and entered 25, 0, and 1000. Each one was rejected with the message “Guess must be between 1 and 20.” That showed me the game was finally checking the selected difficulty range instead of accepting every number I typed. 

Futhermore while testing the different difficulty levels, I noticed that the game was enforcing the correct number ranges behind the scenes, but the message shown to the player still said "Guess a number between 1 and 100" regardless of the selected difficulty. After reviewing the code, I updated the displayed range so it matches the active difficulty level. I verified the fix by switching between Easy, Normal, and Hard modes and confirming that both the displayed instructions and the input validation were using the same range.

---

## 4. What did you learn about Streamlit and state?

Before this project, I honestly didn't understand what people meant when they talked about reruns in Streamlit. Now I think of it as the app basically starting over every time a user clicks something. The part that confused me at first was how the game could remember things like the secret number and remaining attempts if it kept rerunning. That's where session state clicked for me. Session state acts like the app's memory and keeps important information from being reset every time the page refreshes.

---

## 5. Looking ahead: your developer habits

One thing I want to keep doing in future projects is intentionally testing things that aren't supposed to happen. The bug I fixed wasn't found by entering normal guesses. It was found because I started trying values like 25, 0, and 1000 while Easy mode was selected. That showed me how important edge-case testing can be.

The next time I work with AI on a coding task, I want to slow down and review each suggested change before accepting it. There were times when the AI was helpful and pointed me in the right direction, but there were also times when I had to verify that the suggestion actually solved the problem and didn't create a new one.

This project helped me realize that AI is a useful teammate, but it isn't a replacement for understanding the code. I still have to test, question, and verify what it gives me. The AI can help me work faster, but I'm still responsible for making sure the solution actually works.