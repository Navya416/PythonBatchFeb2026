#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithm:
============
1) is it empty 
2) is it alphabet 
3) is it vowel or not 

NOTE: handle case-sensitivity 
"""

ch = input("Enter a character: ").strip()

# Step 1: Check if input is empty
if ch == "":
    print("No input provided.")

# Check if more than one character is entered
elif len(ch) != 1:
    print("Please enter only one character.")

# Step 2: Check if it is an alphabet
elif not ch.isalpha():
    print("Input is not an alphabet.")

# Step 3: Check vowel or consonant
elif ch.lower() in "aeiou":
    print(f"'{ch}' is a Vowel.")
else:
    print(f"'{ch}' is a Consonant.")