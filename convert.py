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


convert("dataset/meta_data.json","dataset/meta_Baby.json.gz")

convert("dataset/reviews.json","dataset/reviews_Baby.json.gz")

