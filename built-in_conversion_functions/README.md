# Python Type Conversion & Operations – Step-by-Step README

**What this script does (short):**  
This script demonstrates how Python handles **different data types** (`int`, `float`, and `str`) and how to **convert values** between these types to perform arithmetic operations or text concatenation.

---

# Output screenshot
'screenshots/python_built-in_conversion_functions.png'

# Step-by-step explanation

1. Define variables

* int_value = 15
  float_value = 4.1
  text_value = "33"

int_value is an integer (int).

float_value is a floating-point number (float).

text_value is a string (str), even though it looks like a number.

2. Check the type of float_value

* type_of_float_value = type(float_value)

type() returns the data type of an object.

Stores <class 'float'> in type_of_float_value.

3. Convert string to integer

* text_value_as_int = int(text_value)

Converts "33" (string) into 33 (integer).

This makes it possible to add it to another integer.

4. Convert integer to string

* int_value_as_text = str(int_value)

Converts 15 (integer) into "15" (string).

This allows concatenation with another string.

5. Print the type of float_value

* print("float_value type:", type_of_float_value)

Displays <class 'float'>.

6. Integer addition

* print("Integer addition: Adding text_value_as_int (33) to int_value (15):", text_value_as_int + int_value)

Both text_value_as_int (33) and int_value (15) are integers.

Performs arithmetic: 33 + 15 = 48.

7. String concatenation

* print("Text addition: Adding text_value (33) to int_value_as_text (15):", text_value + int_value_as_text)

Both text_value ("33") and int_value_as_text ("15") are strings.

Performs concatenation: "33" + "15" = "3315".