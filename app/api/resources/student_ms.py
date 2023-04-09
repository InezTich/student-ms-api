from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from marshmallow.utils import INCLUDE
from app.api.apimodels import AddStudentValidator
from app.appclass.student_class import StudentClass

class AddStudent(Resource):
    @jwt_required()
    def get(self):
        print("Here 1")
        return {'status': 1, 'message': 'get method worked!'}
    
    def post(self): 
        json_data = request.get_json()
        print(json_data)
        if not json_data:
            return {'status':2, 'message': 'invalid request!'},400
        
        try:
            AddStudentValidator().load(json_data)
        except ValidationError as err:
            return {"status": 'Errror here'}
        
        # save to database
        newStudent=StudentClass()
        response=newStudent.AddStudent(json_data)
        return response,response['code']
    
class FetchStudentData(Resource):
    @jwt_required()
    def get(self):
        GetStudent = StudentClass()
        respone = GetStudent.FetchAllStudent()
        return respone, respone['code']
    

class FetchSingleStudentData(Resource):
    @jwt_required()
    def get(self,**kwargs):
        print("I'm here >>>>>>>>>>>>")
        GetStudent = StudentClass()
        print(GetStudent)
        username = kwargs.get('username')
        print(username)
        respone = GetStudent.FetchSingleStudent(username)
        return respone,respone['code']
    

class FetchStudentPagination(Resource):
    @jwt_required()
    def get(self,**kwargs):
        page = kwargs.get('page')
        print("I'm Here ===> ",page)
        per_page = 4
        GetStudent = StudentClass()
        respone = GetStudent.FetchWithPage(page,per_page)
        return respone,respone['code']
    
class ManageStudentData(Resource):
    @jwt_required()
    def put(self,**kwargs):
        username = kwargs.get('username') 
        json_data = request.get_json()
        if not json_data:
            return {"status": 2, "message" : "Invalid Request"},400
        
        UpdateStudent = StudentClass()
        respone = UpdateStudent.UpdateStudentData(json_data,username)
        return respone, respone['code']
    
    def delete(self,**kwargs):
        username = kwargs.get('username')
        deleteStudent = StudentClass()
        respone = deleteStudent.DeleteStudentData(username)
        return respone,respone['code']

