import cv2


if __name__ == '__main__':
    image = cv2.imread('Board.jpg')

    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(grayScale, 105, 255, 0)
    cannyEdge = cv2.Canny(thresh, 125, 255)

    contours, hierarchy = cv2.findContours(cannyEdge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    image = cv2.resize(image, (500, 500))
    cv2.imshow("Contours", image)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()





