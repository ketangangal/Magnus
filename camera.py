import cv2
import numpy as np
from constants import CAMERA_DEVICE_NUMBER

camera = cv2.VideoCapture(CAMERA_DEVICE_NUMBER)

point_one: list = [182, 400]
point_two: list = [750, 400]
point_three: list = [675, 90]
point_four: list = [285, 90]

thickness: int = 5
color: tuple = (255, 0, 0)
radius: int = 0

initial_coordinates = np.float32([point_four, point_three, point_two, point_one])

converted_point_one = [0, 512]
converted_point_two = [512, 512]
converted_point_three = [512, 0]
converted_point_four = [0, 0]

final_coordinates = np.float32([converted_point_four, converted_point_three, converted_point_two, converted_point_one])

while True:
    check, frame = camera.read()
    frame = cv2.resize(frame, (1024, 512))

    # Draw Points on The image
    frame = cv2.circle(
        img=frame, center=(point_one[0], point_one[1]), radius=radius, color=color,
        thickness=thickness)

    frame = cv2.circle(
        img=frame, center=(point_two[0], point_two[1]), radius=radius, color=color,
        thickness=thickness)

    frame = cv2.circle(
        img=frame, center=(point_three[0], point_three[1]), radius=radius, color=color,
        thickness=thickness)

    frame = cv2.circle(
        img=frame, center=(point_four[0], point_four[1]), radius=radius, color=color,
        thickness=thickness)

    # Exact Chess Boundary
    cv2.line(frame, point_one, point_two, color, thickness)
    cv2.line(frame, point_two, point_three, color, thickness)
    cv2.line(frame, point_three, point_four, color, thickness)
    cv2.line(frame, point_four, point_one, color, thickness)

    matrix = cv2.getPerspectiveTransform(initial_coordinates,
                                         final_coordinates)

    result = cv2.warpPerspective(frame, matrix, (512, 512))

    result = cv2.rotate(result, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('video', frame)
    cv2.imshow('warped', result)

    key = cv2.waitKey(1)
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()
