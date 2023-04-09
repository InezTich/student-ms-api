from app import db
from sqlalchemy import DateTime,func

class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(50),nullable=False)
    sname=db.Column(db.String(50),nullable=False)
    username=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    student_class=db.Column(db.String(50),nullable=False)
    last_updated=db.Column(DateTime(timezone=True),onupdate=func.now(),nullable=True)


class Admins(db.Model):
    __tablename__='admins'
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(50),nullable=False)
    sname=db.Column(db.String(50),nullable=False)
    username=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    passwd=db.Column(db.String(100),nullable=False)
    rupdate=db.Column(db.DateTime,nullable=False,default=func.now())

class TokenBlockList(db.Model): 
    __tablename__='token_blocklist'
    id=db.Column(db.Integer,primary_key=True)
    jit=db.Column(db.String(255),nullable=False)
    created_at=db.Column(db.DateTime,nullable=False)


