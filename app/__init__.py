from flask import Flask, g, render_template, request
from flask import redirect, url_for, abort

from bs4 import BeautifulSoup
import pandas as pd
import os
import requests

import io
import base64

app = Flask(__name__)

@app.route('/')
def main():
    """
    Loads template for main page
    """
    return render_template('main_better.html')

@app.route('/form/', methods=['POST', 'GET'])
def ask():
    """
    Loads page for user input
    """
    if request.method == 'GET':
        return render_template('form.html')
    else: 
        try:
            return redirect(url_for('resume'))
        except:
            return render_template('form.html', error=True) 

@app.route('/resume/', methods=['POST'])
def resume():
    """
    Loads information from user input into html template and outputs resume
    """
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    location=request.form['location']
    phone=request.form['phone']
    email=request.form['email']

    school1=request.form['school1']
    school1startdate=request.form['school1startdate']
    school1enddate=request.form['school1enddate']
    school1GPA=request.form['school1GPA']
    school1Relevant_Courses=request.form['school1Relevant_Courses']


    company1=request.form['company1']
    company1position=request.form['company1position']
    company1startdate=request.form['company1startdate']
    company1enddate=request.form['company1enddate']
    company1experience1=request.form['company1experience1']
    company1experience2=request.form['company1experience2']

    company2=request.form['company2']
    company2position=request.form['company2position']
    company2startdate=request.form['company2startdate']
    company2enddate=request.form['company2enddate']
    company2experience1=request.form['company2experience1']
    company2experience2=request.form['company2experience2']

    Achievement1=request.form['Achievement1']
    Achievement1description1=request.form['Achievement1description1']

    languages=request.form['languages']
    technical_skills=request.form['technical_skills']
    interests=request.form['interests']

    return render_template('resume.html', first_name=first_name, last_name=last_name, location=location, phone=phone, email=email, 
    school1=school1, school1startdate=school1startdate, school1enddate=school1enddate, school1GPA=school1GPA, school1Relevant_Courses=school1Relevant_Courses, 
    company1=company1, company1position=company1position, company1startdate=company1startdate, company1enddate=company1enddate, company1experience1=company1experience1, company1experience2=company1experience2,
    company2=company2, company2position=company2position, company2startdate=company2startdate, company2enddate=company2enddate, company2experience1=company2experience1, company2experience2=company2experience2,
    Achievement1=Achievement1, Achievement1description1=Achievement1description1, 
    languages=languages, technical_skills=technical_skills, interests=interests)

@app.route('/indeed_test/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('indeed_test.html')
    else:
        user_job = request.form['job']
        user_location = request.form['location']
        user_job = user_job.replace(" ", "%20")
        user_location = user_location.replace(" ", "%20")
        current_url = f"https://www.indeed.com/jobs?q={user_job}&l={user_location}"

        return render_template('indeed_test.html', user_job=user_job, user_location=user_location, current_url=current_url)



@app.route('/about/')
def hello():
    return render_template('about.html')



