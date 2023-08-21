import tkinter as tk


def start_detection():
    # Create a new window for detection
    detection_window = tk.Toplevel(root)
    detection_window.title("Detection Page")

    # Add a label with summary text
    summary_text = "This detection system is designed to find anomalous attacks on blockchain networks, with a focus on Bitcoin attacks."
    summary_label = tk.Label(
        detection_window, text=summary_text, font=("Arial", 12))
    summary_label.pack(pady=20)

    # Function to handle file selection
    def select_file():
        file_path = filedialog.askopenfilename()
        # Here, you can use the selected file_path for your detection logic
        print("Selected file:", file_path)

    # Add a button for file selection
    select_file_button = tk.Button(
        detection_window, text="Select File to Detect", command=select_file, **button_style)
    select_file_button.pack(pady=10)


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
title_label = tk.Label(root, text="Anomalous Attack Detection System", font=(
    "Arial", 20), fg="red")
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

start_button = tk.Button(root, text="Start Detection",
                         command=select_file, **button_style)
start_button.pack(pady=10)

train_button = tk.Button(root, text="Train Model",
                         command=train_model, **button_style)
train_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app, **button_style)
exit_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
