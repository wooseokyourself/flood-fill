import sys
import argparse
import numpy as np
import cv2 as cv

def floodFill (img, x, y, color):
    rows, cols = img.shape[:2]
    mask = np.zeros((rows + 2, cols + 2), np.uint8)
    loDiff, upDiff = (35, 35, 35), (35, 35, 35)
    cv.floodFill(img, mask, (x, y), color, loDiff, upDiff)
    return img

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="fill flood")
    parser.add_argument("--io", nargs=2, type=str, help="inputfile, outputfile", required=True)
    parser.add_argument("--location", nargs=2, type=int, help="an integer for (x,y)", required=True)
    parser.add_argument("--rgb", nargs=3, type=int, help="(optional) color=(r,g,b), default=(255,0,0)")
    args = parser.parse_args()

    inp, outp = args.io[0], args.io[1]
    x, y = args.location[0], args.location[1]
    img = cv.imread(inp)
    if img is None:
        print(" flood-fill.py error: Image input failed")
        sys.exit(1)
    if y < 0 or y > img.shape[0] or x < 0 or x > img.shape[1]:
        print(" flood-fill.py error: x or y out of image range")
        sys.exit(1)
    bgrColor = (0, 0, 255)
    if args.rgb is not None:
        bgrColor = (args.rgb[2], args.rgb[1], args.rgb[0])
        if 0 > bgrColor[0] or 255 < bgrColor[0] or 0 > bgrColor[1] or 255 < bgrColor[1] or 0 > bgrColor[2] or 255 < bgrColor[2]:
            print(" flood-fill.py error: Invalid RGB value")
            sys.exit(1)
    floodFill(img, x, y, bgrColor)
    if cv.imwrite(outp, img) == False:
        print(" flood-fill.py error: Image output failed")
        sys.exit(1)
    sys.exit(0)