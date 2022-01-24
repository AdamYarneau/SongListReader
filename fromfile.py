import numpy as np
from PIL import Image
# import cv2
import pytesseract
from datetime import datetime

def main():
    startString = "RunLogs/"
    startString += datetime.now().strftime("%H-%M-%S")
    startString += ".txt"
    fileObj = open(startString,"w")
    listOfFiles = ["WordPics/1.PNG","WordPics/2.PNG","WordPics/3.PNG","WordPics/4.PNG","WordPics/5.PNG","WordPics/6.PNG","WordPics/7.PNG","WordPics/8.PNG","WordPics/9.PNG","WordPics/current.PNG","WordPics/Capture.PNG"]
    custom_psm_config = r'--psm 7'
    for x in range(len(listOfFiles)):
        preImg = Image.open(listOfFiles[x])
        img = np.array(preImg)
        # cv2.imshow('window', img)
        txt = pytesseract.image_to_string(img, config=custom_psm_config)
        # print(txt)      
        fileObj.write(txt)
    fileObj.close()
if __name__ == '__main__':
    main()