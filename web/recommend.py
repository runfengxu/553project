import array
import numpy as np
from scipy.stats import pearsonr
from scipy.spatial import distance
import sys
import pymongo
import heapq

def predict(targetarray):
    H=[(0,0)]*10
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo = myclient["amazonproducts"]
    feature = mongo.feature
    cur = feature.find()
    count=0
    for i in cur:
        asin = list(i.keys())[1]
        b = i[asin]
        dist = distance.euclidean(targetarray,b[0])
        heapq.heappushpop(H,(dist,asin[4:]))
        count+=1
    print(count)
    result = []
    for i in H:
        result.append(i[1])
    return result