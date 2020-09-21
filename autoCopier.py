# autoCopier.py

# for coping records from the drive to the nas

import os, shutil, time
import datetime
from os import path

#add the path of the foler that will be created in
path = '/Users/nathanielchang/Documents/'

#add the path of which the files come from
src_dir = '/Users/nathanielchang/Documents/testFolder'

#getting the date and time
now = datetime.datetime.now()

# if the drive is pluged in before 1400hrs service is AM if not service is PM
if now.strftime("%H") < 14: 
    service = "AM" 
else: 
    service = "PM"

# logging the name of the folder that will be created
# print(now.strftime("%Y%m%d-%A-%H%M"+service))

#creating the folder
def crtFolder():
    folder = path+time.strftime("%Y%m%d-%A-"+service)
    if os.path.exists(folder):
        dest = path+time.strftime("%Y%m%d-%A-"+service)
    else:
        os.mkdir(path+time.strftime("%Y%m%d-%A-"+service))
        dest = path+time.strftime("%Y%m%d-%A-"+service)

def copy():
    crtFolder()
    src = src_dir
    dest = path+time.strftime("%Y%m%d-%A-"+service)
    for root, dirnames, filenames in os.walk(src):
        for file in filenames:
            (shortname, extension) = os.path.splitext(file)
            if extension == ".txt" :
                shutil.copy2(os.path.join(root,file), os.path.join(dest,   
                             os.path.relpath(os.path.join(root,file),src)))
    time.sleep(2)

if __name__ =="__main__":
    var1 = True
    while var1 == True:
        copy()