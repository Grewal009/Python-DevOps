import os

folderPaths = input("enter folder paths separated by space: ").split()
#print(folderPaths)

for folder in folderPaths:
    # exception handling if folder not exists
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("folder not available =>> "+ folder)
        continue
    print("listing files for folder:==>> "+ folder)
    for file in files:
        print(file)