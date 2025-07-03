import sys
import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

def plot_rms_db(filename, hop_ms=50, smooth=True):
    y, sr = librosa.load(filename, sr=None, mono=True)
    hop_length = int(sr * hop_ms / 1000)

    rms = librosa.feature.rms(y=y, hop_length=hop_length)[0]
    rms_db = librosa.amplitude_to_db(rms, ref=np.max)

    if smooth:
        rms_db = gaussian_filter1d(rms_db, sigma=1)

    times = librosa.frames_to_time(np.arange(len(rms_db)), sr=sr, hop_length=hop_length)

    plt.figure(figsize=(10, 4), facecolor='white')
    plt.plot(times, rms_db, color='black', linewidth=1)
    plt.xlabel(" ", color='black')
    plt.ylabel("RMS dB", color='black')
    plt.title(" ", color='black')

    ax = plt.gca()
    ax.set_facecolor("white")
    ax.tick_params(axis='both', colors='black')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    try:
        with open(".selected_audio.txt", "r") as f:
            filename = f.readline().strip()
    except FileNotFoundError:
        print("Errore: .selected_audio.txt non trovato.")
        sys.exit(1)

    hop_ms = 50  # default
    if len(sys.argv) > 1:
        try:
            hop_ms = int(sys.argv[1])
        except ValueError:
            print("Errore: hop_ms deve essere un intero.")
            sys.exit(1)

    plot_rms_db(filename, hop_ms)
