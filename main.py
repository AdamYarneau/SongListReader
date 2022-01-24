import numpy as np
from PIL import ImageGrab
import pytesseract
import time
from datetime import datetime
import cv2      #adds preview window
def main():
    # Generate Text file name
    startString = "RunLogs/"
    startString += datetime.now().strftime("%H-%M-%S")
    startString += ".txt"

    # Create and open file
    fileObj = open(startString,"w")
    custom_psm_config = r'--psm 7'
    runLength = time.time() + 10
    while time.time() < runLength:
        
        # Set the boundaries to capture images
        leftBorder = 1950
        topBorder = 396
        rightBorder = 3300
        height = 70

        preImg = ImageGrab.grab(bbox=(leftBorder, topBorder, rightBorder, topBorder + height),all_screens=False)
        img = np.array(preImg)
        cv2.imshow('window', img)       #adds preview window
        txt = pytesseract.image_to_string(img, config=custom_psm_config)
        print(txt)      
        fileObj.write(txt)
        
        #Remove if preview window is not needed
        if cv2.waitKey(25) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()
            break

    fileObj.close()

if __name__ == '__main__':
    main()