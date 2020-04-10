#import pandas as pd
import gzip
import urllib.request
def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def getDF(path):
    j = 0
    df = {}
    d = parse(path)
    while(True):
        try:
            a = next(d)
            if (('asin' in a) and ('imUrl' in a)):
                asin = a['asin']
                url = a['imUrl']
                urllib.request.urlretrieve(url, 'img/'+asin+".jpg")
                j += 1
            if j%1000==0:
                print(j)
            else:
                continue
        except StopIteration:
            print('finish')   
        except:
            continue

df = getDF('meta_Clothing_Shoes_and_Jewelry.json.gz')

    
