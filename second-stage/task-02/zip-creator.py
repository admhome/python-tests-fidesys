# -*- coding: UTF-8 -*-
 
import sys
import os
import argparse
import zipfile


ZIP_OTPUT_FILE_NAME = "task2.zip"


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-o', '--output', help='paste path to output file')
 
    return parser
 
 
if __name__ == '__main__':
    parser = createParser()
    scriptParams = parser.parse_args(sys.argv[1:])

    # формирование имени выходного файла
    if scriptParams.output:
        outputFilename = scriptParams.output

        if outputFilename[-1] != os.sep:
            outputFilename += os.sep

        outputFilename += ZIP_OTPUT_FILE_NAME
    else:
        outputFilename = ZIP_OTPUT_FILE_NAME

    print("Output file: " + outputFilename)