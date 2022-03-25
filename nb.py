import numpy as np
import json
from sklearn.feature_extraction import text

class NaiveBayes(object):

    def __init__(self):
        #load spreadsheet
        data = open('KickStarterData.csv').read()
        json.loads(data)
