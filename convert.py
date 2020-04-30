import json
import gzip
def convert(output,input):
    def parse(path):
        g = gzip.open(path, 'r')
        for l in g:
            yield json.dumps(eval(l))

    f = open(output, 'w')
    for l in parse(input):
        f.write(l + '\n')


convert("dataset/meta_cloth.json","dataset/meta_Clothing_Shoes_and_Jewelry.json.gz")

convert("dataset/reviews_cloth.json","dataset/reviews_Clothing_Shoes_and_Jewelry.json.gz")

