AUDIO TEST LOG ANALYZER
=======================

Web version: index.html + lib/ (hosted on Vercel, no build step).

Desktop version: app.py wraps index.html in a window using pywebview.
It is built into a Windows installer by GitHub Actions
(.github/workflows/build-installer.yml) when a tag like v1.0.0 is pushed,
or when the workflow is run manually from the Actions tab.

Local build (optional): run build.bat on Windows, result is
dist\AudioTestLogAnalyzer.exe.

Note: pywebview uses the WebView2 runtime (preinstalled on current
Windows 10/11).
