# Aditya Mandwekar 
# Task 01: A password strength assessment tool that evaluates the robustness of your password considering factors like length, inclusion of uppercase and lowercase letters, numeric digits, and special characters.
# Code:
# We have used the python library called Regular expressions (regex) are a powerful tool for pattern matching and manipulation of strings. 
# In the provided code, the re module is used to search for specific patterns within the password string.
import re

def check_password_complexity(password):
    # Minimum length requirement
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return False, "Password must contain lowercase letters"
    
    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return False, "Password must contain uppercase letters"
    
    # Check for numeric digits
    if not re.search("[0-9]", password):
        return False, "Password must contain numeric digits"
    
    # Check for special characters
    if not re.search("[!@#$%^&*()-_=+{};:,<.>/?\|`~]", password):
        return False, "Password must contain special characters"
    
    return True, "Password meets complexity requirements"

#Test
password = input("Enter your password: ")
is_complex, message = check_password_complexity(password)
print(message)
