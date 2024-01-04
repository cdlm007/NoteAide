import math
import os
import random

path = r"./EnglishWords/"

while 1:

    words = []
    meanings = []
    sounds = []
    passed_in = []
    n = 0

    print(os.listdir(path))
    fileName = input("文件名：")


    if fileName.isdigit():
        fileName = int(fileName)
        fileName = os.listdir(path)[fileName]

    #打开文件,提取单词意思音标
    with open(path+fileName,"r",encoding="utf-8") as f:
        lines = f.readlines()
        n = len(lines)
        for i in range(n):
            parts = lines[i].split()
            words.append(parts[0].strip())
            meanings.append(parts[1].strip())

        f.close()
    times = n
    print()
    print("此文件共有{}个单词".format(n))
    print("根据中文给出对应英文")
    while times:
        ranIn = random.randint(0,n-1)

        #已通过的跳过
        if ranIn in passed_in:
            continue

        meaning = meanings[ranIn]
        word = words[ranIn]
        print("="*40)
        print(meaning)
        inputword = input("word:")
        if inputword == word:
            print("right!")
            passed_in.append(ranIn)
        else:
            print("错误，正确答案："+word)
            times+=1
        times-=1
    print()