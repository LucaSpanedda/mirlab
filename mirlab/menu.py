import os
import subprocess
import librosa
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Vertical
from textual.reactive import reactive

class MenuItem(Static):
    is_selected = reactive(False)
    width = 50  # larghezza fissa per uniformare i box
    
    def __init__(self, text, module_name=None, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.module_name = module_name or text.lower().replace(" ", "_")

    def render(self):
        text = self.renderable
        padding = self.width - len(text)
        left_pad = padding // 2
        right_pad = padding - left_pad
        padded_text = " " * left_pad + text + " " * right_pad

        border_line = "─" * self.width
        if self.is_selected:
            # evidenzia con sfondo bianco e testo nero
            style = "bold black on white"
            border_style = "white"
        else:
            style = "white on black"
            border_style = "white"

        lines = [
            f"[{border_style}]┌{border_line}┐[/]",
            f"[{border_style}]│[/][{style}]{padded_text}[/{style}][{border_style}]│[/]",
            f"[{border_style}]└{border_line}┘[/]",
        ]
        return "\n".join(lines)

class MIRMenu(App):
    CSS_PATH = os.path.join(os.path.dirname(__file__), "menu.tcss")

    def get_audio_info(self):
        try:
            with open(".selected_audio.txt") as f:
                path = f.read().strip()
            if not os.path.isfile(path):
                return "No valid audio file selected."

            y, sr = librosa.load(path, sr=None, mono=False)
            duration = librosa.get_duration(y=y, sr=sr)
            channels = 1 if y.ndim == 1 else y.shape[0]

            info = (
                f"File: {os.path.basename(path)}\n"
                f"Sample Rate: {sr} Hz | "
                f"Duration: {int(duration // 60)} min {int(duration % 60)} sec | "
                f"Channels: {channels}"
            )
            return info
        except Exception as e:
            return f"Errore nel caricamento file audio:\n{e}"

    def get_analysis_modules(self):
        analysis_dir = os.path.join(os.path.dirname(__file__), "analysis")
        modules = [
            f[:-3] for f in os.listdir(analysis_dir)
            if f.endswith(".py") and f != "__init__.py"
        ]
        return sorted(modules)

    def compose(self) -> ComposeResult:
        yield Static(self.get_audio_info(), classes="header")
        modules = self.get_analysis_modules()
        self.menu_items = [MenuItem(mod.replace("_", " ").title(), mod) for mod in modules]
        self.menu_items.append(MenuItem("Exit", "exit"))
        # Contenitore verticale centrato
        yield Vertical(*self.menu_items, classes="menu")
        self.selected_index = 0
        self.menu_items[self.selected_index].is_selected = True

    def on_key(self, event):
        if event.key == "down":
            self.menu_items[self.selected_index].is_selected = False
            self.selected_index = (self.selected_index + 1) % len(self.menu_items)
            self.menu_items[self.selected_index].is_selected = True
        elif event.key == "up":
            self.menu_items[self.selected_index].is_selected = False
            self.selected_index = (self.selected_index - 1) % len(self.menu_items)
            self.menu_items[self.selected_index].is_selected = True
        elif event.key == "enter":
            selected_item = self.menu_items[self.selected_index]
            module_name = selected_item.module_name
            if module_name == "exit":
                self.exit()
            else:
                subprocess.run(["python3", "-m", f"mirlab.analysis.{module_name}"])

if __name__ == "__main__":
    MIRMenu().run()
