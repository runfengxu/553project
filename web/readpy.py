import array
import numpy as np
from scipy.stats import pearsonr

path = 'C:/Users/admin/Downloads/image_features_Baby.b'#从数据库中提取多个图像feature的路径
target = ('123', [1, 2, 4, 0, 5, 0, 0])#image recognition获得的单个feature，应该不用前面那个asin
targetid, targetarray = target

simarray = {}

def readImageFeatures(path):
  f = open(path, 'rb')
  while True:
    asin = f.read(10)
    if asin == '': break
    a = array.array('f')
    a.fromfile(f, 4096)
    #print(a)
    yield asin,a.tolist()#读数据库中的数据，asin和feature向量
                        #target数据是b文件格式的话重新调用一个这样的func

asin = readImageFeatures(path)

i=0
#targetarray adjustment
while(i<len(targetarray)):#float转int操作，前面你们处理过数据的话这里应该可以注释掉while
  targetarray[i] = int(targetarray[i]*1000)
  i=i+1

i=0
while(i<5):#这里我就取了5个数据
  id, newarray = next(asin)
  #print(id)
  #print(newarray)
  j=0#array from db adjustment
  while (j < len(newarray)):#float转int操作，前面你们处理过数据的话这里应该可以注释掉while
     newarray[j] = int(newarray[j] * 1000)
     j = j + 1
  sim = pearsonr(targetarray, newarray)[0]#算相关系数， pearson coefficient
  simarray[i] = [sim, id]#相关系数和asin
  i=i+1

simarray1 = sorted(simarray.items(), key=lambda x: x[1])#能排序，没法提取asin
while(i<len(simarray1)):
  print(simarray1[i])
  #simarray1[i]
  i=i+1

