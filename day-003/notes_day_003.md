# --------------------------------------------------
# Day 3: Control Flow & Logical Operators
# --------------------------------------------------

## 1. Conditional Statements: The `if/else` Construct

### Key Syntax:
- if condition:
    - do this
- else:
    - do this

### Explanation:
- How indentation (the code block) is crucial in Python.
- The role of the colon `:`.
- The `if` statement executes its block only when the condition evaluates to `True`.
- The `else` statement provides an alternative path for when the condition is `False`.

### Example Code:
- [You will fill this in based on our lesson]
# A program to check if someone is tall enough to ride a roller coaster.

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

# The condition is 'height >= 120'. This will be either True or False.
if height >= 120:
    # This indented block runs if the condition is True.
    print("You can ride the roller coaster!")
else:
    # This indented block runs if the condition is False.
    print("Sorry, you have to grow taller before you can ride.")


## 2. Nested `if/else` and the `elif` Statement

### Key Syntax:
- if condition1:
    - do A
- elif condition2:
    - do B
- else:
    - do C

### Explanation:
- `elif` stands for "else if" and allows for checking multiple conditions in sequence.
- Python checks conditions from top to bottom and executes the *first* block where the condition is `True`.
- The final `else` is a catch-all if no preceding conditions were met.

### Example Code:
- [You will fill this in]

## 3. Logical Operators

### The `and` Operator:
- `A and B` is `True` only if both A and B are `True`.
- Use Case: Checking multiple requirements at once (e.g., age >= 18 AND has_photo_id).

### The `or` Operator:
- `A or B` is `True` if at least one of A or B is `True`.
- Use Case: Checking for one of several possibilities (e.g., pays_with_cash OR pays_with_card).

### The `not` Operator:
- `not A` inverts the boolean value of A. `not True` becomes `False`.
- Use Case: Checking for the absence of a condition (e.g., `if not is_raining:`).

### Example Code:
- [You will fill this in]

## 4. Useful Functions with Conditionals

### The `.lower()` and `.upper()` String Methods
- Explanation: How these methods are essential for creating case-insensitive comparisons in user input.
- Example: `if user_input.lower() == "yes":`

### The `.count()` String Method
- Explanation: How to count occurrences of a substring within a string.
- Example: `love_score = name1.count("l") + name2.count("l")`

### The Modulo Operator (`%`)
- Recap from yesterday.
- Primary use case in conditionals: Checking for even/odd numbers (`number % 2 == 0`).

***

### **Tech Lead Deep Dive: Binary Decisions - The Foundation of Complexity**

You might look at `if/else` and think it's simple. It is. But that simplicity is its power. Every complex piece of software you've ever used is, at its core, built upon millions of these simple, binary decisions.

-   **Authentication System:** `if password_hash == stored_hash`, then `grant_access`. `else`, `show_error_message`.
-   **E-commerce Site:** `if item_stock > 0`, then `allow_add_to_cart`. `else`, `display_out_of_stock`.
-   **Code Editor (like VS Code):** `if user_presses_save_shortcut`, then `write_file_to_disk`. `else`, `continue_listening_for_input`.
-   **Feature Flags (A very common industry practice):** We often release new features "turned off" in the code.
    `if feature_flag_for_new_dashboard == True`, then `show_new_dashboard()`. `else`, `show_old_dashboard()`. This allows us to enable features for specific users (like testers or premium members) without deploying new code.

You're not just learning to make a program say one thing or another. You are learning to construct the fundamental logical atom that all complex software is built from. Master this, and you can build anything.

***

### **New Tickets Assigned: Control Flow Practice**

Here are three tickets for you to work on. They will solidify your understanding of the `if/else` block and comparison operators. Let me know which tier you'd like to attempt for the first one.

---
**Ticket #007: Odd or Even Checker**

*   **Goal:** Create a program that checks if a number entered by the user is odd or even.
*   **Concepts:** `input()`, `int()`, `if/else`, and the **Modulo Operator (`%`)** from yesterday.
*   **Hint:** An even number is any number that can be divided by 2 with a remainder of 0.

---
**Ticket #008: Roller Coaster Ticketing 2.0**

*   **Goal:** Modify the roller coaster code from the lesson. In addition to the existing height check, add a new condition to check if the person's height is *exactly* 120cm and print a special message for them.
*   **Concepts:** Nested `if/else` (or a simple modification, depending on your approach), `==` operator.

---
**Ticket #009: Leap Year Checker (Simplified)**

