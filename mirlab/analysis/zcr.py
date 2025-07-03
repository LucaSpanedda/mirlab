import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def zero_crossing_rate(signal, frame_size, hop_size):
    zcr_values = []
    for start in range(0, len(signal) - frame_size, hop_size):
        frame = signal[start:start+frame_size]
        crossings = np.where(np.diff(np.sign(frame)))[0]
        zcr = len(crossings) / frame_size
        zcr_values.append(zcr)
    return np.array(zcr_values)

def plot_zcr(filepath, frame_duration=0.05):
    rate, data = wav.read(filepath)

    # Mono
    if data.ndim > 1:
        data = data[:, 0]

    # Normalizza se interi
    if np.issubdtype(data.dtype, np.integer):
        data = data / np.iinfo(data.dtype).max

    frame_size = int(rate * frame_duration)
    hop_size = frame_size  # Nessun overlap

    zcr = zero_crossing_rate(data, frame_size, hop_size)

    times = np.arange(len(zcr)) * (hop_size / rate)

    plt.figure(figsize=(12, 4), facecolor='white')
    plt.plot(times, zcr, color='black', linewidth=1)
    plt.xlabel(" ", color='black')
    plt.ylabel("ZCR", color='black')    # etichetta Y aggiornata
    plt.title(" ", color='black')
    plt.grid(False)
    ax = plt.gca()
    ax.set_facecolor("white")
    ax.tick_params(axis='both', colors='black')
    for spine in ax.spines.values():
        spine.set_color('black')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        with open(".selected_audio.txt", "r") as f:
            filename = f.readline().strip()
    except FileNotFoundError:
        print("Errore: .selected_audio.txt non trovato.")
        sys.exit(1)

    frame_duration = 0.05  # default
    if len(sys.argv) > 1:
        try:
            frame_duration = float(sys.argv[1])
        except ValueError:
            print("Errore: frame_duration deve essere un numero (secondi).")
            sys.exit(1)

    plot_zcr(filename, frame_duration)
