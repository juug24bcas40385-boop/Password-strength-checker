import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password():
    password = entry.get()

    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a number")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add a special character")

    # Determine Strength
    if score <= 2:
        strength = "WEAK"
    elif score == 3:
        strength = "MEDIUM"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    result_text = f"Password Strength: {strength}\n\nSecurity Score: {score}/5"

    if suggestions:
        result_text += "\n\nSuggestions:\n"
        for item in suggestions:
            result_text += f"• {item}\n"

    result_label.config(text=result_text)

# Main Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")

# Heading
title = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)

# Password Entry
label = tk.Label(root, text="Enter Password:")
label.pack()

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=10)

# Check Button
button = tk.Button(
    root,
    text="Check Strength",
    command=check_password
)
button.pack(pady=10)

# Result Area
result_label = tk.Label(
    root,
    text="",
    justify="left",
    font=("Arial", 11)
)
result_label.pack(pady=20)

# Run Application
root.mainloop()