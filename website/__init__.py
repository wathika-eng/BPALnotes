from flask import Flask, url_for, send_file, jsonify, make_response, send_from_directory
#from flask_sqlalchemy import SQLAlchemy
from os import path
from datetime import datetime

# database connection details

# create a database object





#create flask app and configure it / DB to models
def create_app():
    app = Flask(__name__)
    # Secret key!
    app.config['SECRET_KEY'] = '****************'
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    # Define DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #initialize DB    
    #db = SQLAlchemy(app)
    
 
    
    
    #import views
    from .views import views
    from .auth import auth
#import DB
#    from .models import User, Note
    #class notes(db.Model):
    #    id = db.Column(db.Integer, primary_key=True)
    #    name = db.Column(db.String(50), nullable=False)
     #   date_added = db.Column(db.DateTime, default=datetime.utcnow)
        
        #create string
      #  def __repr__(self):
      #      return '<Name %r' % self.name

    #register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    


    return app
 

#def create_database(app):
    #if not path.exists('website/' + DB_NAME):
     #   db.create_all(app=app)
      #  print ( 'Database created successfully' )

    