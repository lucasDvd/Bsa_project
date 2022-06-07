"""main.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/10BeIpWUCHrcTP4B5d74YFRWtKXGxjOme
"""

import os

from flask import Flask, render_template, request, url_for
from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1

#from google.colab import drive

#drive.mount('/content/gdrive', force_remount= True)
#path = "gdrive/My Drive/Colab Notebooks/BSA/classificationproject-34308-8e6bee0ea720.json"
#path2= r"C:\Users\lucas\Documents\Master SI\Big-Scale\Amazon_project\classificationproject-349308-f342b1166ce0.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/lucas_dvd/Amazon_project/classificationproject-349308-f342b1166ce0.json"


def predict(content):

    options = ClientOptions(api_endpoint='eu-automl.googleapis.com')
    prediction_client = automl_v1.PredictionServiceClient(client_options=options)
#    payload = {'text_snippet': {'content': content, 'mime_type': 'text/plain'}}
#    response=prediction_client.predict(name=, payload=payload)
    text_snippet = automl_v1.TextSnippet(content=content, mime_type='text/plain')
    payload = automl_v1.ExamplePayload(text_snippet=text_snippet)
#    model_id = automl_v1.AutoMlClient.model_path("classificationproject-349308", 'eu', "TCN979071124069416960")

    response = prediction_client.predict(name="projects/858196023112/locations/eu/models/TCN979071124069416960", payload=payload)
    return response.payload


app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        content = request.form.get("to_classify")
        response = predict(content)
        return render_template("result.html", data=response, result=content)
    if request.method == 'GET':
        return "<h3> nothing to show </h3>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)