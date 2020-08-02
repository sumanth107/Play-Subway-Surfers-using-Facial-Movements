#@uthor : Sumanth Nethi

import cv2 as cv
from pynput.keyboard import Key, Controller

capture = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
keyboard = Controller()
lr_limit = 0
ud_limit = 0


def lr_controller(x1, y1):
    if x1 < 280:  # left
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    if x1 > 360:  # right
        keyboard.press(Key.left)
        keyboard.release(Key.left)


def ud_controller(x1, y1):
    if y1 < 200:  # up
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    if y1 > 280:  # down
        keyboard.press(Key.down)
        keyboard.release(Key.down)


while True:
    ret, frame = capture.read()
    frame = cv.resize(frame, (640, 480))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    xc = 320
    yc = 240
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        xc, yc = (x + int(w * 0.5)), (y + int(h * 0.5))
        cv.circle(frame, (xc, yc), 5, (0, 0, 255), -1)
    cv.rectangle(frame, (280, 200), (360, 280), (0, 255, 0), 2)
    if lr_limit == 0:
        lr_controller(xc, yc)
        lr_limit += 1
    if 280 < xc < 360:
        lr_limit = 0
    if ud_limit == 0:
        ud_controller(xc, yc)
        ud_limit += 1
    if (yc > 200) and (yc < 280):
        ud_limit = 0
    cv.imshow('Frame', frame)
    if cv.waitKey(1) & 0xFF == 27:
        break
capture.release()
cv.destroyAllWindows()
