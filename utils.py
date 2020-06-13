import cv2 as cv
from matplotlib import pylab as plt
def imshow(mat):
    mv = cv.split(mat)
    if len(mv) == 3:
        b, g, r = mv
        mv = [r, g, b]
        dst = cv.merge(mv)
    else:
        dst = cv.merge(mv)
    plt.imshow(dst)
    # return dst