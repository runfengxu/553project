from flask import Flask,request,jsonify, render_template
from werkzeug import secure_filename
from extract_feature import extract
from readpy import predict
import sys
from flask_pymongo import PyMongo


#from readpy import
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/amazonproducts'
mongo = PyMongo(app)

@app.route('/')
def main_page():
    return render_template('index.html')
    
@app.route('/result',methods =['GET',"POST"])
def display_result():
    if request.method =='POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        feature = extract(f.filename)
        # print(len(feature[0]), file=sys.stdout)
        products = predict(feature[0])
        metadata = mongo.db.metadata
        output = {}
        refer = {}
        i=0
        while(i<len(products)):
            asin = products[i]
            asin = str(asin)[2:-1]
            print(asin)
            try:
                cursor = metadata.find({"asin":asin})
                p=cursor[0]
                output[p['asin']]= p['imUrl']
                i+=1
            except:
                i+=1
                continue
            
            #refer[p['title']]=p['asin']
        #refer = jsonify(refer)
        return render_template('display.html',result = output)

@app.route('/product/<asin>')
def hello_name(asin):
    metadata = mongo.db.metadata
    review= mongo.db.reivews
    # print(title)
    cursor = metadata.find({"asin":asin})[0]
    meta = {}
    candidate = ['title','brand','description','price']
    url = cursor["imUrl"]
    for element in candidate:
        if element in cursor:
            meta[element]=cursor[element]
    re={}
    try:
        cursor2 = review.find({"asin":asin})[0]
    
    
        
    
        candidate2 = ["reviewerID","reviewerName","reviewText","overall","summary","unixReviewTime","reviewTime"]
    
        for element in candidate2:
            if element in cursor2:
                re[element]=cursor2[element]
        
    except:
        return render_template('product.html',meta = meta,review = re,url = url)
    return render_template('product.html',meta = meta,review = re,url = url)


if __name__ == '__main__':
    app.debug=True
    app.run()