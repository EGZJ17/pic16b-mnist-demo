from flask import Flask, g, render_template, request

import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pickle

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io
import base64

### stuff from last class
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main_better.html')

@app.route('/form/', methods=['POST', 'GET'])
def ask():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        #function to store the imputs 
        try:
            return render_template('form.html', thanks=True)
        except:
            return render_template('form.html', error=True)
#######

@app.route('/indeed_test/', methods=['POST', 'GET'])
def submit():
    return render_template('indeed_test.html')

####### group exercise
@app.route('/about/')
def hello():
    return render_template('about.html')

#######
# Request object: https://flask.palletsprojects.com/en/2.1.x/api/#flask.Request
@app.route('/submit-basic/', methods=['POST', 'GET'])
def submit_basic():
    pass

# matplotlib: https://matplotlib.org/3.5.0/gallery/user_interfaces/web_application_server_sgskip.html
# plotly: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946

@app.route('/submit-advanced/', methods=['POST', 'GET'])
def submit_advanced():
    pass

