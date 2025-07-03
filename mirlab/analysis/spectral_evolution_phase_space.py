import sys
import librosa
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import CheckButtons

def plot_phase_space_with_toggles(filename, hop_length=2048):
    y, sr = librosa.load(filename, sr=None)

    centroid = librosa.feature.spectral_centroid(y=y, sr=sr, hop_length=hop_length)[0]
    bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr, hop_length=hop_length)[0]
    rms = librosa.feature.rms(y=y, hop_length=hop_length)[0]

    centroid /= np.max(centroid)
    bandwidth /= np.max(bandwidth)
    rms /= np.max(rms)

    n_points = len(centroid)
    colors = [(0, 0, 0, alpha) for alpha in np.linspace(0.2, 1.0, n_points)]

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    scatter = ax.scatter(centroid, bandwidth, rms, color=colors, s=1)
    line, = ax.plot(centroid, bandwidth, rms, color='black', linewidth=0.1, alpha=0.8)

    ax.set_title("Spectral Phase Space (Points + Trail)", fontsize=12, color='black')

    def toggle_box(label):
        visible = check_box.get_status()[0]
        if visible:
            ax.grid(False)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_zticks([])
            ax.xaxis.pane.set_facecolor((1,1,1,1))
            ax.yaxis.pane.set_facecolor((1,1,1,1))
            ax.zaxis.pane.set_facecolor((1,1,1,1))
            ax._axis3don = True
        else:
            ax.xaxis.pane.set_facecolor((1,1,1,0))
            ax.yaxis.pane.set_facecolor((1,1,1,0))
            ax.zaxis.pane.set_facecolor((1,1,1,0))
            ax._axis3don = False
        plt.draw()

    def toggle_line(label):
        visible = check_line.get_status()[0]
        line.set_visible(visible)
        plt.draw()

    ax_check_box = plt.axes([0.005, 0.95, 0.03, 0.03], facecolor='white')
    check_box = CheckButtons(ax_check_box, [''], [True])
    for label in check_box.labels:
        label.set_fontsize(1)
    for spine in ax_check_box.spines.values():
        spine.set_visible(False)
    ax_check_box.set_xticks([])
    ax_check_box.set_yticks([])
    check_box.on_clicked(toggle_box)

    ax_check_line = plt.axes([0.005, 0.90, 0.03, 0.03], facecolor='white')
    check_line = CheckButtons(ax_check_line, [''], [True])
    for label in check_line.labels:
        label.set_fontsize(1)
    for spine in ax_check_line.spines.values():
        spine.set_visible(False)
    ax_check_line.set_xticks([])
    ax_check_line.set_yticks([])
    check_line.on_clicked(toggle_line)

    toggle_box('init')
    toggle_line('init')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        with open(".selected_audio.txt", "r") as f:
            filename = f.readline().strip()
    except FileNotFoundError:
        print("Errore: .selected_audio.txt non trovato.")
        sys.exit(1)

    hop_length = 2048  # default
    if len(sys.argv) > 1:
        try:
            hop_length = int(sys.argv[1])
        except ValueError:
            print("Errore: hop_length deve essere un intero.")
            sys.exit(1)

    plot_phase_space_with_toggles(filename, hop_length)
