import flask
from flask_cors import CORS, cross_origin
import os
import random
import json

imgFolder = "images/"
imgs = os.listdir(imgFolder)
imgData = {}
try:
    with open('result.txt') as json_file:
        imgData = json.load(json_file)
        for key in imgData:
            imgs.remove(key)
        print(" * file loaded")
except FileNotFoundError:
    print(" * No file found")

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

# Returns the imgId for an image that has not yet been marked
@app.route('/', methods=['GET'])
@cross_origin()
def home():
    if(len(imgs) < 1):
        return "complete"
    return imgs[random.randint(0, len(imgs)-1 )]

# GET: Returns image based on imgId
# POST: Stores image region from user
@app.route('/<imgId>', methods=['GET', 'POST'])
@cross_origin()
def imgById(imgId):
    path = imgFolder+imgId
    if(flask.request.method == 'GET'):
        if(imgId == "complete"):
            return flask.send_file("success.png", mimetype='image/png')
        return flask.send_file(path, mimetype='image/png')

    elif(flask.request.method == 'POST'):
        if(imgId == "complete"):
            return ""
        print("image "+path+" has region ")
        print(flask.request.json)
        imgData[imgId] = flask.request.json
        if(imgId in imgs):
            imgs.remove(imgId)
        saveState()
        return ""

def saveState():
    with open('result.txt', 'w') as outfile:
        json.dump(imgData, outfile)

app.run()
