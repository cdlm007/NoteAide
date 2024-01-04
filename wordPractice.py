import os

path = r"./EnglishWords/"

while 1:
    words = []
    meanings = []
    n = 0
    print(os.listdir(path))
    fileName = input("文件名：")
    if fileName.isdigit():
        fileName = int(fileName)
        fileName = os.listdir(path)[fileName]
    with open(path+fileName,"r",encoding="utf-8") as f:
        lines = f.readlines()
        n = len(lines)
        for i in range(lines):
            wordmeaning = lines[i].split(" ")
            meanings[i] = wordmeaning[1]
            words[i] = wordmeaning[0]
        f.close()
    while n:
        

    print()