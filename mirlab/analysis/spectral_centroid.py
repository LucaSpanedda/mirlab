import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def plot_centroid_and_kde_matplotlib(filename, hop_ms=100):
    y, sr = librosa.load(filename, sr=None)
    hop_length = int(sr * hop_ms / 1000)
    n_fft = max(2048, hop_length)

    centroids = librosa.feature.spectral_centroid(y=y, sr=sr, hop_length=hop_length, n_fft=n_fft)[0]
    times = librosa.frames_to_time(np.arange(len(centroids)), sr=sr, hop_length=hop_length)

    kde = gaussian_kde(centroids)
    freq_range = np.linspace(0, sr / 2, 1000)
    density = kde(freq_range)

    fig, axs = plt.subplots(2, 1, figsize=(12, 8), facecolor='white')

    axs[0].plot(times, centroids, color='black', linewidth=1.5)
    axs[0].set_title(' ', color='black')
    axs[0].set_xlabel(' ', color='black')
    axs[0].set_ylabel('Hz', color='black')
    axs[0].tick_params(colors='black')

    axs[1].plot(freq_range, density, color='black', linewidth=1.5)
    axs[1].set_title(' ', color='black')
    axs[1].set_xlabel('Hz', color='black')
    axs[1].set_ylabel('Density KDE', color='black')
    axs[1].tick_params(colors='black')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    with open(".selected_audio.txt") as f:
        path = f.readline().strip()
    plot_centroid_and_kde_matplotlib(path)
