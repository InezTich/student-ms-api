
from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt, jwt_required
from app.api.apimodels import AdminLoginWithEmail, AdminRegiserValidator  
from marshmallow.exceptions import ValidationError
from app.appclass.admins_class import AdminsClass
class AdminbRegister(Resource): 
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'status': 2, 'message': 'Invalid request'}, 400
        
        try:
            AdminRegiserValidator().load(json_data)

        except ValidationError as e:
            print(e)
            return {'status':2, 'message': 'Error found', 'code': 400}
        
        Admin=AdminsClass()
        respone = Admin.AdminsRegister(
            fname=json_data['fname'],
            sname=json_data['sname'],
            email=json_data['email'],
            passwd=json_data['passwd'],
            username=json_data['username'],
            # rupdate=json_data['rupdate']
        )
        return respone,respone['code']
    
class AdminLogin(Resource): 
    def post(self):
        json_data = request.get_json()

        if not json_data:
            return {'status': 2, 'message': 'Invalid request'}, 400
        
        try:
            AdminLoginWithEmail().load(json_data)

        except ValidationError as e:
            print(e)
            return {'status':2, 'message': 'Error found', 'code': 400}
        
        Admin = AdminsClass()
        respone = Admin.AdminLogin(json_data['username'],json_data['passwd'])
        return respone,respone['code']
    
class AdminLogout(Resource):
    @jwt_required()
    def post(self):
        jit = get_jwt()['jti']
        print(" JTI is ",jit)
        Admin = AdminsClass()
        respone = Admin.AdminLogOut(jit)
        return respone,respone['code']
