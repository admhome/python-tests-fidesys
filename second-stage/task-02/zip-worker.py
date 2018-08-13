# -*- coding: UTF-8 -*-
 
import sys
import os
import argparse
import zipfile
import uuid
import json
import csv
import io


ZIP_FILE_NAME = "task2.zip"

csvFiles = {
    'valid': {
        'name': 'guids.csv',
        'data': []
    },
    'invalid': {
        'name': 'others.csv',
        'data': []
    }
}


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i', '--input', help='paste path to input file')
    parser.add_argument ('-o', '--output', help='paste path to output file')
 
    return parser
 
 
if __name__ == '__main__':
    parser = createParser()
    scriptParams = parser.parse_args(sys.argv[1:])

    # формирование имени файла
    if scriptParams.input:
        zipFilename = scriptParams.input

        if zipFilename[-1] != os.sep:
            zipFilename += os.sep

        zipFilename += ZIP_FILE_NAME
    else:
        zipFilename = ZIP_FILE_NAME

    print("Input file: " + zipFilename)

    if zipfile.is_zipfile(zipFilename):
        zip = zipfile.ZipFile(zipFilename, 'r')

        validData = []
        invalidData = []

        for file in zip.namelist():
            zipFile = zip.getinfo(file).filename
            zipDir = os.path.dirname(zipFile)
            print('File: ' + str(zipFile))
            print('Dir: ' + str(zipDir))

            with zip.open(zipFile) as f:
                data = f.read()

            encodedData = json.loads(data.decode("utf-8"))

            print('encodedData: ' + str(encodedData))

            print('')

            try:
                guid = uuid.UUID(str(zipDir))

                csvFiles['valid']['data'].append({
                    'folder': zipDir,
                    'value': encodedData['value'],
                    'str': encodedData['str'],
                })

                print("[VALID]")
            except Exception as e:
                csvFiles['invalid']['data'].append({
                    'folder': zipDir,
                    'value': encodedData['value'],
                    'str': encodedData['str'],
                })

                print("[INVALID]")

            print()

        zip.close()

        csvFiles['valid']['sorted'] = sorted(csvFiles['valid']['data'], key=lambda x: (x['value'], x['str']))
        csvFiles['invalid']['sorted'] = sorted(csvFiles['invalid']['data'], key=lambda x: x['folder'])

        print('validData: ' + str(csvFiles['valid']['data']))
        print('sorted validData: ' + str(csvFiles['valid']['sorted']))
        print()

        print('invalidData: ' + str(csvFiles['invalid']['data']))
        print('sorted invalidData: ' + str(csvFiles['invalid']['sorted']))
        print()

        # create 2 csv
        zip = zipfile.ZipFile(zipFilename, 'a')

        for key, value in csvFiles.items():
            csvData = io.StringIO()
            csvWriter = csv.writer(csvData, delimiter =';')

            # header if needed
            csvWriter.writerow(['folder', 'value', 'str'])

            # print('key: ' + str(key))
            # print('value: ' + str(value))
            for sortedDataItem in value['sorted']:
                csvWriter.writerow(list(sortedDataItem.values()))

            zip.writestr(value['name'], csvData.getvalue())

        #

        zip.close()
    else:
        print("Input file is not correct zip file!")
