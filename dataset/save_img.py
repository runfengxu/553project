#import pandas as pd
import gzip
import urllib.request
from multiprocessing import Pool
import os
import json

class download():
    def __init__(self,path):
        self.path = path

    def parse(self,size=1024*1024):
        g = gzip.open(self.path, 'rb')
        fileEnd = os.path.getsize(self.path)
        chunkEnd = g.tell()
        while True:
            chunkStart = chunkEnd
            g.seek(size,1)
            g.readline()
            chunkEnd = g.tell()

            yield int(chunkStart),int(chunkEnd-chunkStart)
            if chunkEnd>fileEnd:
                break

    def get_img(self,a):
        try:
            if (('asin' in a) and ('imUrl' in a)):
                asin = a['asin']
                url = a['imUrl']
                urllib.request.urlretrieve(url, 'E:/553/553project/dataset/img/'+asin+".jpg")
                return 0
        except:
            return 1
    def process_wrapper(self,chunkStart,chunkSize):
        print('start chunk ',chunkStart)
        with gzip.open(self.path) as f:
            f.seek(chunkStart)
            lines = f.read(chunkSize).splitlines()
            for line in lines:
                line = json.dumps(eval(line))
                line = json.loads(line)
                self.get_img(line)

    def run_parallel(self,processes=8):
        processes = int(processes)
        pool = Pool(processes)
        # try:
        print(1)
        jobs =[]
        for chunkStart,chunkSize in self.parse():
            jobs.append(pool.apply_async(self.process_wrapper,args=(chunkStart,chunkSize)))
        for job in jobs:
            job.get()
            pool.close()

        # except Exception as e:
        #     print(e)
       
if __name__ =='__main__':
    case = download('E:/553/553project/dataset/meta_Clothing_Shoes_and_Jewelry.json.gz')
    case.run_parallel(8)