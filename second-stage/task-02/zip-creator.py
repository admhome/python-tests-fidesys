# -*- coding: UTF-8 -*-
 
import sys
import os
import argparse
import zipfile
import uuid
import json


ZIP_OTPUT_FILE_NAME = "task2.zip"
JSON_FILE_NAME = "data.json"


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='paste path to input dir')
    parser.add_argument('-o', '--output', help='paste path to output file')

    return parser


if __name__ == '__main__':
    parser = createParser()
    scriptParams = parser.parse_args(sys.argv[1:])

    # формирование имени входного каталога
    if scriptParams.input:
        inputFilename = scriptParams.input

        if inputFilename[-1] != os.sep:
            inputFilename += os.sep

    else:
        inputFilename = ""

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

    for iter in range(15):
        if (iter < 10):
            # with GUID
            dirSuffix = str(uuid.uuid4())
        else:
            # without GUID
            dirSuffix = 'dir-name-' + ('%03d' % iter)

        iterDir = inputFilename + dirSuffix

        # safely create dir
        if not os.path.exists(iterDir):
            os.makedirs(iterDir)

            print('Folder created')

            JSONdata = {
                'value': iter,
                'str': dirSuffix
            }

            # write json-files
            with open(iterDir + os.sep + JSON_FILE_NAME, 'w') as JSONfile:
                json.dump(JSONdata, JSONfile)

        print('iter: ' + str(iter) + ', iterDir: ' + iterDir)

    # zip it
    ZIPfile = zipfile.ZipFile(outputFilename, 'w')

    for root, dirs, files in os.walk(inputFilename):
        for file in files:
            realPath = os.path.join(root, file)
            fakePath = (os.sep).join(realPath.split(os.sep)[-2:])

            ZIPfile.write(realPath, fakePath)

    ZIPfile.close()

    print("zip file must be created")
