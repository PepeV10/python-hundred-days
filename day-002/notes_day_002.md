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

