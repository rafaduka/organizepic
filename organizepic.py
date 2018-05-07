#!/usr/bin/env python
import os
import sys
import hashlib
import time
from datetime import date, datetime
import shutil

def displayFiles(arg):
    filelist = os.listdir(arg)
    for item in filelist:
        path = os.path.join(arg, item)
        if os.path.isdir(path):
            displayFiles(path)
        else:
            filename, file_extension = os.path.splitext(path)
            if file_extension != "":
                tm = time.localtime(os.stat(path).st_birthtime)
                dt = datetime(tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec)
                formatted = dt.strftime("%d-%m-%Y_%H_%M_%S" + "_" + md5(path) + file_extension)
                directory = dt.strftime("%m%Y")
                if not os.path.exists(directory):
                    os.makedirs(directory)

                renamed = os.path.dirname(path) + "/"+ formatted
            
                if (anyOneThere(sys.argv[1], md5(path)) == 'false'):
                    shutil.copy2(path, "/Users/rxhoracio/Desktop/" + directory + "/" + formatted)
                    print("copied -> " +"\n"+
                    "from -> " +path + " md5 -> " +md5(path) + "\n"+
                    "to ->/Users/rxhoracio/Desktop/" + directory + "/" + formatted) 


def md5(file):
    f = open(file, 'rb')
    sum = hashlib.md5(f.read()).hexdigest()
    f.close()
    return sum


def anyOneThere(arg, md5arg):
    filelist = os.listdir(arg)
    count = 0;
    for item in filelist:
        path = os.path.join(arg, item)
        if os.path.isdir(path):
            anyOneThere(path, md5arg)
        else:
            if md5(path) == md5arg:
                count += 1

    return 'true' if count > 0 else 'false'            


displayFiles(sys.argv[1])