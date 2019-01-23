#-*-coding:utf-8-*-
import os
import re;
## 复制SceneObj文件并提供别名
def renameSceneObj(path,base,path2):
    dirs = os.listdir(path)
    for file in dirs:
        no = re.search(r"\d+", file).group()  ##18
        newfile = file.replace(no, str(int(no) + base))
        sourceFile = os.path.join(path,file)
        targetFile = os.path.join(path2,newfile)
        open(targetFile, "wb").write(open(sourceFile, "rb").read())
        print "完成："+targetFile

def getOpsMap(path):
    map = "ops = {";
    file = open(path)
    for line in file:
        if re.search("^\s*\n*$",line) == None:
            if re.search("^\s*#+.*\n*$",line) == None:
                try:
                    if line.index("#") > 0:
                        line = line[0:line.index("#")-1]
                    items = line.split("=")
                    map += items[1]+":'" +items[0].lstrip().rstrip() + "',"
                except BaseException:
                    print "==============================================="
                    print "error:"+line
    map += "}"
    print map