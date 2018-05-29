"""
os
"""

import os
import pprint as pp

print("__file__: ", __file__) 
print("basename: ", os.path.basename(__file__))
print("dirname: ", os.path.dirname(__file__))
print("realpath: ", os.path.realpath(__file__))
print("relpath: ", os.path.relpath(__file__))
print("split: ", os.path.split(__file__))

tempfolder = "_temp"

print("isdir: ", os.path.isdir(tempfolder))
print("isfile: ", os.path.isfile(tempfolder))
print("join: ", os.path.join(tempfolder, "_Temp"))

if not os.path.exists(tempfolder):
    os.mkdir(tempfolder) # Creates
    os.rmdir(tempfolder) # Removes

print()
file1 = os.path.join(tempfolder, "log.log")
file2 = os.path.join(tempfolder, "log.bak")

if os.path.isfile(file1) and not os.path.isfile(file2):
    os.rename(file1, file2)
    #os.remove(file2)

print()
print(os.getcwd()) # Get current folder
os.chdir("c:\\")
print(os.getcwd()) # Get current folder

print()
print(os.name)
print(os.sep)

#os.startfile(file2)
#os.system("notepad test") # Run command in the system shell
