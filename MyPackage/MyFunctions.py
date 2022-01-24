import os

#list all files in directory: "path"
def listFiles(path):
    listDirectory = os.listdir(path)
    listFiles = []
    for element in listDirectory:
        if(os.path.isfile(element)):
            listFiles.append(element)
    return listFiles

