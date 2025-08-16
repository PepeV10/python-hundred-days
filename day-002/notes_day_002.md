### Python Primitive Data Types
- **Primitive Data Types** are the most basic building blocks of data in Python.

- **String (`str`)**
  - A sequence of characters.
  - Defined using single `'` or double `"` quotes.
  - Example: `"Hello"`, `'12345'`
  - **Subscripting**: Accessing individual characters using an index in square brackets `[]`.
    - Python uses **zero-based indexing**. The first character is at index `0`.
    - `my_string = "Hello"`
    - `my_string[0]` -> `'H'`
    - `my_string[4]` -> `'o'`
    - Negative indexing starts from the end: `my_string[-1]` -> `'o'`.

- **Integer (`int`)**
  - A whole number (no decimal part). Can be positive or negative.
  - Defined without quotes.
  - Example: `123`, `-50`, `0`
  - For readability, large integers can use underscores: `100_000_000` is treated as `100000000`.

- **Float (`float`)**
  - A number with a decimal point ("floating-point number").
  - Example: `3.14159`, `-0.001`, `2.0`

- **Boolean (`bool`)**
  - Represents one of two states: truth or falsehood.
  - Only two possible values: `True` and `False`. (Note the capitalization).
  - Crucial for logic and control flow (which we'll cover later).

---

### Mathematical Operations
- **Addition:** `+`
- **Subtraction:** `-`
- **Multiplication:** `*`
- **Division:** `/`
  - **Key Note:** Always results in a `float`, even if the division is exact (e.g., `6 / 3` results in `2.0`).
- **Floor Division (Integer Division):** `//`
  - Performs division and **truncates** (removes) the decimal part, resulting in an `int`.
  - Example: `5 // 3` results in `1`. (Careful: this is NOT standard rounding).
- **Exponentiation (Power):** `**`
  - Example: `2 ** 3` (2 to the power of 3)

### Operator Precedence (PEMDAS)
- The order in which mathematical operations are evaluated:
  1. **P**arentheses `()`
  2. **E**xponents `**`
  3. **M**ultiplication `*` and **D**ivision `/`
  4. **A**ddition `+` and **S**ubtraction `-`
- **Evaluation Order:** Multiplication/Division and Addition/Subtraction are evaluated from **left to right** if they share the same precedence level.
- Use parentheses `()` to explicitly define the order of operations.

---

### Number Manipulation & F-Strings

#### The `round()` function
- Used to round a number to the nearest integer or to a specified number of decimal places.
- **Syntax:**
  - `round(number)`: Rounds to the nearest whole number.
    - `round(8 / 3)` -> `3`
  - `round(number, ndigits)`: Rounds to `ndigits` decimal places.
    - `round(2.6666, 2)` -> `2.67`
- **Pro Note (Banker's Rounding):** In Python 3, `round(2.5)` results in `2` and `round(3.5)` results in `4`. It rounds to the nearest *even* number for `.5` cases. This is a subtle but important detail in data science.

#### Augmented Assignment Operators
- Shorthand operators to modify a variable's value in place.
- Makes code more concise and readable.
- `score = score + 1` becomes `score += 1`
- **Common Operators:**
  - `+=` (Addition)
  - `-=` (Subtraction)
  - `*=` (Multiplication)
  - `/=` (Division)

#### F-Strings (Formatted String Literals)
- The modern, clean, and preferred way to mix variables with strings.
- **Syntax:** Start the string with the letter `f` before the quotes. Place variables inside curly braces `{}`.
- **Main Advantage:** Python handles the type conversion automatically. No more `TypeError` or manual `str()` conversion.
- **Example:**
  ```python
  score = 10
  height = 1.75
  is_winning = True
  print(f"Your score is {score}, your height is {height}, and winning status is {is_winning}.")

## Comparisson between round() function and f"(value:.2f)" String Formatting

Feature:	round(value, 2)	f"{value:.2f}"
Purpose:	Mathematical operation	String formatting / Presentation
Return Type:	float or int	str
Where to Use:	Can be used anywhere (calculations, variables)	Only inside an f-string or .format() method
Behavior:	Actually changes the numerical value	Changes only the text representation
Padding:	Does NOT pad with zeros. round(12.5, 2) is 12.5	Pads with zeros. f"{12.5:.2f}" is "12.50"

  ---

