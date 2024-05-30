from ast import Return
from ctypes.wintypes import INT
import os
import math

def GetFileList(dir = 'files'):
    return os.listdir(dir)

def WhatTipeOfFile(s): #Pass file
    ia_list = ['.png', '.jpeg']
    if s in ia_list:
        return 0
    else:
        return 1

def GetFileType(name):
    file_type = ''
    for i in range(1, len(name)):
        if name[-i] == '.': file_type += '.' ; break
        file_type += name[-i]
    
    a = ''
    for i in range(len(file_type)):
        a += file_type[-i - 1]
        
    return a

def AI(file, folder):
    return GetFileType(file)

def Clasify(name, folder = 'files'):
    file_type = GetFileType(name)
    file_AI_usable = WhatTipeOfFile(file_type)

    if file_AI_usable == 0:
        return AI(name, folder)
    
    return file_type

f = GetFileList()
for i in f:
    b = Clasify(i) 
    print(b)