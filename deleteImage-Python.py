#coding:utf-8 

import os
import os.path
import json

#存放图片所有路径的数组
imagePaths = ["/Users/dingle/Desktop/MyProject/elifehome/common_modules/image",
              "/Users/dingle/Desktop/MyProject/elifehome/common_modules/image-new"]
#存放js文件所有路径的数组
jsPaths = ["/Users/dingle/Desktop/MyProject/elifehome/apps",
           "/Users/dingle/Desktop/MyProject/elifehome/common_modules/ehomekit"]
#图片模型类，
# searchPath：即js文件中引用图片使用的路径，后面查找js文件是否使用了本路径即可检查到本图片是否被使用。
#fullPath：图片的全路径，后期删除图片时使用。
#searchCount：使用的次数，遍历js文件检查到使用，则次数加一。最终结算如是0次则删除。
class imageModel:
    def __init__(self,searchPath,fullPath):
        self.searchPath = searchPath
        self.fullPath = fullPath

    searchCount = 0        
#声明一个存放图片的数组    
imageModels = []       

#遍历所有图片存放文件夹
for imagePath in imagePaths:
    #找到图片文件夹中的package.json文件，读取name属性的值，用于拼接后面的searchPatch
    packagePath = os.path.join(imagePath,'package.json')
    f = open(packagePath,encoding = 'utf-8')
    packageStr = f.read()
    f.close()
    packageDic = json.loads(packageStr)
    baseName = packageDic['name']
    
    #遍历图片文件夹下的所有子目录
    for root,dirs,files in os.walk(imagePath):
        #拼接搜索路径前半部分（没有文件名呢）
        filePath = root[len(imagePath):]
        filePath = baseName + filePath

        #遍历当前搜索路径下的所有文件
        for name in files:
            #拆分文件名和文件后缀名
            fileName, fileSuffix = os.path.splitext(name)
            #如果文件是图片类型
            if fileSuffix in ['.png','.JPG','jpg']:
                #拼接文件全路径
                fullPath = os.path.join(root,name)
                #如果文件名中有@2x、@3x字符的话，则去掉这个字符
                if name.find("@") != -1:
                    index = name.find("@")
                    name = name.replace(name[index:index + 3],'')
                    
                 #拼接最终搜索路径（js文件中使用的）
                searchPath = os.path.join(filePath,name)
                
                #把搜索路径、全路径装入对象，把对象装入数组
                imageM = imageModel(searchPath,fullPath)
                imageModels.append(imageM)

#遍历所有存放js文件的路径
for jsPath in jsPaths:
    #遍历js文件路径下所有子目录
    for root,dirs,files in os.walk(jsPath):

        #遍历子目录下所有文件
        for name in files:
                #拆分文件名、文件后缀，判断是否为js文件
                fileName, fileSuffix = os.path.splitext(name)
                if fileSuffix == '.js':
                    #拼接文件全路径
                    filePath = os.path.join(root,name)

                    #打开文件，以utf-8编码打开（此处如果不指明打开编码，默认是ASCII编码。）
                    f = open(filePath,encoding='utf-8')
                    #读取文件为字符串
                    doc = f.read()
                    #遍历图片对象数组，如果js文本中包含该图片的搜索路径，图片的searchCount + 1
                    for imageM in imageModels:
                        if doc.find(imageM.searchPath) != -1:
                            imageM.searchCount += 1
                    f.close()
                    
#最终遍历图片，发现图片searchCount == 0 的，删除该图片
for imageM in imageModels:
    if imageM.searchCount == 0:
        print('remove ==>',imageM.fullPath)
        os.remove(imageM.fullPath)

print('共删除图片' + len(imageModels) + '张')
        




        
