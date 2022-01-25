from fileinput import filename
import os
import shutil
import MyFunctions

targetPath = input('Input target directory: ')
os.chdir(targetPath)
# os.chdir(r"C:\Users\count\dev\file-ops\originalFiles") # r = raw string
print("targeting directory: " + os.getcwd())
fileList = MyFunctions.listFiles(os.getcwd()); 
print("target directory contents: ")
print(fileList)


print(end='\n')

# make folder for renamed files if dosent exist yet
renumberedDirectory = os.path.join(os.getcwd(),'renumbered')
if(os.path.exists(renumberedDirectory) == False):
    os.mkdir(renumberedDirectory)

# make original and new number lists
originialFileNumbers = []
for count, i in enumerate(range(95,106)):
    originialFileNumbers.append('_' + str(i))
#print(originialFileNumbers)

newFileNumbers = []
for count, i in enumerate(range(105,94,-1)):
    newFileNumbers.append('_' + str(i))
#print(newFileNumbers)


changeCount = 0
for oldNumber in originialFileNumbers:

    for fileName in fileList:
    
        f_name, f_ext = os.path.splitext(fileName)
        
        if f_name.__contains__(oldNumber):
            
            # replace with new number at index of old number
            new_f_name = f_name.replace(oldNumber, 
                newFileNumbers[originialFileNumbers.index(oldNumber)])
            # compose new file name
            newFileName = os.path.join(renumberedDirectory, new_f_name + f_ext) 
            # make a copy of old file with new name
            shutil.copy(fileName, newFileName)
            changeCount = changeCount + 1
            
            # f = open(newFileName, "w")
            # f.write( fileName + " changed to: " + os.path.basename(newFileName))
            # f.close()

            print(f_name + " changed to " + new_f_name)    
            
print( "Renamed " + str(changeCount) + " files.")         
