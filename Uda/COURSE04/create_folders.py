def makeFolders(path):
    import os
    print(path)
    for fileName in range(1, 41):
        newFolderAbsPath = path + '/' + str(fileName).zfill(2) + '_'
        # print(newFolderAbsPath)
        # print(path+str('%02d', fileName))
        os.makedirs(newFolderAbsPath)


makeFolders("/Users/Univesre/Desktop/tmpFolders")
