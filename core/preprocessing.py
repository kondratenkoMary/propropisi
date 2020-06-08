from imutils.perspective import four_point_transform
from skimage.filters import threshold_local
import imutils
import numpy as np
import cv2
import core.analysis as analysis


def show_image(image, caption='image'):
    # cv2.imshow(caption, imutils.resize(image, height=1000))
    # cv2.waitKey(0)
    print('')

#     sorting contours func
def get_contour_precedence(contour, cols):
    tolerance_factor = 10
    origin = cv2.boundingRect(contour)
    return ((origin[1] // tolerance_factor) * tolerance_factor) * cols + origin[0]


def preprocess_image(image):
    # load the image and compute the ratio of the old height
    # to the new height, clone it, and resize it
    ratio = image.shape[0] / 1600
    orig = image.copy()
    image = imutils.resize(image, height=1600)
    show_image(image)

    image_height, image_width, image_channels = image.shape
    # convert the image to grayscale, blur it, and find edges
    # in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)

    show_image(edged)

    # Find contours

    # find the contours in the edged image, keeping only the
    # largest ones, and initialize the screen contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    XY = []
    # cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    # print(cnts)

    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        area = w * h
        aspect = (h + 0.0) / w
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.022 * peri, True)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        text = str(x) + '-' + str(y) + '-' + str(w) + '-' + str(h)

        xpr = x
        ypr = y  # debug
        if x < image_width / 2:
            x += w

        if y < image_height / 2:
            y += h

        cv2.putText(image, text, (xpr, ypr), cv2.FONT_HERSHEY_SIMPLEX,
                    0.3, (255, 0, 0), 1, cv2.LINE_AA)
        if (0.9 < aspect) and (aspect < 1.1) and (area > 100) and (area < 1200) and (len(approx) == 4):
            xy = np.array([x, y])
            XY.append(xy)
            cv2.rectangle(image, (xpr, ypr), (xpr + w, ypr + h), (0, 0, 255), 3)
    # cv2.drawContours(orig, cnts, -1, (0, 0, 255), 1)

    show_image(image)

    XY = np.array(XY)
    # loop over the contours

    #  Transform and scale

    # apply the four point transform to obtain a top-down
    # view of the original image
    warped = four_point_transform(orig, XY.reshape(4, 2) * ratio)
    show_image(warped)

    # convert the warped image to grayscale, then threshold it
    # to give it that 'black and white' paper effect
    orig = np.copy(warped)
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped, 11, offset=10, method="gaussian")
    # warped = (warped > T).astype("uint8") * 255

    # show the original and scanned images

    gray = cv2.bitwise_not(warped)
    bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)

    # Show extracted horizontal lines
    # [horiz]

    show_image(gray)

    cnts = cv2.findContours(bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    res = cv2.cvtColor(warped, cv2.COLOR_GRAY2RGB)

    res_contours = []
    for i in range(len(cnts)):
        c = cnts[i]
        x, y, w, h = cv2.boundingRect(c)
        area = w * h
        aspect = (h + 0.0) / w
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.022 * peri, True)

        if (0.9 < aspect) and (aspect < 1.1) and (area > 100) and (len(approx) == 4):
            crop = res[y:y + h, x:x + w]
            res_contours.append(approx)

    # sort contours
    res_contours.sort(key=lambda ww: get_contour_precedence(ww, bw.shape[1]))

    return res_contours, res

