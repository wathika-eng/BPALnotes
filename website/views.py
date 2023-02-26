from flask import Blueprint, send_file, flash, get_flashed_messages, request
from flask import render_template, redirect, url_for, json, jsonify, make_response, send_from_directory
from os import path


views = Blueprint('views', __name__)

#create views
@views.route("/")
def home():
    return render_template('home.html')

@views.route("/upload")
def up():
    return render_template('upload.html')
##home##
@views.route("/error")
def error():
    return render_template('404.html')
##################YEARS OF STUDY#######################################################
@views.route("/BPAL 1st year")
def first():
    return render_template('1select.html')

@views.route("/BPAL 2nd year")
def second():
    return render_template('select.html')

@views.route("/BPAL 3rd year")
def third():
    return render_template('3select.html')

#4thyr
@views.route("/research")
def resea():
    return render_template('research.html')

##########################SEMESTER#################################
@views.route("/1.1")
def one():
    return render_template('1sthome.html')

@views.route("/1.2")
def oone():
    return render_template('11sthome.html')

@views.route("/2.1")
def sec():
    return render_template('2ndhome.html')

@views.route("/2.2")
def secc():
    return render_template('22ndhome.html')

@views.route("/3.1")
def three():
    return render_template('3rdhome.html')

@views.route("/3.2")
def threee():
    return render_template('33rdhome.html')


#########################################################################
@views.route("/project")
def proj():
    return render_template('project.html')

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

@views.route('/manifest.json')
def manifest():
    return jsonify(manifest.json)

from flask import make_response, send_from_directory
@views.route('/service-worker.js')
def sw():
    response=make_response(
                    send_from_directory('static','/service-worker.js'))
    #change the content header file. Can also omit; flask will handle correctly.
    response.headers['Content-Type'] = 'application/javascript'
    return response

#########################3RD YR#############################################
@views.route("/MIS")
def mis():
    return render_template('mis.html')

@views.route("/negotiation")
def negotiation():
    return render_template('n&n.html')

@views.route("/evolution")
def evol():
    return render_template('evol.html')

@views.route("/PM")
def pm():
    return render_template('PM.html')

@views.route("/HRM")
def hrm():
    return render_template('hrm.html')

@views.route("/costaccounting")
def ca():
    return render_template('c&m.html')

@views.route("/strategic")
def sm():
    return render_template('sm.html')

#############################3.2############################################



##############SEARCH###########################

@views.route("/search")
def post_list():
    q = request.args.get('q')
    if q:
        notes = notes.query.filter(Notes.title.contains(q) |
                Notes.body.contains(q))
         
        notes = notes.query.all()
        return render_template('base.html', notes=notes)
    
