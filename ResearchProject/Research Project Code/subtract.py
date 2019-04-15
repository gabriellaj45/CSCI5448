import cv2


if __name__ == '__main__':
    # Read in past image
    oldImage = cv2.imread("0.jpg")
    oldImage = cv2.resize(oldImage, (500, 500))
    cv2.imshow("First Image", oldImage)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('n'):
        cv2.destroyAllWindows()

    # Read in new image
    newImage = cv2.imread("1.jpg")
    newImage = cv2.resize(newImage, (500, 500))
    cv2.imshow("Second Image", newImage)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('n'):
        cv2.destroyAllWindows()

    # Computer difference of images
    imageDiff = cv2.subtract(oldImage, newImage)

    # Find contours
    grayImage = cv2.cvtColor(imageDiff, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grayImage, 50, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours (differences)
    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        x, y = (int(x), int(y))
        center = x, y
        radius = int(radius)
        if radius > 7:
            cv2.circle(newImage, center, radius, (255, 255, 255), 1)

    # Show the difference
    newImage = cv2.resize(newImage, (500, 500))
    cv2.imshow("Image Difference", newImage)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('n'):
        cv2.destroyAllWindows()
