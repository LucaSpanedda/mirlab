#!/usr/bin/env python3

import sys
import librosa
import numpy as np
import matplotlib.pyplot as plt

def plot_centroid_and_spread(filename, hop_ms=100):
    y, sr = librosa.load(filename, sr=None, mono=True)
    hop_length = int(sr * hop_ms / 1000)

    # Feature
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr, hop_length=hop_length)[0]
    spread = librosa.feature.spectral_bandwidth(y=y, sr=sr, hop_length=hop_length)[0]
    times = librosa.frames_to_time(np.arange(len(centroid)), sr=sr, hop_length=hop_length)

    # Plot
    fig, axs = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

    axs[0].plot(times, centroid, color='black', linewidth=1)
    axs[0].set_ylabel("Spectral Centroid (Hz)", color='black')
    axs[0].set_title(" ", color='black')
    axs[0].set_ylim(0, sr/2)

    axs[1].plot(times, spread, color='black', linewidth=1)
    axs[1].set_ylabel("Spectral Spread (Hz)", color='black')
    axs[1].set_xlabel("Time (s)", color='black')
    axs[1].set_title(" ", color='black')
    axs[1].set_ylim(0, sr/2)

    # stile minimal
    for ax in axs:
        ax.set_facecolor('white')
        ax.tick_params(colors='black')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('black')
        ax.spines['bottom'].set_color('black')
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

    hop_ms = 100  # default
    if len(sys.argv) > 1:
        try:
            hop_ms = int(sys.argv[1])
        except ValueError:
            print("Errore: hop_ms deve essere un intero (millisecondi).")
            sys.exit(1)

    plot_centroid_and_spread(filename, hop_ms)
