import cv2
import numpy as np


if __name__ == "__main__":

    image = cv2.imread('Board.jpg')

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # defining the Range of blue color
    blueLowerBound = np.array([99, 115, 150], np.uint8)
    blueUpperBound = np.array([110, 255, 255], np.uint8)

    # defining the Range of yellow color
    yellowLowerBound = np.array([20, 190, 20], np.uint8)
    yellowUpperBound = np.array([30, 255, 255], np.uint8)

    # finding the range of blue and yellow color in the image
    blue = cv2.inRange(hsv, blueLowerBound, blueUpperBound)
    yellow = cv2.inRange(hsv, yellowLowerBound, yellowUpperBound)

    # Morphological transformation, Dilation
    kernal = np.ones((5, 5), "uint8")

    blue = cv2.dilate(blue, kernal)
    res1 = cv2.bitwise_and(image, image, mask=blue)

    yellow = cv2.dilate(yellow, kernal)
    res2 = cv2.bitwise_and(image, image, mask=yellow)

    # Tracking the Blue Color
    contours, hierarchy = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            ar = w / float(h)
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(image, "blue color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

    # Tracking the yellow Color
    contours, hierarchy = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            ar = w / float(h)
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(image, "yellow  color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255))

    # Show the Color Detection
    image = cv2.resize(image, (500, 500))
    cv2.imshow("Color Detection", image)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()
