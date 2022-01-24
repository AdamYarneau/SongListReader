import numpy as np
from PIL import ImageGrab
import pytesseract
import time
from datetime import datetime

def main():
    # Generate Text file name
    startString = "C:/Users/yarne/Desktop/RunLogs/"
    startString += datetime.now().strftime("%H-%M-%S")
    startString += ".txt"

    # Create and open file
    fileObj = open(startString,"w")

    runLength = time.time() + 5
    while time.time() < runLength:
        
        # Set the boundaries to capture images
        leftBorder = 1950
        topBorder = 396
        rightBorder = 3300
        height = 70

        preImg = ImageGrab.grab(bbox=(leftBorder, topBorder, rightBorder, topBorder + height),all_screens=False)
        img = np.array(preImg)
        txt = pytesseract.image_to_string(img)
        print(txt)      
        fileObj.write(txt)

    fileObj.close()

if __name__ == '__main__':
    main()