import numpy as np
import cv2 as cv
from mss import mss

if __name__ == '__main__':
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

        # cv.imread(hsv, 0)hh

        cv.imshow("frame", frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
