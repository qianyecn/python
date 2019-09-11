#!/usr/bin/python3 
#coding=utf-8
from  PIL import Image,ImageColor
import os
i=1
j=1
os.chdir('/Users/evan/Pictures/tmp')
# f="test1.png"
num=input("编号:")
num_n=str(int(num)+1)
f=input('拖入图片文件：')
# 头尾去空格
f=f.strip()
img=Image.open(f)
img=img.convert("RGB")
def _1to2_crop():
    global img
    width,height=img.size
    img1=img.crop((0,0,width//2,height))
    img2=img.crop((width//2,0,width,height))
    img1.save("/Users/evan/Pictures/tmp1/优王宣传册"+num+".png")
    img2.save("/Users/evan/Pictures/tmp1/优王宣传册"+num_n+".png")
    print("保存成功")
_1to2_crop()
# print(img.size)
