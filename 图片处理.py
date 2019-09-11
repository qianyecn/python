#!/usr/bin/python3 
#coding=utf-8
from  PIL import Image,ImageColor
i=1
j=1
f="/Users/evan/Downloads/test.png"
# f=input('拖入图片文件：')
# 头尾去空格
f=f.strip()
img=Image.open(f)
img = img.convert('RGBA') # 修改颜色通道为RGBA
print(img.size)
# 获取指定坐标像素数据
print(img.getpixel((4,4)))
# rgb
old=[255,0,0,255]
new=[128,128,128,255]
width,height=img.size
# width=img.size[0]
# height=img.size[1]
# 替换颜色函数
def chagecolor(my_old,my_new):
    # 引用全局变量
    global img
    for i in range(0,width):
        for j in range(0,height):
            data=(img.getpixel((i,j)))
            # print(data)
            # print(data[0])
            if (data[0]==my_old[0] and data[1]==my_old[1] and data[2]==my_old[2] and data[3]==my_old[3]):
                img.putpixel((i,j),(my_new[0],my_new[1],my_new[2],my_new[3]))
    print("颜色替换成功")
    img=img.convert("RGBA")
    img.save("/Users/evan/Downloads/test1.png")
    print("保存成功")
chagecolor(old,new)
# img.show()