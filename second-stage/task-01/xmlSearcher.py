# -*- coding: UTF-8 -*-

# К элементам иногда добавляются Атрибуты. Атрибуты состоят из пары имя-значение, где значение берется в двойные кавычки ("),
# вот так: type="dessert". Атрибуты позволяют сохранять вместе с элементом дополнительные параметры, меняя значения этих
# параметров от элемента к элементу в одном и том же документе.

import sys
import argparse
import xml.etree.ElementTree as ET
import os

neededSumm = 0;
neededCount = 0;

# def createParser():
#     parser = argparse.ArgumentParser(prog='XML Searcher')
#     parser.add_argument('-f', '--file', '--xml-file', type=argparse.FileType('r'))
#
#     return parser


def findInXML(data):
    summ = 0
    count = 0
    searchRes = data.findall(".//*[@value2]")

    for searchItem in searchRes:
        summ += int(searchItem.attrib['value2'])
        count += 1

    return {
        "summ": summ,
        "count": count
    }


if __name__ == '__main__':
    # parser = createParser()
    # xmlFile = parser.parse_args(sys.argv[1:])
    # fileContent = xmlFile.file.read()
    # xmlRoot = ET.fromstring(fileContent)

    xmlFile = sys.argv[1]
    xmlRoot = ET.parse(xmlFile).getroot()

    avgData = findInXML(xmlRoot)

    print('avegRes: ' + str(avgData["summ"] / avgData["count"]))
