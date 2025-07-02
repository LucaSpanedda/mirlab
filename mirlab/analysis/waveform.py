import numpy as np
import scipy.io.wavfile as wav
import matplotlib
matplotlib.use('MacOSX')  # o "TkAgg" se su altri sistemi
import matplotlib.pyplot as plt

def plot_oscilloscope():
    with open(".selected_audio.txt", "r") as f:
        filename = f.readline().strip()

    rate, data = wav.read(filename)

    if data.ndim == 1:
        data = data[:, np.newaxis]

    num_channels = data.shape[1]
    duration = data.shape[0] / rate
    time = np.linspace(0, duration, data.shape[0])

    if np.issubdtype(data.dtype, np.integer):
        max_val = np.iinfo(data.dtype).max
        data = data / max_val

    fig, axes = plt.subplots(num_channels, 1, figsize=(10, 2 * num_channels), sharex=True, facecolor='white')
    if num_channels == 1:
        axes = [axes]

    for i, ax in enumerate(axes):
        ax.plot(time, data[:, i], color='black', linewidth=0.5)
        ax.set_facecolor('white')
        ax.set_ylabel(" ", color='black')
        ax.spines['bottom'].set_color('black')
        ax.spines['top'].set_color('black')
        ax.spines['left'].set_color('black')
        ax.spines['right'].set_color('black')
        ax.tick_params(axis='both', colors='black')

    axes[-1].set_xlabel(" ", color='black')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_oscilloscope()
