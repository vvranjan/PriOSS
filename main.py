import tkinter as tk
from tkinter import ttk
import json

# Load data
with open("Userdata.json", 'r') as f:
    userdata = json.load(f)
with open("StreamingHistory.json", 'r') as f:
    streaming_history = json.load(f)
with open("Inferences.json", 'r') as f:
    inferences = json.load(f)

def create_gui():
    # Create main window
    window = tk.Tk()
    window.title("Spotify User Data Visualization")
    window.geometry("800x600")

    # Userdata GUI
    profile_frame = ttk.LabelFrame(window, text="User Profile", padding=(10, 5))
    profile_frame.pack(padx=10, pady=10, fill="x")
    labels = ["Username", "Email", "Country", "Birthdate", "Gender", "Creation Time"]
    keys = ["username", "email", "country", "birthdate", "gender", "creationTime"]
    for i, (label, key) in enumerate(zip(labels, keys)):
        ttk.Label(profile_frame, text=label).grid(row=i, column=0, padx=5, pady=2, sticky="w")
        ttk.Label(profile_frame, text=userdata[key]).grid(row=i, column=1, padx=5, pady=2, sticky="w")

    # StreamingHistory GUI (showing only the recent 10 songs for simplicity)
    history_frame = ttk.LabelFrame(window, text="Recent Streaming History", padding=(10, 5))
    history_frame.pack(padx=10, pady=10, fill="x")
    labels = ["End Time", "Artist", "Track", "Duration (ms)"]
    keys = ["endTime", "artistName", "trackName", "msPlayed"]
    for i, label in enumerate(labels):
        ttk.Label(history_frame, text=label).grid(row=0, column=i, padx=5, pady=2)
    for row, song in enumerate(streaming_history[:10], start=1):
        for col, key in enumerate(keys):
            ttk.Label(history_frame, text=song[key]).grid(row=row, column=col, padx=5, pady=2)

    # Inferences GUI
    inferences_frame = ttk.LabelFrame(window, text="Inferences", padding=(10, 5))
    inferences_frame.pack(padx=10, pady=10, fill="x")
    for i, inference in enumerate(inferences["inferences"]):
        color = "blue" if "1P" in inference else "red"
        label = ttk.Label(inferences_frame, text=inference, background=color, foreground="white")
        label.grid(row=i//4, column=i%4, padx=5, pady=2, sticky="w")

    window.mainloop()

# Run the GUI
create_gui()
