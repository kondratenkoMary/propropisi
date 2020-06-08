from core.preprocessing import *
from core.analysis import *

def test_sheet(image):
    processed_contours, res_image = preprocess_image(image)
    mark = analyse(processed_contours, res_image)

    return mark

image = cv2.imread('/Users/andrew/Work/personal/Projects/propropisi/core/test3.jpg')
print(test_sheet(image))
