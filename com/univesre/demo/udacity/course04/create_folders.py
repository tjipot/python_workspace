'''说明: 在参数'path'所在的文件夹中生成前缀形如'01_', '02_'的文件夹'''

def makeFolders(path):
    import os
    print(path)
    for fileName in range(1, 100):
        newFolderAbsPath = path + '/' + str(fileName).zfill(2) + '_'
        # print(newFolderAbsPath)
        # print(path+str('%02d', fileName))
        os.makedirs(newFolderAbsPath)


# makeFolders("/Users/Univesre/Desktop/tmpFolders")
''' # 如果文件已经存在, 会报错: FileExistsError:
[Errno 17] File exists: '/Users/UNIVESRE/Desktop/tmpFolders/01_'
'''
makeFolders("/Users/UNIVESRE/Desktop/tmpFolders")

