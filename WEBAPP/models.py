from . import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    studentName=db.Column(db.String(50),nullable=False)
    schoolName=db.Column(db.String(100),nullable=False)
    studentAge=db.Column(db.Integer,nullable=False)
    studentContactNumber=db.Column(db.Integer,nullable=False,unique=True)
    emailAddress=db.Column(db.String(150),nullable=False,unique=True)
    studentSelectedLocation=db.Column(db.String(10))
    paymentStatus=db.Column(db.Boolean,default=False)   