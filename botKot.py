import cv2
from mss import mss
import numpy as np
import time

width = 450
height = width
scr = {'top': 320, 'left': 390, 'width': width, 'height': height}

k = 30
sct = mss()


def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def foo():
    r = []
    for top in range(0, int(width/k)):
        r.append([])
        for left in range(0, int(width/k)):
            sct_img = sct.grab({'top': scr['top']+top*k, 'left': scr['left']+left*k, 'width': k, 'height': k})
            frame = np.array(sct_img)
            processed_image = process_image(frame)
            mean = np.mean(processed_image)
            r[top].append([])
            r[top][left] = mean
    print('r = ', r)


def goo(img):
    hsv_min = np.array((0, 54, 5), np.uint8)
    hsv_max = np.array((187, 255, 253), np.uint8)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    contours0, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv2.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        cv2.drawContours(img, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник

    # cv2.imshow('contours', img)  # вывод обработанного кадра в окно


def main():
    last_time = time.time()
    while True:

        sct_img = sct.grab(scr)

        frame = np.array(sct_img)

        processed_image = process_image(frame)
        mean = np.mean(processed_image)
        print('mean = ', mean)
        # foo()
        goo(frame)
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        for i in range(0, 15):
            cv2.line(img=frame, pt1=(0, i*k), pt2=(width, i*k), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
            cv2.line(img=frame, pt1=(i*k, height), pt2=(i*k, 0), color=(255, 0, 0), thickness=1, lineType=8, shift=0)

        cv2.imshow("frame", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    main()
