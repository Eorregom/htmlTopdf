import pdfkit
import re
import os
from os import listdir
from os.path import isfile, join

mypath = input("Enter the path of the files to convert\n") 
output_path = input("Enter the output path\n") 

files = os.listdir(mypath)
print(files)

options = {
  "enable-local-file-access": None,
  "load-media-error-handling": 'ignore',
  'load-error-handling': 'ignore'
}



perreo

for item in files:
    path = mypath +"\\"+ item 
    name = os.listdir(path)
    for html in name:
        if '.html' in html:
            file_path = path + "\\" + html
            output = output_path + "\\" +item + ".pdf"
            pdfkit.from_file(file_path,output,options=options,)



