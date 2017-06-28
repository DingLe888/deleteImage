# deleteImage-Python
批量删除未使用图片脚本

## 一、目的
工程迭代的过程中，很多之前使用的图片现在放弃使用，但是图片还遗留在工程中，造成工程体积变大，打包体积变大。为解决这一问题，编写此脚本批量删除工程中未使用的图片。

## 二、使用
打开`deleteImage-Python.py`,填写所有图片存放路径、js文件存放路径。
``` python
#存放图片所有路径的数组
imagePaths = ["/Users/dingle/Desktop/MyProject/elifehome/common_modules/image",
              "/Users/dingle/Desktop/MyProject/elifehome/common_modules/image-new"]
#存放js文件所有路径的数组
jsPaths = ["/Users/dingle/Desktop/MyProject/elifehome/apps",
           "/Users/dingle/Desktop/MyProject/elifehome/common_modules/ehomekit"]
```

运行脚本。打开终端：
``` ruby
python /Users/tangjr/Documents/deleteImage/deleteImage-Python.py
```

## 三、思路
1、遍历所有图片文件，拿到所有图片对象。
2、遍历所有js文件，每一个js文件都比对所有图片对象。如果使用到某图片，那么这个图片的使用次数加一。
3、最终遍历所有图片对象，对于使用次数是0的图片，做出删除处理。


