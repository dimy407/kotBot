import numpy as np
import cv2 as cv
from mss import mss


def nothing(x):
    pass


cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)

cv.setTrackbarPos("LH", "Tracking", 110)
cv.setTrackbarPos("LS", "Tracking", 110)
cv.setTrackbarPos("LV", "Tracking", 100)

w1 = 1205
h1 = 850
top = 40
left = 5
wid = w1 - left
hei = h1 - top

bbox = {'top': top, 'left': left, 'width': wid, 'height': hei}
sct = mss()

while 1:
    sct_img = sct.grab(bbox)
    frame = np.array(sct_img)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("LH", "Tracking")
    l_s = cv.getTrackbarPos("LS", "Tracking")
    l_v = cv.getTrackbarPos("LV", "Tracking")

    u_h = cv.getTrackbarPos("UH", "Tracking")
    u_s = cv.getTrackbarPos("US", "Tracking")
    u_v = cv.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, l_b, u_b)
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)

    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
