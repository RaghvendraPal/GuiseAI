from flask import *  
import requests
import pathlib
import os
import datetime
import pandas as pd
from fuzzywuzzy import fuzz


app = Flask(__name__)
 
@app.route('/')  
def file_upload_form_v2():  
    return render_template("file_upload_form_v2.html")

@app.route('/all_image_v2', methods = ['POST', 'GET'])  
def all_image_v2():
    file_path = "static/upload_image/"
    try:
        if request.method == 'GET':
            data = os.listdir(file_path)
            
            image_name = []
            date_uploaded = []
            for name in data:
                t = os.path.getctime(file_path+name)
                date_uploaded.append(datetime.datetime.fromtimestamp(t))
                image_name.append(name)
            data = {'Name': image_name, 'Time': date_uploaded}
            dataframe = pd.DataFrame(data)
            dataframe = dataframe.sort_values(by=['Time'], ascending=False)
            print(dataframe)
            return render_template("all_image_v2.html", dataframe = dataframe)
    except Exception as e:
        print(e)
        return render_template("failure_v2.html", message = "Something went wrong!! Sorry !")

@app.route('/add_image', methods = ['POST', 'GET'])  
def add_image():  
    return render_template("add_image.html")

@app.route('/get_image', methods = ['POST', 'GET'])  
def get_image():  
    return render_template("get_image.html")

@app.route('/delete_image', methods = ['POST', 'GET'])  
def delete_image():  
    return render_template("delete_image.html")

 
@app.route('/success', methods = ['POST'])  
def success():  
    try:
        if request.method == 'POST':  
            f = request.files['file']  
            extensions = ['.jpg', '.jpeg', '.png']
            if pathlib.Path(f.filename).suffix.lower() in extensions:
                f.save("static/upload_image/"+f.filename)
                return render_template("success_v2.html", image_message = "Image Uploaded Successfully",image_name = f.filename, flag = True)  
            else:
                return render_template("failure_v2.html", message = "Your file extension should be .jpg, .jpeg, .png")
    except Exception as e:
        print(e)
        return render_template("failure_v2.html", message = "Something went wrong!! Sorry !")

@app.route('/search', methods = ['POST'])  
def search():  
    try:
        if request.method == 'POST':  
            filename = request.form.get("filename") 
            file_path = "static/upload_image/"
            flag = True
            for value in os.listdir(file_path):
                if fuzz.ratio(value.lower(), filename.lower()) >= 93:
                    flag = False
                    return render_template("success_v2.html", image_message = value,image_name = value, flag = True)  
            if flag:
                return render_template("failure_v2.html", message = "File Not Found")
    except Exception as e:
        print(e)
        return render_template("failure_v2.html", message = "Something went wrong!! Sorry !")
  
@app.route('/delete', methods = ['POST'])  
def delete():  
    try:
        if request.method == 'POST':  
            filename = request.form.get("filename") 
            file_path = "static/upload_image/"
            flag = True
            for value in os.listdir(file_path):
                if fuzz.ratio(value.lower(), filename.lower()) >= 75:
                    os.remove(file_path+value)
                    flag = False
                    return render_template("success_v2.html", image_message = str(value)+" Deleted Successfully.",image_name = value, flag = False)  
            if flag:
                return render_template("failure_v2.html", message = "File Not Exist in DataBase")
    except Exception as e:
        print(e)
        return render_template("failure_v2.html", message = "Something went wrong!! Sorry !")

if __name__ == '__main__':  
    app.run(debug=True)