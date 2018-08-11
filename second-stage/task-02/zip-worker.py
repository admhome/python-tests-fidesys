# -*- coding: UTF-8 -*-
 
import sys
import os
import argparse
import zipfile


ZIP_INPUT_FILE_NAME = "task2.zip"
ZIP_OTPUT_FILE_NAME = "task2_.zip"


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i', '--input', help='paste path to input file')
    parser.add_argument ('-o', '--output', help='paste path to output file')
 
    return parser
 
 
if __name__ == '__main__':
    parser = createParser()
    scriptParams = parser.parse_args(sys.argv[1:])

    # формирование имени входного файла
    if scriptParams.input:
        inputFilename = scriptParams.input

        if inputFilename[-1] != os.sep:
            inputFilename += os.sep

        inputFilename += ZIP_INPUT_FILE_NAME
    else:
        inputFilename = ZIP_INPUT_FILE_NAME

    # формирование имени выходного файла
    if scriptParams.output:
        outputFilename = scriptParams.output

        if outputFilename[-1] != os.sep:
            outputFilename += os.sep

        outputFilename += ZIP_OTPUT_FILE_NAME
    else:
        outputFilename = ZIP_OTPUT_FILE_NAME

    print("Input file: " + inputFilename)
    print("Output file: " + outputFilename)