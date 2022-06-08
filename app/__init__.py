from flask import Flask, g, render_template, request
from flask import redirect, url_for, abort

from bs4 import BeautifulSoup

HEADERS ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

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
        try:
            user_job = request.form['job']
            user_location = request.form['location']
            user_job_n = user_job.replace(" ", "%20")
            user_location_n = user_location.replace(" ", "%20")
            current_url = f"https://www.indeed.com/jobs?q={user_job_n}&l={user_location_n}"

            #resp = requests.get(current_url)
            content = BeautifulSoup(requests.get(current_url, headers=HEADERS).content, 'lxml')
            jobs_list = []    
            jobs_fixedlist = []
            company_list = []
            location_list = []
            date_list = []
            date_fixedlist = []
            job_desc_list = []
            job_link_list = []
            job_fixedlink_list = []
            for post in content.select('.job_seen_beacon'):
                jobs_list.append(post.select('.jobTitle')[0].get_text().strip()),
                company_list.append(post.select('.companyName')[0].get_text().strip()),
                location_list.append(post.select('.companyLocation')[0].get_text().strip()),
                date_list.append(post.select('.date')[0].get_text().strip()),
                job_desc_list.append(post.select('div.job-snippet')[0].get_text().strip()),
                job_link_list.append(post.find(class_='jcs-JobTitle', href=True)['href'])

            for date in date_list:
                date_fixedlist.append(date.replace('Posted', '').replace('EmployerActive', ''))

            for job_title in jobs_list:
                jobs_fixedlist.append(job_title.replace('new', ''))

            for links in job_link_list:
                job_fixedlink_list.append('https://www.indeed.com' + links)


            return render_template('indeed_test.html', 
            user_job=user_job, user_location=user_location, 
            job1 = jobs_fixedlist[0], job2 = jobs_fixedlist[1], job3 = jobs_fixedlist[2], job4 = jobs_fixedlist[3], job5 = jobs_fixedlist[4], 
            job6 = jobs_fixedlist[5], job7 = jobs_fixedlist[6], job8 = jobs_fixedlist[7], job9 = jobs_fixedlist[8], job10 = jobs_fixedlist[9], 
            company1 = company_list[0], company2 = company_list[1], company3 = company_list[2], company4 = company_list[3], company5 = company_list[4],
            company6 = company_list[5], company7 = company_list[6], company8 = company_list[7], company9 = company_list[8], company10 = company_list[9],
            loc1 = location_list[0], loc2 = location_list[1], loc3 = location_list[2], loc4 = location_list[3], loc5 = location_list[4],
            loc6 = location_list[5], loc7 = location_list[6], loc8 = location_list[7], loc9 = location_list[8], loc10 = location_list[9],
            date1 = date_fixedlist[0], date2 = date_fixedlist[1], date3 = date_fixedlist[2], date4 = date_fixedlist[3], date5 = date_fixedlist[4],
            date6 = date_fixedlist[5], date7 = date_fixedlist[6], date8 = date_fixedlist[7], date9 = date_fixedlist[8], date10 = date_fixedlist[9],
            desc1 = job_desc_list[0], desc2 = job_desc_list[1], desc3 = job_desc_list[2], desc4 = job_desc_list[3], desc5 = job_desc_list[4],
            desc6 = job_desc_list[5], desc7 = job_desc_list[6], desc8 = job_desc_list[7], desc9 = job_desc_list[8], desc10 = job_desc_list[9],
            link1 = job_fixedlink_list[0], link2 = job_fixedlink_list[1], link3 = job_fixedlink_list[2], link4 = job_fixedlink_list[3], link5 = job_fixedlink_list[4],
            link6 = job_fixedlink_list[5], link7 = job_fixedlink_list[6], link8 = job_fixedlink_list[7], link9 = job_fixedlink_list[8], link10 = job_fixedlink_list[9],
            current_url=current_url)
            
        except:
            return render_template('indeed_test.html', error = True)

@app.route('/about/')
def hello():
    return render_template('about.html')



