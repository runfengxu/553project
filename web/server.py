from flask import Flask
from Image_recognition import predict
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')
    
@app.route('/result',methods =['GET',"POST"])
def display_result():
    if request.method =='POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        result = predict(f.filename)
        recommendation = []
        result = {}
        for item in recommendation:
            result[item]=db.get_img_url(item)
        return render_template("dispaly.html",result = result)
@app.route('/product/<asin>')
def hello_name(asin):
    metadata = db.get('metadata')
    review= db.get('review')
    return render_template('product.html',metadata = metadata,review = review)


if __name__ == '__main__':
    app.debug=True
    app.run()
