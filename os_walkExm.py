""" this will program demostarates the os.walk() function
it will run through all the folders, subfolders and files in a given directory"""
import os
for folderName, subfolders, filenames in os.walk('C:\\exampleFolder'):
    print('The current folder is ' + folderName)    #os.walk() will return lists of the folders,subfolders and files on which the for loop will itterate
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
print('')
