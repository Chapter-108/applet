# -*- coding: utf-8 -*-
import cv2
tracker = None
tracking = False

cap = cv2.VideoCapture(0)

window_width = 800
window_height = 600
cv2.namedWindow('Tracking', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Tracking', window_width, window_height)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if cv2.waitKey(1) == ord('a'):
        tracking = True
        roi = cv2.selectROI('Tracking', frame, False)
        tracker = cv2.TrackerCSRT_create()
        tracker.init(frame, roi)

    if tracking and tracker is not None:
        success, bbox = tracker.update(frame)
        if success:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Tracking', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
