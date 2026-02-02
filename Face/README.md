# Face Detection (webcam) 🚀

A small, modular Python project for real-time face (human) detection using OpenCV's Haar cascade.

## Project structure

- `src/face_detector/` — package source
  - `detector.py` — main capture/detection logic
  - `utils.py` — small helpers
- `tests/` — unit tests (pytest)
- `face_detection.py` — convenience script (entrypoint for legacy usage)
- `requirements.txt` — runtime deps
- `requirements-dev.txt` — dev deps for testing & linting
- `README.md`, `LICENSE`, `.gitignore`, `setup.py`

## Quickstart (Windows PowerShell) ⚡

1. Create & activate venv
   - `python -m venv .venv`
   - `.\.venv\Scripts\Activate.ps1`
2. Install runtime deps
   - `python -m pip install --upgrade pip`
   - `python -m pip install -r requirements.txt`
3. (Optional) Install project in editable mode to get `face-detect` console script:
   - `pip install -e .`
4. Run
   - `python face_detection.py` (legacy)
   - `python -m face_detector` (run as package)
   - `face-detect` (after pip install)
   - To use another camera or file: `python face_detection.py --source 1` or `--source path\to\video.mp4` or `python -m face_detector --source 1`
   - Use `--out out_dir` to save snapshots when faces are detected
5. Press `q` to quit

## Tests

- Run unit tests with:
  - `pytest -q`

## Notes & tips 💡

- If you still have a file named `import cv2.py` in this folder, **rename or remove** it; it will shadow the real `cv2` package and break imports.
- To create a distributed package, use `python setup.py sdist bdist_wheel` or configure `pyproject.toml`.
