# Python Advance — Context Managers & File Utilities

A small, Python project to practice **context managers**, safe file handling, and utility modules.
Tested on **Python 3.12** (Git Bash on Windows).

## Project Structure

```
python-advance/
│  .gitignore
│  .python-version
│  example.txt
│  main.py
│  pyproject.toml
│  README.md
│  test.txt
│  uv.lock
│
├─ .venv/                 # local virtual environment (created by uv/venv)
└─ utils/
   │  file_opener.py      # class-based context manager: safe open/close files
   │  email_layout.py     # helper(s) for building email bodies/layouts
   │  email_layout_cl.py  # (optional) CLI or class-based variant for emails
   │  __init__.py
   └─ __pycache__/
---

## Quick Start

### 1) Create/activate venv

Using **uv** (recommended):

```bash
uv venv
uv sync
```

Or with Python’s built-in venv:

```bash
python -m venv .venv
source .venv/Scripts/activate      # Git Bash / PowerShell: .\.venv\Scripts\Activate.ps1
pip install -U pip
```

*(No external deps yet; `pyproject.toml`/`uv.lock` are ready for future additions.)*

### 2) Run the demo

```bash
uv run python main.py
# or
python main.py
```

---

## Usage

### A) Class-based Context Manager (FileOpener)

`utils/file_opener.py` implements a **context manager** that opens a file and guarantees closing it—even on errors.

**Write example:**

```python
from utils.file_opener import FileOpener

with FileOpener("example.txt", "w") as f:
    f.write("Hello from FileOpener!\n")
```

**Read example:**

```python
from utils.file_opener import FileOpener

with FileOpener("example.txt", "r") as f:
    for line in f:
        print(line.rstrip())
```

### B) Email helpers (optional)

* `utils/email_layout.py` – put common functions/classes for composing email bodies (subjects, headers, footers).
* `utils/email_layout_cl.py` – a CLI or class-based variant (e.g., generate a formatted preview).

Example (adapt to your functions/classes):

```python
from utils.email_layout import build_newsletter  # ← replace with your actual function/class

html = build_newsletter(title="Weekly Update", items=["Item 1", "Item 2"])
print(html)
```

---

## Why Context Managers?

* **Safety:** cleans up resources automatically (`__exit__` runs even on exceptions).
* **Clarity:** localizes resource lifetime to the `with ...:` block.
* **Extensible:** you can add variants later (gzip, atomic writes, etc.).

---

## Roadmap (nice next steps)

* `utils/cm.py`: add `@contextmanager`-style helpers (e.g., `open_text`, `timer`).
* `utils/atomic.py`: implement `atomic_write(path)` (write to temp → `fsync` → `os.replace`).
* Add simple tests (`pytest`) and a GitHub Action.

---
## License

Add your preferred license (MIT is common for learning projects).

---

## Author

Ahsen — practicing advanced Python patterns on Windows 💪
