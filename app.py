#imports#
from website import create_app
from flask import Flask
from flask_minify import minify

app = Flask(__name__)

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)
    app.run(host = '0.0.0.0', port =5000)
    # initializing minify for html, js and cssless
    minify(app=app, html=True, js=True, cssless=True, fail_safe=True)
    
    
#Admin panel
