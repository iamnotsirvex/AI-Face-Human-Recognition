import cv2
import time
import argparse
import logging
import os
from typing import Tuple, List
from .utils import parse_source


logger = logging.getLogger(__name__)


def load_cascade(path: str = None) -> cv2.CascadeClassifier:
    if path is None:
        path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    cascade = cv2.CascadeClassifier(path)
    if cascade.empty():
        raise RuntimeError(f"Failed to load cascade from: {path}")
    return cascade


def detect_faces(gray_frame, face_cascade) -> List[Tuple[int, int, int, int]]:
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    return faces


def annotate_frame(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Human", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return frame


def main(source='0', show_fps=True, display=True, out_dir=None):
    src = parse_source(source)
    try:
        cap = cv2.VideoCapture(int(src)) if isinstance(src, int) else cv2.VideoCapture(src)
    except Exception:
        cap = cv2.VideoCapture(src)

    if not cap.isOpened():
        logger.error("Cannot open source: %s", src)
        return

    face_cascade = load_cascade()
    prev_time = time.time()
    saved = 0

    os.makedirs(out_dir, exist_ok=True) if out_dir else None

    while True:
        ret, frame = cap.read()
        if not ret:
            logger.info("Frame read failed or stream ended, exiting")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detect_faces(gray, face_cascade)
        annotate_frame(frame, faces)

        if show_fps:
            cur_time = time.time()
            fps = 1.0 / (cur_time - prev_time) if cur_time != prev_time else 0.0
            prev_time = cur_time
            cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        if display:
            cv2.imshow('Face Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        if out_dir and len(faces) > 0:
            fname = os.path.join(out_dir, f"capture_{saved:04d}.jpg")
            cv2.imwrite(fname, frame)
            saved += 1

    cap.release()
    if display:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='Real-time face detection (Haar cascade).')
    parser.add_argument('--source', default='0', help='Video source (camera index or file path). Default=0')
    parser.add_argument('--no-display', dest='display', action='store_false', help='Do not show video window')
    parser.add_argument('--no-fps', dest='show_fps', action='store_false', help='Do not show FPS')
    parser.add_argument('--out', dest='out_dir', help='Directory to save snapshots when faces are detected')
    args = parser.parse_args()
    main(source=args.source, show_fps=args.show_fps, display=args.display, out_dir=args.out_dir)
