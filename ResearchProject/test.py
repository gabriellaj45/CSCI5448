import cv2

if __name__ == '__main__':
    image = cv2.imread("0.jpg")
    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("NewBoard.jpg", grayScale)