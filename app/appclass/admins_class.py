
from datetime import datetime, timedelta, timezone

from flask_jwt_extended import create_access_token
from app.models import Admins, TokenBlockList
from app import db
import hashlib
from werkzeug.security import generate_password_hash,check_password_hash
class AdminsClass():

    @staticmethod
    def AdminsRegister(**kwargs):
        ''' use this method to create an Admin '''

        print("Track 1 here!!")
        admin = db.session.query(Admins)\
        .filter((Admins.email==kwargs.get('email')) | (Admins.username==kwargs.get('username'))).first()
        print("Track 2 here!!")
        if admin:
            return {'status': 2, 'message': 'Admin already exist!', 'code': 200}
        try:
            print("Track 3 here!!")
            newAdmin = Admins()
            newAdmin.fname=kwargs.get('fname')
            newAdmin.sname=kwargs.get('sname')
            newAdmin.email=kwargs.get('email')
            newAdmin.username=kwargs.get('username')
            # newAdmin.passwd=kwargs.get('passwd')
            # newAdmin.rupdate=kwargs.get('rupdate')
            newAdmin.passwd=generate_password_hash(kwargs.get('passwd'),method='pbkdf2:sha1', salt_length=8)
            db.session.add(newAdmin)
            db.session.commit()
            print("Track 4 here!!")

            
        except Exception as e:
            print(e)
            return {'status': 1, 'message': 'An error occured', 'code':500}
        
        else:
            return {'status': 1, 'message': 'Admin have successfully registered', 'code':200}
        
    @staticmethod
    def AdminLogin(username,passwd):
        ''' This method will authenticate the admin '''
        user = db.session.query(Admins.fname,Admins.sname,Admins.username,Admins.email,Admins.id,Admins.passwd)\
        .filter(Admins.username==username).first()
        if user and check_password_hash(user.passwd,passwd):
            expires = timedelta(minutes=10)
            userClaim = {
                'fname': user.fname,
                'sname': user.sname,
                'email': user.email
            }
            accessToken = create_access_token(
                identity = user.id,
                fresh    = True,
                expires_delta  = expires,
                additional_claims = userClaim
            )
            return {'status' : 1, 'message' : 'Login was successfully!!','access_token' : accessToken, 'code' : 200}
        else:
            return {'status' : 2, 'message' : 'Invalid username or password!!', 'code' : 400}

    @staticmethod
    def AdminLogOut(jit):
        try:
            now = datetime.now(timezone.utc)
            db.session.add(TokenBlockList(jit=jit,created_at=now))
            db.session.commit()

        except Exception as e:
            print(e)
            return {'status' : 2, 'message' : 'logout error!!', 'code' : 500}
        
        else:
            return {'status': 1, 'message' : 'logout successfully', 'code' : 200}