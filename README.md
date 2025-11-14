# Warranty
A private project for my friend's boss

## Installation

### Clone the repository
```bash
git clone https://github.com/Oceanman07/Warranty.git && cd Warranty
```

### Install uv
https://docs.astral.sh/uv/#installation

### Environment setup
```bash
uv venv
```
```bash
uv pip install .
```
```bash
source .venv/bin/activate
```

### Development
```bash
uv run main.py
```

### Build
macOS
```bash
pyinstaller --noconfirm --noconsole --windowed --icon icons/icon.icns --collect-all customtkinter --name Warranty main.py
```
