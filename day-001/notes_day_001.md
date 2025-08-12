## Day 001: Core Concepts

## Concept 1: The `print()` Function

- **Purpose:** The most fundamental command. Tells the computer to display output to the console.
- **Syntax:** `print("Content goes here")`
- **Key:** Lowercase `print`, followed by `()`.

---

## Concept 2: Strings

- **Definition:** A sequence of text characters. Simply "text".
- **Syntax:** Must be enclosed in matching quotes.
  - Double quotes: `"Hello"`
  - Single quotes: `'Hello'`
- **Rule:** `"This works"`. `'This works'`. `"This fails'`.

---

## Concept 3: Debugging (The #1 Skill)

- **Definition:** The process of finding and fixing errors in your code.
- **Syntax Error:** An error in the "grammar" of the code. The program won't run.
  - Example: Forgetting a closing `"` or `)`.
- **Your Best Tool:** Use `print()` to see what your program is doing. "Print-line debugging" is a universal, professional technique.

---

## Concept 4: String Manipulation

### The Newline Character: `\n`
- **Purpose:** To create a line break within a single string.
- **Syntax:** `\n` (a backslash followed by 'n').
- **Example:**
  ```python
  print("Hello\nWorld")
  # Output:
  # Hello
  # World

---

## Concept 5: The Importance of Indentation
- **Indentation:** The spaces at the beginning of a line of code.
- **The Rule:** In Python, indentation is not for style; it is part of the syntax. It defines blocks of code.
- **IndentationError:** A critical error that occurs if you have an unexpected space or tab at the beginning of a line. The code will crash.
- **Fix:** Remove the leading whitespace.
- **SyntaxError vs. IndentationError:**
- **SyntaxError:** You broke Python's grammar (e.g., print("Hello without the closing quote).
- **IndentationError:** You broke Python's spacing rules (e.g., print("Hello") with a leading space).

---

## Concept 6: The `input()` Function

- **Purpose:** To get text input *from* the user via the console. It pauses the program and waits.
- **How it Works:**
  1.  Displays a prompt (the text inside the parentheses) to the user.
  2.  The program execution **stops** and waits.
  3.  The user types their response and hits `Enter`.
  4.  The function then **returns** the user's typed text as a **string**.
- **Syntax:** `input("Your prompt to the user goes here: ")`
- **Example:** `input("What is your name? ")`

### Nesting Functions (An Important Idea)
- **Definition:** Placing one function inside another.
- **Execution Order:** Python works from the **inside out**.
- **Example:** `print("Hello " + input("What is your name?"))`
  1.  The `input()` function runs first. It prompts "What is your name?" and waits.
  2.  Let's say you type "Pepe". The `input()` function finishes and returns the string `"Pepe"`.
  3.  The line now effectively becomes `print("Hello " + "Pepe")`.
  4.  The `+` concatenation happens next, creating the string `"Hello Pepe"`.
  5.  Finally, the `print()` function runs with the final string and displays it.

---

## Concept 7: Comments

- **Purpose:** To leave notes for humans (including your future self!) inside the code. They are completely ignored by the Python interpreter.
- **Syntax:** The `#` symbol. Everything after the `#` on that same line is a comment.
- **Example:**
  ```python
  # This line asks for the user's name and then prints a greeting.
  print("Hello " + input("What is your name? "))  

---

## Concept 8: Variables

- **Purpose:** A named container for storing a piece of data. This allows you to label, reuse, and change data throughout your program.
- **Analogy:** Like labeling a box. The box is the computer's memory, the stuff inside is the data (e.g., the string `"Pepe"`), and the label on the box is the variable name (e.g., `user_name`).
- **Syntax (Assignment):** `variable_name = data`
  - The single equals sign `=` is the **assignment operator**. It means "put the data on the right into the container on the left."
- **Example:**
  ```python
  name = input("What is your name? ")
  # The string the user types is now stored in the 'name' variable.
  print(name)

---

## Concept 9: The len() Function

- **Purpose:** A built-in function that returns the length of an object.
- **For Strings:** It returns the number of characters in the string (including spaces).
- **Syntax:** len(some_string)
- **Return Type:** It returns an integer (a whole number).

- **Example:**
```python
name = "Pepe"
name_length = len(name) # name_length is now the integer 4
print(name_length)      # Prints 4

---

## Concept 10: Variable Naming Rules & Conventions

There are hard rules (which will crash your code) and conventions (which professionals follow for readability).

### The Rules (Must Follow)
1.  **Must be a single unit:** Variable names cannot contain spaces. Use an underscore `_` to separate words.
    -   ✅ `user_name`
    -   ❌ `user name` (This is a `SyntaxError`)
2.  **Cannot start with a number:** You can have numbers in a name, just not at the very beginning.
    -   ✅ `player1`
    -   ❌ `1st_player` (This is a `SyntaxError`)
3.  **Only use letters, numbers, and underscores:** Special characters like `-`, `!`, `?`, `&` are not allowed.
    -   ✅ `user_id_123`
    -   ❌ `user-id-123` (This is a `SyntaxError`)

### Conventions (Best Practices - Should Follow)
1.  **Use `snake_case`:** This is the official Python style guide (PEP 8) recommendation for multi-word variable names. All lowercase, with words separated by underscores.
    -   ✅ `user_login_count`
    -   ⚠️ `userLoginCount` (This is called `camelCase` and is used in other languages like JavaScript. It works in Python but is considered un-pythonic.)
2.  **Make names descriptive:** The name should clearly describe the data it holds.
    -   ✅ `user_age`
    -   ❌ `a` or `x` (unless it's a simple counter in a loop).
3.  **Don't "shadow" built-in functions:** Avoid naming your variables the same as functions like `print`, `len`, or `input`.
    -   **Why:** If you write `print = "Pepe"`, you have replaced the `print()` function with the string `"Pepe"`. The original function is now broken for the rest of your script. This causes massive confusion.

---

## Concept 11: The `NameError`

- **What it is:** A crash that happens when you try to use a variable that has **not been defined yet**.
- **The #1 Cause:** A simple typo.
  ```python
  name = "Pepe"
  # Later in the code...
  print(nama) # <- Typo!
  # This will crash with: NameError: name 'nama' is not defined

  