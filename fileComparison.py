import os
import filecmp


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


def compareFiles(listOfFiles):
    copyFiles = list()
    for files in listOfFiles:
        for files2 in listOfFiles:
            if filecmp.cmp(files, files2) and not os.path.samefile(files, files2):
                if files in copyFiles or files2 in copyFiles:
                    continue
                else:
                    print("%s is a copy of %s" % (files, files2))
                    copyFiles.append(files)
