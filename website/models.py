#import db and user
#from . import db
#from flask_login import UserMixin
#from sqlalchemy import func

#class Reminder(db.Model):


#ensure consistent
#class Note(db.Model):
#    id = db.column(db.Integer, primary_key=True)
#    data = db.column(db.String(10000))
#    data = db.column(db.DateTime(timezone=True), default=func.now()) 
    
    #foreign keys#
#    user.id = db.Column(db.Integer, db.ForeignKey('user.id')


#ensure conformity
#class User(db.Model, UserMixin):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String(30), unique=True)
#    password = db.Column(db.String(100))
#    tel = db.Column(db.String(10), unique=True )