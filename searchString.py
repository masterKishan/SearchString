import sys,os

sys.version

string = raw_input("Enter the string for search")
path = raw_input("Enter the path of directory")

allFiles = dict ([(f, None) for f in os.listdir (path)])

found = [f for f in allFiles if string in open(f).read()]

if found:
    print("String found in file:")
    print(found)
else:
    print("No String in any file")
