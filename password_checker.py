import tkinter as tk
import string
import math

# Function to calculate password strength and feedback
def check_strength(password):
    length = len(password)
    special_chars = any(char in string.punctuation for char in password)
    digits = any(char.isdigit() for char in password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    
    feedback = []
    if length < 8:
        feedback.append("Increase length (at least 8 characters)")
    if not (special_chars and digits and uppercase and lowercase):
        feedback.append("Use a combination of uppercase, lowercase, numbers, and symbols")
    
    # Entropy calculation
    charset_size = 0
    if special_chars:
        charset_size += len(string.punctuation)
    if digits:
        charset_size += 10
    if uppercase:
        charset_size += 26
    if lowercase:
        charset_size += 26
    
    entropy = length * math.log2(charset_size) if charset_size > 0 else 0
    
    # Strength classification
    if length < 8 or not (special_chars and digits and uppercase and lowercase):
        return "Weak", "red", feedback
    elif entropy < 50:
        return "Medium", "orange", feedback
    else:
        return "Strong", "green", []

# GUI Setup
def evaluate_password(event=None):
    password = entry.get()
    strength, color, feedback = check_strength(password)
    result_label.config(text=f"Strength: {strength}", fg=color)
    
    feedback_text = "\n".join(feedback) if feedback else "Looks good!"
    feedback_label.config(text=feedback_text, fg="black")

# Tkinter Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

frame = tk.Frame(root)
frame.pack(pady=20)

title_label = tk.Label(frame, text="Enter your password:", font=("Arial", 12))
title_label.pack()

entry = tk.Entry(frame, show="*", width=30)
entry.pack(pady=5)
entry.bind("<KeyRelease>", evaluate_password)  # Sync with typing

result_label = tk.Label(frame, text="", font=("Arial", 12))
result_label.pack()

feedback_label = tk.Label(frame, text="", font=("Arial", 10), wraplength=350, justify="left")
feedback_label.pack()

root.mainloop()
