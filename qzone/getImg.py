'''
将imgAddr的所有图片下载下来
'''
from PIL import Image
from io import BytesIO
import os
import requests

os.mkdir("img")

imgAddrList = []
with open("imgAddr.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        imgAddrList.append(line)
    f.close()

count = 0
for i in imgAddrList:
    if i[:4] == "http":
        try:
            r = requests.get(i)
            print(r.status_code)
            img = Image.open(BytesIO(r.content))
            img = img.convert("RGB")
            img.save(os.path.dirname(__file__) + "/img/" + str(count) + ".jpg")
            count += 1
        except:
            f = open("log.txt","a+")
            f.write(i+"\n")
            f.close()
