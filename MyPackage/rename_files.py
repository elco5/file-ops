from fileinput import filename
import os
import shutil
import MyFunctions


os.chdir(r"C:\Users\count\dev\FILE-OPS\newFileFolder") # r = raw string
print(os.getcwd())
fileList = MyFunctions.listFiles(os.getcwd()); print(fileList)


print(end='\n')

# make folder for renamed files if dosent exist yet
renumberedDirectory = os.path.join(os.getcwd(),'renumbered')
if(os.path.exists(renumberedDirectory) == False):
    os.mkdir(renumberedDirectory)

# make original and new number lists
originialFileNumbers = []
for count, i in enumerate(range(95,106)):
    originialFileNumbers.append('_' + str(i))
print(originialFileNumbers)

newFileNumbers = []
for count, i in enumerate(range(105,94,-1)):
    newFileNumbers.append('_' + str(i))
print(newFileNumbers)



#for oldNumber in originialFileNumbers:
for oldNumber in originialFileNumbers:

    for fileName in fileList:

    
        f_name, f_ext = os.path.splitext(fileName)
        
        # if name contains original number
        
        if f_name.__contains__(oldNumber):
            # replace with new number at index of old number

            new_f_name = f_name.replace(oldNumber, 
                newFileNumbers[originialFileNumbers.index(oldNumber)])
            
            newFileName = os.path.join(renumberedDirectory, new_f_name + f_ext) 
            
            shutil.copy(fileName, newFileName)
            
            f = open(newFileName, "w")
            f.write( fileName + " changed to: " + os.path.basename(newFileName))
            f.close()

            print(f_name + " changed to " + new_f_name)    
            
         
