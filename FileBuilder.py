#/
# make file

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())


# with open('new.txt') as text_file, open('xyz.txt', 'w') as myfile:  
#     for line in text_file:
#         var1, var2 = line.split(",")
#         myfile.write(var1+'\n')

import os
if (os.path.isdir("newFileFolder") == False):
    os.mkdir("newFileFolder")

for i in range(95,106):
    f = open("newFileFolder/myFile_" + str(i) + ".txt" , "w")
    f.write("this is file number " + str(i))