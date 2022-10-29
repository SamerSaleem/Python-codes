from csv import reader
import json
import csv

with open ('csvconverted.json') as data:  #you need  json file in same path or direct python to it.
    read_it = json.load(data)
    print(read_it)