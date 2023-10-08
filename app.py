# from flask import Flask, render_template, jsonify, request, redirect, url_for
# import requests 

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route('/api')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/api/face_match', methods=['POST', 'GET'])
# def upload(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             return {"responseCode": "1", "responseMessage": "Success"}
# # def face_match():
# #     if request.method == 'POST':
# #         # check if the post request has the file part
# #         if ('file1' not in request.files):
# #             print('No file part')
# #             #return {"message": "No File Part"}
# #             return {"responseCode": "0", "responseMessage": "No File Part"}
# #         else:
# #             return{"responseCode": "1", "responseMessage": "Success!"}

# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return redirect(url_for("user", usr=user))
#     else:
#         return render_template("login.html")

# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"
#     data = {'title':'Python Requests','body':'Requests are awesome','userId':1} 
#     response = requests.post('https://jsonplaceholder.typicode.com/posts', data) 
#     print(response.status_code) 
#     print(response.text)



# if __name__ == "__main__":
#     app.run(debug = "True")

from flask import Flask, json, request, jsonify
import os
import urllib.request
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
 
#app.secret_key = "caircocoders-ednalan"
 
UPLOAD_FOLDER = 'C:/Users/sushr/Dropbox/My PC (LAPTOP-AC0PDSKE)/Desktop/Sushree/Internship/static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/')
def main():
    return 'Homepage'


@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if ('file1' not in request.files) or ('file2' not in request.files):
            print('No file part')
            resp = jsonify({"responseCode": "0", "responseMessage": "No File Part"})
            resp.status_code = 400
            return resp
        
    # if 'files[]' not in request.files:
    #     resp = jsonify({'message' : 'No file part in the request'})
    #     resp.status_code = 400
    #     return resp
 
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if file1.filename == '' or file2.filename == '':
        print('No selected file')
        resp = jsonify({"responseCode": "0", "responseMessage": "No Selected File"})
        resp.status_code = 400
        return resp

    # errors = {}
    success = False

    if allowed_file(file1.filename) and allowed_file(file2.filename):
            #call compare function and send response code if it matches or not matches
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)
            file1.save( os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            file2.save( os.path.join(app.config['UPLOAD_FOLDER'], filename2))
            success = True
    else :
        return {"responseCode": "0", "responseMessage": "Invalid File Type"}

    if success:
        resp = jsonify({'message' : 'Files successfully uploaded xyz'})
        resp.status_code = 201
        return resp
    
    # for file in files:      
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         success = True
    #     else:
    #         errors[file.filename] = 'File type is not allowed'
 
    # if success and errors:
    #     errors['message'] = 'File(s) successfully uploaded'
    #     resp = jsonify(errors)
    #     resp.status_code = 500
    #     return resp
    # if success:
    #     resp = jsonify({'message' : 'Files successfully uploaded'})
    #     resp.status_code = 201
    #     return resp
    # else:
    #     resp = jsonify(errors)
    #     resp.status_code = 500
    #     return resp
 
if __name__ == '__main__':
    app.run(debug=True)