from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
import cv2
import os
import io
import numpy as np

app = Flask(__name__, static_folder="./src", template_folder="./templates")

app.config["DEBUG"] = True

UPLOAD_FOLDER = './src/save_images'
REF_FOLDER = '/src/save_images'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post", methods=["GET","POST"])
def post():
    if request.method == "POST":
        if not request.files["file-submit"].filename == "":
            dic = {}
            img_file = request.files["file-submit"]
            f = img_file.stream.read()
            bin_data = io.BytesIO(f)
            file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            raw_img_url = os.path.join(UPLOAD_FOLDER, "raw_" + secure_filename(img_file.filename))
            cv2.imwrite(raw_img_url, img)
            ref_img_url = os.path.join(REF_FOLDER, "raw_" + secure_filename(img_file.filename))
            dic["img_url"] = ref_img_url
        else:
            pass
    else:
        pass

    return jsonify(dic)

@app.route("/post_text", methods=["GET","POST"])
def post_text():
    if request.method == "POST":
        dic = {}
        if request.form["input-text"]:
            text = request.form["input-text"]
            dic["text"] = text
        else:
            dic["text"] = " "
            pass
    else:
        pass

    return jsonify(dic)

if __name__=="__main__":
    app.run(debug=True)
