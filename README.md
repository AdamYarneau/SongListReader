# SongListReader
A python based Optical Character Recognition (OCR) program that grabs the artist and song names from a YouTube video using Tesseract OCR and writes the data to an auto generated text file. 

The current boundary box settings for main.py are configured to fit this video when played in theater mode. But the bounds can easily be adjusted for a different video.

https://www.youtube.com/watch?v=DWcJFNfaw9c

You can also run fromfile.py to preform OCR on a set of test images found in the WordPics directory.

Both scripts will make a text file named for the time the script was ran, and save it into the RunLogs directory.
