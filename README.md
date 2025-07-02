# mirlab

**mirlab** is a terminal-based audio analysis toolkit designed for inspection of
audio files.
It features a TUI (Text User Interface),
automated script discovery,
and modular audio feature extraction using Python.

---

## What It Does

- Lets you **select a `.wav` file** via graphical file picker (Tkinter)
- Displays **key info** about the file: sample rate, duration, channels
- Launches a **TUI menu** (based on [Textual](https://textual.textualize.io/))
- Each analysis is a separate Python module located in the `mirlab/analysis/` directory
- The TUI is **automatically populated** with all available analysis scripts

---

## Requirements

- Python **3.8+**

### Python Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install numpy scipy matplotlib librosa textual
```

---

## Installation

```bash
git clone https://github.com/yourusername/mirlab.git
cd mirlab
pip install .
```

After installation, you can launch the tool from anywhere using:

```bash
mirlab
```

---

## Usage

1. A GUI will ask you to select a `.wav` file.
2. After selection, a clean black-and-white terminal menu will appear.
3. Choose an analysis from the list — it will open a plot or perform computation.

---

## 📂 Folder Structure

```
mirlab/
│
├── analysis/              # Drop your custom analysis scripts here
│   ├── fft.py
│   ├── recurrence.py
│   ├── spectral_centroid.py
│   ├── oscilloscope.py
│   └── ...
│
├── menu.py                # TUI menu using Textual
├── selector.py            # File selector using Tkinter
├── launcher.py            # Entry point (used by the CLI)
├── menu.tcss              # Textual style sheet (black & white theme)
│
├── setup.py               # Install config
└── README.md              # This file
```

---

## Adding New Analyses

Simply add a new `.py` script to the `mirlab/analysis/` folder. The script must be executable via:

```bash
python3 -m mirlab.analysis.your_script
```

The name will appear automatically in the menu, formatted in a readable way.

---

## License

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
Copyright (C) 2025 Luca Spanedda

---

## Contributing

Pull requests and forks are welcome.  
Open an issue for suggestions or bugs.
