import cv2 as cv


def process_images(img1, img2):
    thresh = process(img1)
    thresh2 = process(img2)

    contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cnt1 = contours[0]
    contours, hierarchy = cv.findContours(thresh2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cnt2 = contours[0]
    ans = cv.matchShapes(cnt1, cnt2, cv.CONTOURS_MATCH_I3, 0.0)
    ret = 100 - ans * 100

    return ret


def process(img):
    warped = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    gray = cv.bitwise_not(warped)
    ret, bw = cv.threshold(gray, 127, 255, 0)

    return bw


def analyse(res_contours, res):
    #  print sorted
    line_size = 9
    cur_idx = 0
    pattern = None
    mark = 0
    count_of_processed = 0
    single_mark = 0

    for i in range(len(res_contours)):
        c = res_contours[i]
        cur_idx = i % line_size
        is_pattern = cur_idx == 0
        x, y, w, h = cv.boundingRect(c)
        area = w * h
        aspect = (h + 0.0) / w
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.022 * peri, True)

        if (0.9 < aspect) and (aspect < 1.1) and (area > 100) and (len(approx) == 4):
            crop = res[y:y + h, x:x + w]

            if is_pattern:
                pattern = crop

            if not is_pattern:
                count_of_processed += 1
                single_mark = process_images(pattern, crop)
                mark += single_mark
                cv.putText(res, str(round(single_mark, 2)), (x, y), cv.FONT_HERSHEY_SIMPLEX,
                           1, (255, 0, 0), 1, cv.LINE_AA)

            cv.rectangle(res, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return mark / count_of_processed
