#! python3
# fileComparison.py - compares all files in a directory and all files in sub-directorys
# and identify duplicate files
import os
import filecmp
import send2trash


# Ask user for folder location
def getFolderLocation():
    a = True
    hold = list()
    while a:
        location = input("Please enter folder location: ")

        if os.path.exists(location):
            hold = compareFiles(getListOfFiles(location))
        else:
            print("location given is not a folder location")

        answer = input("Would you like to give another location: ")
        if answer.lower().startswith('n'):
            a = False
    return hold


# returns a list of all files in directory and sub-directorys
# takes directory location as parameter
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


# compares all files in given list of files
def compareFiles(listOfFiles):
    # list of all duplicate files
    duplicateFilesList = list()
    # loops all files in listOfFiles twice as we compare each of them
    for files in listOfFiles:
        for files2 in listOfFiles:
            # if a duplicate is found and its not all ready in the same file list
            # it adds to the duplicate list
            if filecmp.cmp(files, files2) and not os.path.samefile(files, files2):
                if files in duplicateFilesList or files2 in duplicateFilesList:
                    continue
                else:
                    print("%s is a copy of %s" % (files, files2))
                    duplicateFilesList.append(files)
    if len(duplicateFilesList) == 0:
        print("no duplicates found")
        return list()
    else:
        return duplicateFilesList


# ask user what to do with files
def whatToDoWithFiles(listOfFiles):
    x = input("Would you like delete files or nothing:  ")
    # move to trash
    if x.lower().startswith('d'):
        for file in listOfFiles:
            send2trash.send2trash(file)
    # does nothing with files
    else:
        print('files have been left untoachted')
        exit()


# Make main method
def main():
    whatToDoWithFiles(getFolderLocation())
