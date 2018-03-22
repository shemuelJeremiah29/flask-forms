from . import db  
import datetime
from sqlalchemy import DateTime 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname=db.Column(db.String(80)) 
    email = db.Column(db.String(120), unique=True)  
    location=db.Column(db.String(900)) 
    gender=db.Column(db.String (50))
    biography= db.Column(db.String(500)) 
    created_on = db.Column(DateTime, default=datetime.datetime.utcnow) 
     
    
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False 
        
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support


    
    def __repr__(self):
        return '<User %r>' % (self.id)