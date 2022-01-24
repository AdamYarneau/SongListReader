import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract
import time
from datetime import datetime

def main():
    runLength = time.time() + 10
    now = datetime.now()
    startString = "C:/Users/yarne/Desktop/RunLogs/"
    midString = now.strftime("%H-%M-%S")
    endString = ".txt"
    startString += midString
    startString += endString
    fileObj = open(startString,"w")

    while time.time() < runLength:
        leftBorder = 1950
        topBorder = 396
        rightBorder = 3300
        height = 70

        preImg = ImageGrab.grab(bbox=(leftBorder, topBorder, rightBorder, topBorder + height),all_screens=False)#.convert("L")
        
        img = np.array(preImg)
        cv2.imshow('window', img)
        txt = pytesseract.image_to_string(img)

        print(txt)      
        fileObj.write(txt)

        if cv2.waitKey(25) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()
            break

    fileObj.close()

if __name__ == '__main__':
    main()