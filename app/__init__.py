from flask import Flask, g, render_template, request
from flask import redirect, url_for, abort

from selenium import webdriver
import os

import io
import base64

### stuff from last class
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main_better.html')

@app.route('/form/')
def ask():
    return render_template('form.html')


# @app.route('/form/', methods=['POST', 'GET'])
# def ask():
#     if request.method == 'GET':
#         return render_template('form.html')
#     else:
#         #function to store the imputs 
#         try:
#             return render_template('form.html', thanks=True)
#         except:
#             return render_template('form.html', error=True) 
#######

@app.route('/resume/', methods=['POST'])
def resume():
    first_name=request.form['request.form']
    last_name=request.form['last_name']
    location=request.form['location']
    phone=request.form['phone']
    email=request.form['email']

    school1=request.form['school1']
    school1startdate=request.form['school1startdate']
    school1enddate=request.form['school1enddate']
    school1GPA=request.form['school1GPA']
    school1Relevant_Courses=request.form['school1Relevant_Courses']

    school2=request.form['school2']
    school2startdate=request.form['school2startdate']
    school2enddate=request.form['school2enddate']
    school2GPA=request.form['school2GPA']
    school2Relevant_Courses=request.form['school2Relevant_Courses']

    company1=request.form['company1']
    company1position=request.form['company1position']
    company1startdate=request.form['company1startdate']
    company1enddate=request.form['company1enddate']
    company1experience1=request.form['company1experience1']
    company1experience2=request.form['company1experience2']
    company1experience3=request.form['company1experience3']

    company2=request.form['company2']
    company2position=request.form['company2position']
    company2startdate=request.form['company2startdate']
    company2enddate=request.form['company2enddate']
    company2experience1=request.form['company2experience1']
    company2experience2=request.form['company2experience2']
    company2experience3=request.form['company2experience3']

    company3=request.form['company3']
    company3position=request.form['company3position']
    company3startdate=request.form['company3startdate']
    company3enddate=request.form['company3enddate']
    company3experience1=request.form['company3experience1']
    company3experience2=request.form['company3experience2']
    company3experience3=request.form['company3experience3']

    Achievement1=request.form['Achievement1']
    Achievement1description1=request.form['Achievement1description1']
    Achievement1description2=request.form['Achievement1description2']
    
    Achievement2=request.form['Achievement2']
    Achievement2description1=request.form['Achievement2description1']
    Achievement2description2=request.form['Achievement2description2']
    
    languages=request.form['languages']
    technical_skills=request.form['technical_skills']
    interests=request.form['interests']

    return render_template('resume.html', first_name=first_name, last_name=last_name, location=location, phone=phone, email=email, school1=school1, school1startdate=school1startdate, school1enddate=school1enddate, school1GPA=school1GPA, school1Relevant_Courses=school1Relevant_Courses, school2=school2, school2startdate=school2startdate, school2enddate=school2enddate, school2GPA=school2GPA, school2Relevant_Courses=school2Relevant_Courses, company1=company1, company1position=company1position, company1startdate=company1startdate, company1enddate=company1enddate, company1experience1=company1experience1, company1experience2=company1experience2, company1experience3=company1experience3, company2=company2, company2position=company2position, company2startdate=company2startdate, company2enddate=company2enddate, company2experience1=company2experience1, company2experience2=company2experience2, company2experience3=company2experience3, company3=company3, company3position=company3position, company3startdate=company3startdate, company3enddate=company3enddate, company3experience1=company3experience1, company3experience2=company3experience2, company3experience3=company3experience3, Achievement1=Achievement1, Achievement1description1=Achievement1description1, Achievement1description2=Achievement1description2, Achievement2=Achievement2, Achievement2description1=Achievement2description1, Achievement2description2=Achievement2description2, languages=languages, technical_skills=technical_skills, interests=interests)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)


@app.route('/indeed_test/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('indeed_test.html')
    else:
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
            driver.get("https://medium.com")
            source = driver.page_source
            return render_template('indeed_test.html', source=source)
        except:
            return render_template('indeed_test.html', error=True)

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

