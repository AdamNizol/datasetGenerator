import os
import json

imgData = {}
try:
    with open('result.txt') as json_file:
        imgData = json.load(json_file)
        for key in imgData:
            print(key)
        print(" * file loaded")
except FileNotFoundError:
    print(" * No file found")
