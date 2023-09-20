import os
import tkinter as tk
from tkinter import filedialog

def display_menu():
    print("Anomalous Detection Application")
    print("1. Detect Attack")
    print("2. Train Model")
    print("3. Exit")

def detect_attack():
    print("Detecting attack...")

    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Ask the user to select a file using a file dialog
    file_path = filedialog.askopenfilename(title="Select a file for analysis")

    if file_path:
        print(f"Selected file: {file_path}")
        confirmation = input("Do you want to start detecting? (confirm/cancel): ")

        if confirmation.lower() == "confirm":
            # Add your code here to start detecting
            print("Detection process started...")
        else:
            print("Detection canceled.")
    else:
        print("No file selected. Detection canceled.")

def train_model():
    print("Training model...")
    # Add your code for model training here

while True:
    display_menu()
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        detect_attack()
    elif choice == '2':
        train_model()
    elif choice == '3':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")
