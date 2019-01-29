#! python3
#script for converting file into ZIP file
import os , zipfile
# type folder path where your zip file is kept
os.chdir('C:\Users\LEGEND\Desktop')
#type the file name you want for ZIP file
newZipFile=zipfile.ZipFile('neww.zip', 'w')
#type file name you want to convert into ZIP file
newZipFile.write('ZOO.txt', compress_type=zipfile.ZIP_DEFLATED)
newZipFile.close()
#it will save new zip file in same folder  
