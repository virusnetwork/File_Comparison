#! python3
# fileComparison.py - compares all files in a directory and all files in sub-directorys
# and identify duplicate files
import os
import filecmp

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

# Ask user for folder location


def getFolderLocation():
    while True:

        print("Please enter folder location")
        location = input()

        if os.path.exists(location):
            compareFiles(getListOfFiles(location))
        else:
            print("location given is not a folder location")
            answer = input("Would you like to give another location: ")
            if answer.lower.startswith('n'):
                exit()

# TODO: ask user if they want to delete files

# TODO: Make main method
