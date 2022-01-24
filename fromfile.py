import numpy as np
from PIL import Image
import cv2
import pytesseract
from datetime import datetime

def main():
    now = datetime.now()
    startString = "C:/Users/yarne/Desktop/RunLogs/"
    midString = now.strftime("%H-%M-%S")
    endString = ".txt"
    startString += midString
    startString += endString
    fileObj = open(startString,"w")
    listOfFiles = ["C:/Users/yarne/Desktop/WordPics/1.PNG","C:/Users/yarne/Desktop/WordPics/2.PNG","C:/Users/yarne/Desktop/WordPics/3.PNG","C:/Users/yarne/Desktop/WordPics/4.PNG","C:/Users/yarne/Desktop/WordPics/5.PNG","C:/Users/yarne/Desktop/WordPics/6.PNG","C:/Users/yarne/Desktop/WordPics/7.PNG","C:/Users/yarne/Desktop/WordPics/8.PNG","C:/Users/yarne/Desktop/WordPics/9.PNG","C:/Users/yarne/Desktop/WordPics/current.PNG","C:/Users/yarne/Desktop/WordPics/Capture.PNG"]

    for x in range(len(listOfFiles)):
        preImg = Image.open(listOfFiles[x])
        img = np.array(preImg)
        # cv2.imshow('window', img)
        txt = pytesseract.image_to_string(img)
        # print(txt)      
        fileObj.write(txt)
    fileObj.close()
if __name__ == '__main__':
    main()