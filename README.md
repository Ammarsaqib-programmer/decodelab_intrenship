# RuleBot — Rule-Based Chatbot

A simple rule-based chatbot built in Python using if-else logic, keyword matching, and OOP principles. No external libraries required.

---

## 📁 Project Structure

```
task_week_1.py   ← main chatbot script
README.md        ← this file
```

---

## 🚀 How to Run

```bash
python task_week_1.py
```

> Requires Python 3.10+ (uses `tuple[str, bool]` type hints).

---

## 💬 Supported Commands

| What you type              | Bot responds with        |
|----------------------------|--------------------------|
| `hello`, `hi`, `hey`       | Greeting message         |
| `help`, `what can you do`  | List of capabilities     |
| `time`, `date`, `today`    | Current date & time      |
| `joke`, `funny`, `laugh`   | A random programming joke|
| `who are you`, `your name` | Bot identity             |
| `how are you`, `feeling`   | Mood check response      |
| `bye`, `exit`, `quit`      | End the session          |

---

## 🧠 How It Works

### 1. Rule Matching (`get_response`)
Each user message is lowercased and checked against every `Rule` object in order. The first rule whose keyword appears anywhere in the input wins.

```
User input → lowercase → for each Rule → any keyword match? → generate reply
                                                ↓ no match
                                           random fallback
```

### 2. Rule Class
Each `Rule` holds:
- `keywords` — trigger words/phrases
- `responses` — list of possible replies (one chosen randomly)
- `dynamic` — optional `lambda` for live data (e.g. current time)
- `terminal` — if `True`, ends the session after replying

### 3. Session Class
Tracks message count and start time. Displays stats in the footer when the session ends.

### 4. Main Loop
```python
while True:
    user_input = input(...)
    validate_input(user_input)
    reply, is_terminal = get_response(user_input)
    print(reply)
    if is_terminal:
        break
```

---

## 🛠️ Adding a New Topic

Open `task_week_1.py` and append a new `Rule` to the `RULES` list:

```python
Rule(
    keywords=["weather", "rain", "sunny"],
    responses=[
        "I can't check live weather, but it's always sunny in Python! ☀️",
        "No weather module here — try https://weather.com",
    ]
),
```

No changes needed anywhere else.

---

## 📋 Requirements

| Requirement     | Detail                  |
|-----------------|-------------------------|
| Python version  | 3.10 or higher          |
| Dependencies    | None (stdlib only)      |
| Modules used    | `random`, `datetime`, `typing` |

---

## 🎓 Concepts Demonstrated

- **Control flow** — `for` loop + `if/else` for rule matching
- **OOP** — `Rule`, `Session`, `Config` classes
- **Randomness** — `random.choice()` for varied responses
- **Lambda / callables** — dynamic responses (live time/date)
- **Input validation** — length check, empty input guard
- **Exception handling** — `KeyboardInterrupt` / `EOFError`

---

## 🖥️ Sample Session

```
==================================================
         RuleBot — Rule-Based Chatbot
==================================================
  Type 'help' for commands, 'bye' to exit.

  🤖 Bot : Hi! I'm RuleBot 🤖 — powered by if-else logic.
  🤖 Bot : Type something to get started!

  👤 You : hello
  🤖 Bot : Hey! I'm RuleBot. How can I help you today?

  👤 You : tell me a joke
  🤖 Bot : Why do programmers prefer dark mode?
           Because light attracts bugs! 🐛

  👤 You : what time is it
  🤖 Bot : Right now it's 02:45 PM on Thursday, May 14 2026.

  👤 You : bye
  🤖 Bot : Goodbye! It was nice chatting with you. 👋

==================================================
  Session ended.
  Messages: 3 | Duration: 18.4s
==================================================
```

---

## 👤 Author

**Ammar** — BS CS/IT, Semester 7  
Shah Abdul Latif University  
Course: Network Security (Week 1 Task)
