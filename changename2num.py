import os
path=input('请输入文件路径(结尾加上/ 例如：imgs/face/)：')       

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

n=0
for i in fileList:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + fileList[n]   # os.sep添加系统分隔符
    
    #设置新文件名
    newname=os.path.sep.join([path, "{}.jpg".format(
            str(n).zfill(8))])
    
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)
    
    n+=1