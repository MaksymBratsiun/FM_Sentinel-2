import cv2

# Change PATH_1, PATH_2, MATCHES according your purpose
PATH_1 = "test_data/S2A_MSIL1C_20180611T083601_N0206_R064_T36UYA_20180611T104008.SAFE/GRANULE/L1C_T36UYA_A015505_\
20180611T084243/IMG_DATA/T36UYA_20180611T083601_B8A.jp2"
PATH_2 = "test_data/S2A_MSIL1C_20180611T083601_N0206_R064_T37UCR_20180611T104008.SAFE/GRANULE/L1C_T37UCR_A015505_\
20180611T084243/IMG_DATA/T37UCR_20180611T083601_B8A.jp2"
MATCHES = 20

if __name__ == '__main__':
    img1 = cv2.imread(PATH_1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(PATH_2, cv2.IMREAD_GRAYSCALE)

    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    matches = sorted(matches, key=lambda x: x[0].distance)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:MATCHES], None, flags=2)

    for match in good[:MATCHES]:
        m = match[0]
        pt1 = (int(kp1[m.queryIdx].pt[0]), int(kp1[m.queryIdx].pt[1]))
        pt2 = (int(kp2[m.trainIdx].pt[0] + img1.shape[1]), int(kp2[m.trainIdx].pt[1]))
        img3 = cv2.line(img3, pt1, pt2, (0, 255, 0), 2)
    cv2.imwrite('output_image.jpg', img3)
