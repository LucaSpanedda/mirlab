#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
import librosa
from scipy.signal import freqz

def plot_fft_and_spectral_envelope(filename, frame_length=2048, lpc_order=16):
    y, sr = librosa.load(filename, sr=None)

    # Frame al centro
    center = len(y) // 2
    start = max(0, center - frame_length // 2)
    end = min(len(y), start + frame_length)
    frame = y[start:end]

    # Finestra di Hann
    windowed = frame * np.hanning(len(frame))

    # FFT
    n_fft = frame_length * 4
    spectrum = np.abs(np.fft.fft(windowed, n=n_fft))[:n_fft // 2]
    spectrum_db = 20 * np.log10(spectrum + 1e-12)
    spectrum_db -= np.max(spectrum_db)
    freqs = np.linspace(0, sr/2, n_fft // 2)

    # LPC envelope
    a = librosa.lpc(windowed, order=lpc_order)
    w, h = freqz([1], a, worN=n_fft // 2, fs=sr)
    envelope_db = 20 * np.log10(np.abs(h) + 1e-12)
    envelope_db -= np.max(envelope_db)

    # Plot con due pannelli
    fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # FFT
    axs[0].plot(freqs, spectrum_db, color="black", linewidth=1)
    axs[0].set_ylabel("FFT dB", color='black')
    axs[0].set_title(" ", color='black')
    axs[0].set_xlim(0, sr/2)
    axs[0].set_ylim(-100, 0)

    # LPC
    axs[1].plot(w, envelope_db, color="black", linewidth=1)
    axs[1].set_xlabel("Hz", color='black')
    axs[1].set_ylabel("LPC dB", color='black')
    axs[1].set_title(" ", color='black')
    axs[1].set_xlim(0, sr/2)
    axs[1].set_ylim(-100, 0)

    # Stile minimal
    for ax in axs:
        ax.set_facecolor('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('black')
        ax.spines['bottom'].set_color('black')
        ax.tick_params(colors='black')
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

    # parametri opzionali
    frame_length = 2048
    lpc_order = 16

    if len(sys.argv) > 1:
        try:
            frame_length = int(sys.argv[1])
        except ValueError:
            print("Errore: frame_length deve essere un intero.")
            sys.exit(1)

    if len(sys.argv) > 2:
        try:
            lpc_order = int(sys.argv[2])
        except ValueError:
            print("Errore: lpc_order deve essere un intero.")
            sys.exit(1)

    plot_fft_and_spectral_envelope(filename, frame_length, lpc_order)
