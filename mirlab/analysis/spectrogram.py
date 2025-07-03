#!/usr/bin/env python3

import sys
import numpy as np
import librosa
import matplotlib.pyplot as plt

def plot_spectrogram(filename, n_fft=2048, hop_length=512):
    y, sr = librosa.load(filename, sr=None)

    # Calcolo spettrogramma
    S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))
    S_db = 20 * np.log10(S + 1e-12)
    S_db -= np.max(S_db)  # normalizza a 0 dB

    # Parametri per la visualizzazione
    times = librosa.frames_to_time(np.arange(S.shape[1]), sr=sr, hop_length=hop_length)
    freqs = np.linspace(0, sr/2, S.shape[0])

    fig, ax = plt.subplots(figsize=(12, 6))

    img = ax.imshow(
        S_db,
        origin="lower",
        aspect="auto",
        cmap="gray_r",      # bianco basso livello, nero alto livello
        extent=[times[0], times[-1], freqs[0], freqs[-1]],
        interpolation="nearest",
        vmin=-80, vmax=0    # dinamica in dB
    )

    ax.set_xlabel("Time (s)", color='black')
    ax.set_ylabel("Frequency (Hz)", color='black')
    ax.set_title("Minimal Spectrogram (Black Harmonics)", color='black')
    ax.set_facecolor('white')
    ax.tick_params(colors='black')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(False)

    fig.patch.set_facecolor('white')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        with open(".selected_audio.txt", "r") as f:
            filename = f.readline().strip()
    except FileNotFoundError:
        print("Errore: .selected_audio.txt non trovato.")
        sys.exit(1)

    # Opzionale: lettura hop_length da argomento riga di comando
    hop_length = 512
    if len(sys.argv) > 1:
        try:
            hop_length = int(sys.argv[1])
        except ValueError:
            print("Attenzione: hop_length deve essere un intero, uso valore di default 512.")

    plot_spectrogram(filename, hop_length=hop_length)
