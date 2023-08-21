import tkinter as tk
from tkinter import filedialog
import os


def start_detection(file_path):
    # Add your code for "Start Detection" here
    print("Starting detection with file:", file_path)


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
    message_text = "This file will not go through the detection process. Any anomalous attacks will be declared."
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
    # Add your code for "Train Model" here
    pass


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

# Start the Tkinter main loop
root.mainloop()
