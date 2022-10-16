import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
camera = cv2.VideoCapture("rtsp://192.168.3.113:8554/fpv_stream")

while True:
    check, frame = camera.read()
    frame = cv2.resize(frame, (512, 256))

    results = model(frame)
    cv2.imshow('video', results.imgs[0])

    key = cv2.waitKey(1)
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()