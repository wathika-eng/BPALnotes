from flask import Flask
from flask import routes

@app.route('/download')
def download_file():
	path = "egov.pdf"
	#path = "info.xlsx"
	#path = "simple.docx"
	#path = "sample.txt"
	return send_file(path, as_attachment=True)