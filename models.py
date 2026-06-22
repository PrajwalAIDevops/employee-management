
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Employee(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 name=db.Column(db.String(100))
 email=db.Column(db.String(120))
 phone=db.Column(db.String(20))
 department=db.Column(db.String(100))
 designation=db.Column(db.String(100))
 salary=db.Column(db.Float)
 doj=db.Column(db.Date)
