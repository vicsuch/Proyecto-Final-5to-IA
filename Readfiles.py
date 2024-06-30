import os
import EjecutarIA

def GetFileList(dir = 'files'):
    return os.listdir(dir)

def WhatTipeOfFile(s): #Pass file
    s = s.lower()
    ia_list = ['png', 'jpeg']
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

def AI(image):
    print('IA...')
    return EjecutarIA.PassImage(image)

def Clasify(image):
    print('Clasificando...')
    file_type = image.format
    print('file_type:', file_type)
    file_AI_usable = WhatTipeOfFile(file_type)

    if file_AI_usable == 0:
        print('Pasando imagen a IA')
        a = AI(image)
        print('IA_result,', a)
        return a
    
    return file_type