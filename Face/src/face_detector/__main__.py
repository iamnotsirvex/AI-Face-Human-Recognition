try:
    # normal package execution (python -m face_detector)
    from .detector import main
except Exception:
    # allow running as a script (python src\face_detector\__main__.py)
    import os
    import sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    sys.path.insert(0, os.path.join(ROOT, 'src'))
    from face_detector.detector import main


if __name__ == "__main__":
    main()
