from flask import Blueprint, send_file, flash, get_flashed_messages, request
from flask import render_template, redirect, url_for, json, jsonify, make_response, send_from_directory
from os import path
from flask_minify import minify, decorators
from flask_sitemap import Sitemap


views = Blueprint('views', __name__)






#create views
@views.route("/")
@decorators.minify(html=True, js=True, cssless=True)
def home():
    return render_template('home.html')

@views.route("/upload")
@decorators.minify(html=True, js=True, cssless=True)
def up():
    return render_template('upload.html')

####sitemap
@views.route("/sitemap.xml")
def site():
    return render_template('sitemap.xml')

@views.route("/robots.txt")
def robots():
    return render_template('robots.txt')

##home##
@views.route("/error")
@decorators.minify(html=True, js=True, cssless=True)
def error():
    return render_template('404.html')

@views.route("/3a77444deaa3460ab5d78f7190debc5d")
def indexer():
    return render_template('3a77444deaa3460ab5d78f7190debc5d.txt')

@views.route("/3a77444deaa3460ab5d78f7190debc5d")
@decorators.minify(html=True, js=True, cssless=True)
def index():
    return render_template('index.html')
##################YEARS OF STUDY#######################################################
@views.route("/BPAL 1st year")
@decorators.minify(html=True, js=True, cssless=True)
def first():
    return render_template('1select.html')

@views.route("/BPAL 2nd year")
@decorators.minify(html=True, js=True, cssless=True)
def second():
    return render_template('select.html')

@views.route("/BPAL 3rd year")
@decorators.minify(html=True, js=True, cssless=True)
def third():
    return render_template('3select.html')

#4thyr
@views.route("/research")
@decorators.minify(html=True, js=True, cssless=True)
def resea():
    return render_template('research.html')

##########################SEMESTER#################################
@views.route("/1.1")
@decorators.minify(html=True, js=True, cssless=True)
def one():
    return render_template('1sthome.html')

@views.route("/1.2")
@decorators.minify(html=True, js=True, cssless=True)
def oone():
    return render_template('11sthome.html')

@views.route("/2.1")
@decorators.minify(html=True, js=True, cssless=True)
def sec():
    return render_template('2ndhome.html')

@views.route("/2.2")
@decorators.minify(html=True, js=True, cssless=True)
def secc():
    return render_template('22ndhome.html')

@views.route("/3.1")
@decorators.minify(html=True, js=True, cssless=True)
def three():
    return render_template('3rdhome.html')

@views.route("/3.2")
@decorators.minify(html=True, js=True, cssless=True)
def threee():
    return render_template('33rdhome.html')


#########################################################################
@views.route("/project")
@decorators.minify(html=True, js=True, cssless=True)
def proj():
    return render_template('project.html')

@views.route("/pfm")
@decorators.minify(html=True, js=True, cssless=True)
def pfm():
    return render_template('pfm.html')

@views.route("/egov")
@decorators.minify(html=True, js=True, cssless=True)
def egov():
    return render_template('egov.html')

@views.route("/org")
@decorators.minify(html=True, js=True, cssless=True)
def org():
    return render_template('org.html')

@views.route("/crm")
@decorators.minify(html=True, js=True, cssless=True)
def CRM():
    return render_template('crm.html')

@views.route("/corp")
@decorators.minify(html=True, js=True, cssless=True)
def corporate():
    return render_template('corp.html')

@views.route("/marketing")
@decorators.minify(html=True, js=True, cssless=True)
def marketing():
    return render_template('marketing.html')

#@views.route('/download')
#@decorators.minify(html=True, js=True, cssless=True)
#def download_file():
#	path = "egov.pdf"
	#path = "info.xlsx"
	#path = "simple.docx"
	#path = "sample.txt"
#	return send_file(path, as_attachment=True)

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
@decorators.minify(html=True, js=True, cssless=True)
def mis():
    return render_template('mis.html')

@views.route("/negotiation")
@decorators.minify(html=True, js=True, cssless=True)
def negotiation():
    return render_template('n&n.html')

@views.route("/evolution")
@decorators.minify(html=True, js=True, cssless=True)
def evol():
    return render_template('evol.html')

@views.route("/PM")
@decorators.minify(html=True, js=True, cssless=True)
def pm():
    return render_template('PM.html')

@views.route("/HRM")
@decorators.minify(html=True, js=True, cssless=True)
def hrm():
    return render_template('hrm.html')

@views.route("/costaccounting")
@decorators.minify(html=True, js=True, cssless=True)
def ca():
    return render_template('c&m.html')

@views.route("/strategic")
@decorators.minify(html=True, js=True, cssless=True)
def sm():
    return render_template('sm.html')

#############3.2################################

@views.route("/IR")
@decorators.minify(html=True, js=True, cssless=True)
def ir():
    return render_template('ir.html')

@views.route("/TQM")
@decorators.minify(html=True, js=True, cssless=True)
def tqm():
    return render_template('tqm.html')

@views.route("/devolved")
@decorators.minify(html=True, js=True, cssless=True)
def devolved():
    return render_template('dgf.html')

@views.route("/procurement")
@decorators.minify(html=True, js=True, cssless=True)
def proc():
    return render_template('ppp.html')

@views.route("/operations")
@decorators.minify(html=True, js=True, cssless=True)
def oper():
    return render_template('om.html')

@views.route("/economics")
@decorators.minify(html=True, js=True, cssless=True)
def eco():
    return render_template('pse.html')

@views.route("/publicpolicy")
@decorators.minify(html=True, js=True, cssless=True)
def pol():
    return render_template('pp.html')
#############################3.2############################################



##############SEARCH###########################

#@views.route("/search")
#def post_list():
#    q = request.args.get('q')
#    if q:
#        notes = notes.query.filter(Notes.title.contains(q) |
#                Notes.body.contains(q))
#         
#        notes = notes.query.all()
#        return render_template('base.html', notes=notes)
    
