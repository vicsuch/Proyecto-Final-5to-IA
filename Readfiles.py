from ast import Return
from ctypes.wintypes import INT
import os
import math

def GetFileList(dir = 'files'):
    return os.listdir(dir)

def OpenFile(dir, folder = 'files'):
    return open(
        os.path.join(folder, dir)
    )

def WhatTipeOfFile(s): #Pass file
    ia_list = ['.png', '.jpeg']
    if s in ia_list:
        return 0
    else:
        return 1

def GetFileType(file_name):
    file_type = ''
    for i in range(1, len(file_name)):
        if file_name[-i] == '.': file_type += '.' ; break
        file_type += file_name[-i]
    
    a = ''
    for i in range(len(file_type)):
        a += file_type[-i - 1]
        
    return a

def AI(file):
    return GetFileType(file.name)

def Clasify(file):
    name = file.name
    file_type = GetFileType(name)
    file_AI_usable = WhatTipeOfFile(file_type)

    if file_AI_usable == 0:
        return AI(file)
    
    return file_type

f = GetFileList()
for i in f:
    b = Clasify(OpenFile(i)) 
    print(b)