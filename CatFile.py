import os

path = r"./EnglishWords/"

while 1:
    print(os.listdir(path))
    fileName = input("文件名：")
    if fileName.isdigit():
        fileName = int(fileName)
        fileName = os.listdir(path)[fileName]
    with open(path+fileName,"r",encoding="utf-8") as f:
        print(f.read())
    print()
f.close()