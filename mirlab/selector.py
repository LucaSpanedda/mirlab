import tkinter as tk
from tkinter import filedialog

# select a file with Tk, then write it as a temp file
def select_file_with_gui():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select WAV file", filetypes=[("WAV files", "*.wav")])
    root.destroy()

    if file_path:
        with open(".selected_audio.txt", "w") as f:
            f.write(file_path + "\n")
        print(f"File saved in temporary file: {file_path}")
        return file_path
    return None
