from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import Vertical
import subprocess
import librosa
import os

def get_analysis_scripts():
    analysis_dir = os.path.join(os.path.dirname(__file__), "analysis")
    scripts = []
    for filename in os.listdir(analysis_dir):
        if filename.endswith(".py") and not filename.startswith("__") and not filename.startswith("_"):
            script_name = filename[:-3]
            label = script_name.replace("_", " ").title()
            scripts.append((script_name, label))
    return scripts

class MIRMenu(App):
    CSS_PATH = "menu.tcss"

    def get_audio_info(self):
        try:
            with open(".selected_audio.txt") as f:
                path = f.read().strip()
            if not os.path.isfile(path):
                return "No valid audio file selected."
            y, sr = librosa.load(path, sr=None, mono=False)
            duration = librosa.get_duration(y=y, sr=sr)
            channels = 1 if y.ndim == 1 else y.shape[0]
            return (
                f"File: {os.path.basename(path)}\n"
                f"Sample Rate: {sr} Hz | "
                f"Duration: {int(duration // 60)} min {int(duration % 60)} sec | "
                f"Channels: {channels}"
            )
        except Exception as e:
            return f"Errore nel caricamento file audio:\n{e}"

    def compose(self) -> ComposeResult:
        yield Static(self.get_audio_info(), classes="header")
        buttons = [Button(label, id=script_id) for script_id, label in get_analysis_scripts()]
        buttons.append(Button("Exit", id="exit"))
        yield Vertical(*buttons, classes="menu")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id
        if btn_id == "exit":
            self.exit()
        else:
            subprocess.run(["python3", "-m", f"mirlab.analysis.{btn_id}"])

if __name__ == "__main__":
    MIRMenu().run()
