import json
import os
from crawl.百度翻译.CrwalAPI import crwal
import re

def is_chinese(text):
    pattern = r'[\u4e00-\u9fa5]'  # Unicode范围内的汉字编码
    if re.search(pattern, text):
        return True
    else:
        return False

def is_english(text):
    pattern = '[a-zA-Z]+'  # 只包含大小写字母的模式
    if re.match(pattern, text):
        return True
    else:
        return False


path = r"./EnglishWords/"

if not os.path.exists(path):
    os.makedirs(path)
    print("path创建完成")
else:
    print(os.listdir(path))

fileName = input("文件名：")
if fileName.isdigit():
    fileName = int(fileName)
    fileName = os.listdir(path)[fileName]
print("已选择："+fileName)
PathFile = path+fileName
file = open(PathFile,"a",encoding="utf-8")

writeFormat1 = "{:<20s}{:<15s}{:<10s}\n" #无音标
writeFormat2 = "{:<20s}{:<15s}/{:<10s}\n" #有音标

while 1:
    meaning,yinbiao = "",""
    word = input("word:")
    if is_chinese(word):
        print("输入不可为中文")
        continue
    res = crwal(word)
    jsonText = json.loads(res.text)
    if "trans_result" in jsonText:
        meaning = jsonText["trans_result"]["data"][0]["dst"]
    else:
        print("单词意思查无,跳过！")
        continue
    if "dict_result" in jsonText:
        if 'ph_am' in jsonText["dict_result"]["simple_means"]["symbols"][0]:
            yinbiao = jsonText["dict_result"]["simple_means"]["symbols"][0]['ph_am']

    print(meaning+"\t"+"/"+yinbiao+"/")
    OtherMeaning = input("增加词意(回车可跳过)：")
    if OtherMeaning == "del":
        print("已撤回此单词")
        continue
    if is_english(OtherMeaning):
        print("词意不可为英文,增加失败")
        OtherMeaning = ""

    if OtherMeaning != "":
        if yinbiao == "":
            file.write(writeFormat1.format(word,OtherMeaning+","+meaning,yinbiao))
        else:
            file.write(writeFormat2.format(word,OtherMeaning+","+meaning,yinbiao+"/"))
    else:
        if yinbiao == "":
            file.write(writeFormat1.format(word,meaning,yinbiao))
        else:
            file.write(writeFormat2.format(word,meaning,yinbiao+"/"))

    file.flush()
    res.close()

file.close()


