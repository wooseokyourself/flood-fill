import sys
import numpy as np
import cv2 as cv

def reddot (img, x, y, color):
    img = cv.circle(img, (x, y), 30, color, -1)
    return img

if __name__ == '__main__':
    inp, outp = sys.argv[1], sys.argv[2]
    x, y = int(sys.argv[3]), int(sys.argv[4])
    img = cv.imread(inp)
    if img is None:
        print(" flood-fill.py error: Image input failed")
        sys.exit(1)
    if y < 0 or y > img.shape[0] or x < 0 or x > img.shape[1]:
        print(" flood-fill.py error: x or y out of image range")
        sys.exit(1)
    bgrColor = (0, 0, 255)
    reddot(img, x, y, bgrColor)
    if cv.imwrite(outp, img) == False:
        print(" flood-fill.py error: Image output failed")
        sys.exit(1)
    sys.exit(0)