#!/usr/bin/python3 
#coding=utf-8
import os
import os.path
rootdir="/Users/evan/Downloads"
_list=os.listdir(rootdir)
for i in range(0,len(_list)):
    path=os.path.join(rootdir,_list[i])
    if os.path.isfile(path):
        print(path)