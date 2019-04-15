import cv2


if __name__ == '__main__':
    image = cv2.imread('Board.jpg')

    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayScale = cv2.resize(grayScale, (500, 500))
    cv2.imshow("Gray Scale", grayScale)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('n'):
        cv2.destroyAllWindows()

    _, thresh = cv2.threshold(grayScale, 105, 255, 0)
    thresh = cv2.resize(thresh, (500, 500))
    cv2.imshow("Threshold", thresh)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('n'):
        cv2.destroyAllWindows()

    cannyEdge = cv2.Canny(thresh, 125, 255)
    cannyEdge = cv2.resize(cannyEdge, (500, 500))
    cv2.imshow("Canny Edge", cannyEdge)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('n'):
        cv2.destroyAllWindows()


