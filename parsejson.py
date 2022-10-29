from csv import reader
import json

with open ('csvconverted.json') as data:  #you need  json file in same path or direct python to it.
    read_it = json.load(data)
    print(read_it)