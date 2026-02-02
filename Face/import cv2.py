# WARNING: Filename shadowing issue
# This file is named 'import cv2.py' which will shadow the real 'cv2' package when importing.
# Please rename or delete this file (for example to 'old_import_cv2.py') to avoid errors.
raise SystemExit("Rename 'import cv2.py' to avoid shadowing the 'cv2' package")

while True:
    ret, frame = cap.read()
    if not ret: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()