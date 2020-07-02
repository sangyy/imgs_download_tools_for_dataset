import os
path=input('请输入文件路径(结尾加上/)：')       


for i, filename in enumerate(os.listdir(path)):
    with open(os.path.join(path,filename), 'rb') as imageFile:
        if imageFile.read().startswith(b'BM'):
            print(f"{i}: {filename} - found!")
        else:
            print(f"{i}: {filename} - OK!")
        #print("***")