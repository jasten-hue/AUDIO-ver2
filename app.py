import os
import sys

import webview


def resource_path(relative_path):
    """Resolve a bundled read-only resource (index.html, lib/, app.ico) so it
    works both as a normal .py script and as a frozen PyInstaller .exe."""
    try:
        base_path = sys._MEIPASS  # set by PyInstaller at runtime
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def main():
    index_path = resource_path("index.html")
    icon_path = resource_path("app.ico")

    webview.create_window(
        "Audio Test Log Analyzer",
        index_path,
        width=1440,
        height=900,
        min_size=(1000, 700),
    )

    # `icon=` needs pywebview 4.1+.
    webview.start(icon=icon_path)


if __name__ == "__main__":
    main()
