import cv2 as cv
from matplotlib import pylab as plt
def imshow(mat):
    mv = cv.split(mat)
    if len(mv) == 3:
        mv = mv[::-1]
    dst = cv.merge(mv)
    plt.imshow(dst)
    # return dst