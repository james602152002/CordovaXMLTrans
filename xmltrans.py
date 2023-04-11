#! /usr/bin/env python3
import os
import re
import xml.etree.ElementTree as ET

xmlArrs = {"Saury.xml",
           "Saury(en).xml",
           "Saury-ja-JP.xml",
           "Saury-ko-KR.xml",
           "Saury(zh)-zh-CN.xml",
           "Saury-zh-CN.xml",
           "Saury-zh-Hant.xml",
           "Saury-ar.xml",
           "Saury-de.xml",
           "Saury-es.xml",
           "Saury-fr.xml",
           "Saury-hi.xml",
           "Saury-ru.xml"}

docDirectory = os.getenv("HOME")+"/Documents/"
print(docDirectory)

def folderNameSwitcher(arg):
    switcher={
            "Saury.xml":"values",
            "Saury(en).xml":"values-en",
            "Saury-ja-JP.xml":"values-ja-rJP",
            "Saury-ko-KR.xml":"values-ko-rKR",
            "Saury(zh)-zh-CN.xml":"values-zh",
            "Saury-zh-CN.xml":"values-zh-rCN",
            "Saury-zh-Hant.xml":"values-zh-rTW",
            "Saury-ar.xml":"values-ar",
            "Saury-de.xml":"values-de",
            "Saury-es.xml":"values-es",
            "Saury-fr.xml":"values-fr",
            "Saury-hi.xml":"values-hi",
            "Saury-ru.xml":"values-ru"
            }
    return switcher.get(arg,"values")

def parseXML(fileName):
    content = "const language = {\n"
    tree = ET.parse(docDirectory+"localization/"+fileName)
    root = tree.getroot()
    for text in root.findall('./texts/text'):
        key = text.get('name')
        value = text.get('value').replace("'","\"")
        content += "  "
        content += "'" + key + "': '"
        content += value
        content += "',\n"
    content += "}\n\nexport default language"
    return content

def writeFile(fileName,folderName):
    nameRegex = re.sub('\(.*\)',"",fileName)
    #文件路径
    destFilePath = docDirectory
    #创建文件夹
    if not os.path.exists(destFilePath):
        os.makedirs(destFilePath)
    #编写xml内容
    xmlBuilder = parseXML(nameRegex)
    textFile = open(docDirectory+"/"+folderName+".js","w")
    textFile.write(xmlBuilder)
    textFile.close()
    return

for name in xmlArrs:
    writeFile(name,folderNameSwitcher(name).replace("values","language"))
