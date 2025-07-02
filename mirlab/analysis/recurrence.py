import librosa
import numpy as np
import matplotlib.pyplot as plt

def recurrence_matrix(data, threshold=None):
    N = len(data)
    dist = np.abs(data.reshape(-1,1) - data.reshape(1,-1))
    if threshold is None:
        threshold = np.median(dist)
    R = (dist <= threshold).astype(int)
    return R

def plot_recurrence_centroid(filename, hop_ms=100):
    y, sr = librosa.load(filename, sr=None)
    hop_length = int(sr * hop_ms / 1000)
    n_fft = max(2048, hop_length)

    centroids = librosa.feature.spectral_centroid(y=y, sr=sr, hop_length=hop_length, n_fft=n_fft)[0]

    R = recurrence_matrix(centroids)

    plt.figure(figsize=(8,8), facecolor="white")
    plt.imshow(R, origin='lower', cmap='binary', interpolation='none')
    plt.title("Recurrence Plot of Spectral Centroid", color='black')
    plt.xlabel("Frame Index", color='black')
    plt.ylabel("Frame Index", color='black')
    plt.xticks(color='black')
    plt.yticks(color='black')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    with open(".selected_audio.txt") as f:
        path = f.readline().strip()
    plot_recurrence_centroid(path)