*   **Goal:** Write a program that determines if a given year is a leap year.
*   **Simplified Rule:** For this ticket, a leap year is any year that is evenly divisible by 4. (Note: The true rule is more complex, but we'll build up to that.)
*   **Concepts:** `input()`, `int()`, `%`, `if/else`.

---

Let's start with **Ticket #007: Odd or Even Checker**. Please choose your tier: **Tier 1 (Guided)**, **Tier 2 (Assisted)**, or **Tier 3 (Independent)**.

***

### **Spaced Repetition Review**

Before you start coding, let's fire up those neurons. Quick questions:

1.  **(Day 2):** How would you write an F-String to print the value of a variable `total_bill` (e.g., `150.123`) formatted to exactly two decimal places, like "$150.12"?
2.  **(Day 1):** Which function do you use to find the number of characters in a string?
3.  **(Day 3):** What is the difference between `user_age = 30` and `user_age == 30`?

---

## Nested `if/else` and the `elif` Statement (Expanded)

### The `elif` Statement: A Chain of Choices

- **Purpose**: To check multiple, *mutually exclusive* conditions in a clean, sequential way. As soon as one condition is `True`, its code block runs, and the rest of the chain is skipped.
- **Analogy**: A vending machine. You press one button. You get one item. The process stops.

### Example Code (Age Pricing):
```python
# The program only enters ONE of these blocks.
if age < 12:
    # Path A
    bill = 5
elif age <= 18:
    # Path B (only checked if age is NOT < 12)
    bill = 7
else:
    # Path C (only runs if age is NOT < 12 AND NOT <= 18)
    bill = 12

2b. Multiple Independent if Statements: A Checklist
Purpose: To check several independent conditions, where one outcome does not affect the others. Every if statement is checked regardless of the outcome of the ones before it.
Analogy: A restaurant menu. Ordering an appetizer doesn't stop you from ordering a main course.
Example Code (Roller Coaster with Add-ons):
code
Python
# The program checks ALL of these conditions.
bill = 0

# --- Start of First Question ---
if age < 12:
    bill = 5
elif age <= 18:
    bill = 7
else:
    bill = 12
# --- End of First Question ---


# --- Start of Second, Independent Question ---
if wants_photo == "y":
    bill += 3
# --- End of Second Question ---


# --- Start of Third, Independent Question ---
if wants_fast_pass == "y":
    bill += 5
# --- End of Third Question ---
2c. Nested if Statements: Questions Inside Questions
Purpose: To handle logic that only applies after a previous condition has been met.
Analogy: A login system. FIRST, you check if the username exists. ONLY IF IT EXISTS do you then check if the password is correct.
Key: Indentation is everything. The inner if is indented, showing it's a child of the outer if.
Example Code (Roller Coaster Entry):
code
Python
# Outer Question: Are they tall enough?
if height >= 120:
    print("Welcome! Please proceed to ticketing.")

    # Inner Question: What is their age?
    # This question is ONLY asked if they are tall enough.
    if age < 18:
        print("Please go to the youth line.")
    else:
        print("Please go to the adult line.")

else:
    # This path is for the outer question only.
    print("Sorry, you are not tall enough to ride.")
code
Code
***

### **Tech Lead Deep Dive: Visualizing Code Flow**

You mentioned this is where you get lost. Let's make it impossible to get lost. Look at this text-based flowchart for the complete roller coaster code. Before you even read the code, read this.
START
|
--> Ask for height.
|
--> Is height >= 120?
|
|--- YES (Main "Can Ride" Path) ----------------------------
| |
| --> Ask for age.
| |
| --> Is age < 12?
| |--- YES: bill = 5
| |--- NO: --> Is age <= 18?
| |--- YES: bill = 7
| |--- NO: bill = 12
| |
| --> (Age pricing is now complete. Bill is either 5, 7, or 12)
| |
| --> Ask if they want a photo.
| |
| --> Did they say "y"?
| |--- YES: Add 3 to the bill.
| |--- NO: Do nothing to the bill.
| |
| --> Print the final bill.
|
|--- NO (Main "Cannot Ride" Path) ---------------------------
|
--> Print "Sorry, you're too short."
|
END
code
Code
This is the entire program's logic. **The code is just a translation of this flowchart.** When you get a new, complex problem, I want you to try writing out a flowchart like this first. It externalizes the logic from your brain onto the screen, freeing you up to focus on the syntax.

***

### **New Ticket Assigned: Control Flow Practice**

Let's apply this with a new, slightly more complex problem. It will require you to use `if/elif/else` for one set of choices, and another independent `if` for an additional choice.

---
**Ticket #010: Pizza Order Practice**

*   **Goal:** Build an automatic pizza order program.
*   **Business Rules:**
    1.  Based on a user's order, work out their final bill.
    2.  Small Pizza: $15
    3.  Medium Pizza: $20
    4.  Large Pizza: $25
    5.  Pepperoni for Small Pizza: +$2
    6.  Pepperoni for Medium or Large Pizza: +$3
    7.  Extra cheese for any size pizza: +$1

*   **User Input:** The program should ask for `size` (`S`, `M`, or `L`), `add_pepperoni` (`Y` or `N`), and `extra_cheese` (`Y` or `N`).

---

I recommend we tackle this one together using **Tier 1 (Guided)** to start, so we can build the logical structure step-by-step. Does that work for you? If so, I will provide the problem breakdown and formulas.

## Logical Operators

- **Purpose**: To combine multiple conditions into a single, more powerful boolean expression.

### The `and` Operator
- **Syntax**: `condition_A and condition_B`
- **Rule**: Evaluates to `True` **only if both** A and B are `True`.
- **Analogy**: To get a driver's license, you must `pass_written_test AND pass_driving_test`. Failing either one means you don't get the license.
- **Truth Table**:
    - `True and True`   -> `True`
    - `True and False`  -> `False`
    - `False and True`  -> `False`
    - `False and False` -> `False`

### The `or` Operator
- **Syntax**: `condition_A or condition_B`
- **Rule**: Evaluates to `True` **if at least one** of A or B is `True`.
- **Analogy**: To get into a venue, you need `a_ticket OR to_be_on_the_guest_list`. Having either one is enough.
- **Truth Table**:
    - `True or True`   -> `True`
    - `True or False`  -> `True`
    - `False or True`  -> `True`
    - `False or False` -> `False`

### The `not` Operator
- **Syntax**: `not condition_A`
- **Rule**: Inverts the boolean value of the condition. `not True` becomes `False`, and `not False` becomes `True`.
- **Analogy**: `if not is_raining:` means the same as `if is_raining == False:`. It's a more readable way to check for a false condition.

### Example Code (Roller Coaster Midlife Crisis Special):
```python
age = int(input("What is your age? "))
bill = 12 # Default adult price

# Using 'and' to check if age falls within a range.
if age >= 45 and age <= 55:
    print("Everything's going to be okay. Have a free ride on us!")
    bill = 0 # Free ride!

# Note: The 'simplified chained comparison' is a Python shortcut for this.
# '45 <= age <= 55' is equivalent to 'age >= 45 and age <= 55'
# The explicit 'and' version is often clearer for beginners.
code
Code
---

### **New Ticket Assigned: Logical Operator Practice**

Let's put this into practice immediately. This ticket will require you to use the `and`, `or`, and the full leap year logic.

---
**Ticket #011: Leap Year Checker (Full Logic)**

*   **Goal:** Upgrade the Leap Year Checker from Ticket #009 to use the complete, official rules.
*   **The Official Rules for a Leap Year:**
    *   A year is a leap year if it is evenly divisible by 4...
    *   **...EXCEPT** if the year is also evenly divisible by 100...
    *   **...UNLESS** the year is also evenly divisible by 400.
*   **Examples:**
    *   `2000` is a leap year (divisible by 4, 100, and 400). The "unless" rule applies.
    *   `2100` is **not** a leap year (divisible by 4 and 100, but not 400). The "except" rule applies.
    *   `1996` is a leap year (divisible by 4, but not 100). The first rule applies.
    *   `2001` is **not** a leap year (not divisible by 4).
*   **Concepts:** `if/elif/else`, the modulo operator (`%`), and logical operators (`and`, `or`).

---

This one is tricky. It's a classic programming interview question. I want you to try drawing out a **text flowchart** for the logic first, just like I did for the roller coaster. It will make translating it to code much easier.

Let me know which tier you'd like to attempt: **Tier 1 (Guided)**, **Tier 2 (Assisted)**, or **Tier 3 (Independent)**. Given the complexity, Tier 2 might be a good starting point, where you create the plan and I review it before you code.

## 4. Useful Functions and Concepts for Conditionals

### The `.lower()` String Method
- **Purpose**: To create case-insensitive comparisons, which is crucial for robust user input. It takes a string and returns a new version of it in all lowercase.
- **Example**: `if "Yes".lower() == "yes":` evaluates to `True`.
- **Professional Use Case**: When asking for user input like "Y/N", a user might type 'y', 'Y', 'yes', or 'YES'. By converting the input to lowercase immediately, we only have to check for one condition (`if user_input.lower() == 'y':`).
```python
raw_input = input("Do you agree? (Y/N)") # User types "Y"
processed_input = raw_input.lower() # processed_input is now "y"

if processed_input == "y":
    print("User agreed.")
Multi-line Strings with Triple Quotes (''' or """)
Purpose: To create strings that span multiple lines, preserving whitespace, tabs, and line breaks. Extremely useful for things like ASCII art or long blocks of text.
Syntax:
code
Python
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._" ,-"""-._ `"=._o`"=._      `"=._o`"=._.-.___|_______
          |           |o`"=._`"=.o|o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o|
 _________|___________|o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o|_______
|                   |o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o|
|___________________|o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o|_______
          |           |o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o|
 _________|___________|o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o|_______
|                   |o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o`"=._o|
 -------------------------------------------------------------------------------
'''
)
The Escape Character (\)
Purpose: To tell Python that the character immediately following the backslash is "special" and should be treated differently.
Common Uses:
\' or \": To include a quote character inside a string that is defined by the same quote type.
\n: To create a new line character.
Example: print('He said, "It\'s a beautiful day."')

