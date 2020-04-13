import array
import numpy as np
from scipy.stats import pearsonr
import sys
def predict(targetarray):
  path = '../dataset/image_features_Baby.b'#从数据库中提取多个图像feature的路径
  simarray = {}
  def readImageFeatures(path):
    f = open(path, 'rb')
    while True:
      asin = f.read(10)
      if asin == '': break
      a = array.array('f')
      a.fromfile(f, 4096)
      yield asin,a.tolist()

  asin = readImageFeatures(path)

  i=0
  while(i<len(targetarray)):#float转int操作，前面你们处理过数据的话这里应该可以注释掉while
    targetarray[i] = int(targetarray[i]*1000)
    i=i+1
  i=0
  # for i in range(10000):
  #   idx, newarray = next(asin)
  i=0
  while(i<1000):
    idx, newarray = next(asin)
    j=0
    while (j < len(newarray)):#float转int操作，前面你们处理过数据的话这里应该可以注释掉while
      newarray[j] = int(newarray[j] * 1000)
      j = j + 1
    sim = pearsonr(targetarray, newarray)[0]#算相关系数， pearson coefficient
    simarray[i] = [sim, idx]#相关系数和asin
    i=i+1

  simarray = sorted(simarray.values(), key=lambda x: x[1], reverse = True)
  #print(simarray, file=sys.stdout)
  #输出top n个最高相关系数的product id
  
  id_array = []
  i=0
  while(i<1000):
    value = simarray[i]
    idx = value[1]
    #print(value, file=sys.stdout)
    id_array.append(idx)
    i=i+1
  return id_array