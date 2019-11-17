import os
import sys


def checkExistsFiles(fileName):
    return os.path.exists(fileName)


if __name__ == '__main__':
    fileName = sys.argv[1]
    print("File: ", fileName, " exists: ", checkExistsFiles(fileName))
