import subprocess
import sys
# if a file are selected, selector write the index in a temp file
from mirlab.selector import select_file_with_gui

# file selection true or false, launch TUI
def main():
    wav_path = select_file_with_gui()
    if not wav_path:
        print("\n" + "No file selected.")
        sys.exit(1)

    print("\n" + "File selection complete. \n Launching TUI for analysis...")
    subprocess.run(["python3", "-m", "mirlab.menu"])

if __name__ == "__main__":
    main()
