import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/color_reco/', methods=['GET','POST'])
def color_reco():
    if request.method == 'GET':
        return render_template('color_home.html')
    elif request.method == 'POST':
        client_img = request.files['client_img']
        cate1 = request.form['cate1']
        cate2 = request.form['cate2']
        img_filename = secure_filename(client_img.filename)
        client_img.save(os.path.join('./static/image', img_filename))
        return render_template('color_img_upload.html', cate1 = cate1, cate2 = cate2,
                                img_name='image/'+img_filename, graph="image/graph.png", bar_graph="image/bar_graph.jpg")

@app.route('/thumnail_reco/', methods=['GET','POST'])
def thumnail_reco():
    if request.method == 'GET':
        return render_template('thumnail_home.html')
    elif request.method == 'POST':
        client_images = request.files.getlist("client_img[]")
        cate1 = request.form['cate1']
        cate2 = request.form['cate2']
        file_name_list = []
        img_num = 0
        for img in client_images:
            img_num+=1
            img_filename = secure_filename(img.filename)
            file_name_list.append('image/'+img_filename)
            img.save(os.path.join('static/image', img_filename))
        return render_template('thumnail_img_upload.html', cate1 = cate1, cate2 = cate2, imgs_name_list=file_name_list, img_num=img_num)

if __name__ == '__main__':
    app.run(debug=True)
 
#http://127.0.0.1:5000/


