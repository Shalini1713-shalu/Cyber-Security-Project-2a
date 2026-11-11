# Cyber Security Project 1: Password Strength Checker
# Checks length, uppercase letters, numbers and symbols.

import string

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1
if any(char.isupper() for char in password):
    score += 1
if any(char.isdigit() for char in password):
    score += 1
if any(char in string.punctuation for char in password):
    score += 1

if score <= 1:
    strength = "Weak"
elif score <= 3:
    strength = "Medium"
else:
    strength = "Strong"

print("\\nPassword Strength:", strength)
print("Criteria satisfied:", score, "out of 4")
