from flask import Flask,request, render_template
from werkzeug import secure_filename
from extract_feature import extract
#from readpy import
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')
    
@app.route('/result',methods =['GET',"POST"])
def display_result():
    if request.method =='POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        feature = extract(f.filename)

        return str(feature)
#         result = predict(f.filename)
#         recommendation = []
#         result = {}
#         for item in recommendation:
#             result[item]=db.get_img_url(item)
#         return render_template("dispaly.html",result = result)
# @app.route('/product/<asin>')
# def hello_name(asin):
#     metadata = db.get('metadata')
#     review= db.get('review')
#     return render_template('product.html',metadata = metadata,review = review)


if __name__ == '__main__':
    app.debug=True
    app.run()