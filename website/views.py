from flask import Blueprint, send_file
from flask import render_template, redirect, url_for
from os import path

views = Blueprint('views', __name__)

#create views
@views.route("/")
def home():
    return render_template('home.html')

##home##
@views.route("/error")
def error():
    return render_template('404.html')

@views.route("/BPAL 1st year")
def first():
    return render_template('1st.html')

@views.route("/BPAL 2nd year")
def second():
    return render_template('2ndhome.html')

@views.route("/BPAL 3rd year")
def third():
    return render_template('3rdhome.html')

#4thyr
@views.route("/research")
def resea():
    return render_template('research.html')


@views.route("/pfm")
def pfm():
    return render_template('pfm.html')

@views.route("/egov")
def egov():
    return render_template('egov.html')

@views.route("/org")
def org():
    return render_template('org.html')

@views.route("/crm")
def CRM():
    return render_template('crm.html')

@views.route("/corp")
def corporate():
    return render_template('corp.html')

@views.route("/marketing")
def marketing():
    return render_template('marketing.html')

@views.route('/download')
def download_file():
	path = "egov.pdf"
	#path = "info.xlsx"
	#path = "simple.docx"
	#path = "sample.txt"
	return send_file(path, as_attachment=True)