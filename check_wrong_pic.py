import os
path=input('请输入文件路径(结尾加上/ 例如：imgs/face/)：')       


for i, filename in enumerate(os.listdir(path)):
    with open(os.path.join(path,filename), 'rb') as imageFile:
        if imageFile.read().startswith(b'BM'):
            print(f"{i}: {filename} - found!")
        
        #print("***")
print("End!")