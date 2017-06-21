#! /usr/bin/env python3
# delUnneededFiles - Deletes all files AND folders of certain size in KB

import shutil, os

folder = input("Enter path to the folder: ")
size = int(input("Size in KB: "))

def delUnneededFiles(folder, size):
    filesFound = 0
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            currentFile = os.path.join(foldername, filename)
            if os.path.getsize(currentFile) > size:
                #os.unlink(currentFile)
                #send2trash.send2trash(currentFile)
                print(currentFile)
                filesFound += 1
        if foldername == folder:
            continue
        totalSize = 0 
        for filename in os.listdir(foldername):
            totalSize = totalSize + os.path.getsize(os.path.join(foldername, filename))
        if totalSize > size:
            #os.unlink(foldername)
            #send2trash.send2trash(foldername)
            print(foldername)
            filesFound += 1
    print('Total files and folders found: ' + str(filesFound))

delUnneededFiles(folder, size)
