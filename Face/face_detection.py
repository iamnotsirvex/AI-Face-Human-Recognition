# Convenience wrapper — calls the package entrypoint and exposes CLI
import argparse
from face_detector.detector import main


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Real-time face detection (Haar cascade).')
    parser.add_argument('--source', default='0', help='Video source (camera index or file path). Default=0')
    parser.add_argument('--no-display', dest='display', action='store_false', help='Do not show video window')
    parser.add_argument('--no-fps', dest='show_fps', action='store_false', help='Do not show FPS')
    parser.add_argument('--out', dest='out_dir', help='Directory to save snapshots when faces are detected')
    args = parser.parse_args()
    main(source=args.source, show_fps=args.show_fps, display=args.display, out_dir=args.out_dir)
