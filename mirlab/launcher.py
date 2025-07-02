import subprocess
import sys
from mirlab.selector import select_file_with_gui

def main():
    wav_path = select_file_with_gui()
    if not wav_path:
        print("\nNo file selected.")
        sys.exit(1)

    print("\nFile selection complete.\nLaunching TUI for analysis...")
    subprocess.run(["python3", "-m", "mirlab.menu"])

if __name__ == "__main__":
    main()
