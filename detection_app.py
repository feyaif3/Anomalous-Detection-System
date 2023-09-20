import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox  # Import messagebox for pop-up messages
import os
import pandas as pd
import numpy as np

# Global variable to store the selected algorithm
selected_algorithm = ""

def start_detection(file_path):
    # Add your code for "Start Detection" here
    print("Starting detection with file:", file_path)
    detection_completed()

def detection_completed():
    # Display a pop-up message
    messagebox.showinfo("Detection Complete", "This file contains suspicious or anomalous activity")

def open_detection_page(selected_file):
    # Create a new window for detection
    detection_window = tk.Toplevel(root)
    detection_window.title("Detection Page")

    # Add a label with the selected file name (not the full path)
    selected_file_name = os.path.basename(selected_file)
    selected_file_label = tk.Label(
        detection_window, text="File selected: " + selected_file_name, font=("Arial", 12))
    selected_file_label.pack(pady=10)

    # Add text with a message
    message_text = "This file will go through the detection process. Any anomalous attacks will be declared."
    message_label = tk.Label(
        detection_window, text=message_text, font=("Arial", 12))
    message_label.pack(pady=10)

    # Add a button for confirmation
    confirm_button = tk.Button(detection_window, text="Confirm",
                               command=lambda: start_detection(selected_file), **button_style)
    confirm_button.pack(pady=10)

    # Add a button to cancel and close the detection window
    cancel_button = tk.Button(
        detection_window, text="Cancel", command=detection_window.destroy, **button_style)
    cancel_button.pack(pady=10)

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        open_detection_page(file_path)

def train_model():
    # Create a new window for training algorithm selection
    train_window = tk.Toplevel(root)
    train_window.title("Select Algorithm to Train Deep Model")

    # Add a label to instruct the user
    label = tk.Label(train_window, text="Select an algorithm to train the deep model:")
    label.pack(pady=10)

    # Add radio buttons for algorithm selection
    reinforcement_learning_button = tk.Radiobutton(train_window, text="Deep Reinforcement Learning",
                                                  variable=selected_algorithm, value="Reinforcement Learning")
    autoencoders_button = tk.Radiobutton(train_window, text="Multistage Autoencoders",
                                         variable=selected_algorithm, value="Autoencoders")

    # Pack the radio buttons
    reinforcement_learning_button.pack()
    autoencoders_button.pack()

    # Add a button to confirm the selected algorithm
    confirm_button = tk.Button(train_window, text="Confirm",
                               command=train_completed, **button_style)
    confirm_button.pack(pady=10)

def train_completed():
    global selected_algorithm
    # Display a pop-up message
    if selected_algorithm:
        messagebox.showinfo("Training Complete", "Training complete.")
    else:
        messagebox.showerror("Error", "Please select an algorithm first.")

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Anomalous Attack Detection System")  # Set the title
root.geometry("600x500")  # Set the window size

# Customize the title label (make it red)
title_label = tk.Label(
    root, text="Anomalous Attack Detection System", font=("Arial", 20), fg="red")
title_label.pack(pady=20)

# Customize the buttons (making them rounded)
button_style = {
    "font": ("Helvetica", 12),
    "relief": tk.RAISED,
    "borderwidth": 3,
    "width": 15,
    "height": 1,
    "bg": "lightgray",
    "activebackground": "gray"
}

start_button = tk.Button(root, text="Detect Attack",
                         command=select_file, **button_style)
start_button.pack(pady=10)

train_button = tk.Button(root, text="Train Model",
                         command=train_model, **button_style)
train_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app, **button_style)
exit_button.pack(pady=10)

# Initialize the selected_algorithm variable
selected_algorithm = tk.StringVar()

# Start the Tkinter main loop
root.mainloop()
