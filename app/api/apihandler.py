from flask import Blueprint,request
from flask_restful import Api, Resource
from app.api.resources.student_ms import AddStudent,FetchStudentData,FetchSingleStudentData,FetchStudentPagination,ManageStudentData
from app.api.resources.admin_ms import AdminLogout, AdminbRegister,AdminLogin
apiviews = Blueprint('apiview',__name__)

api = Api(apiviews)

    

api.add_resource(AddStudent,'/addStudent')
api.add_resource(FetchStudentData,'/fetchStudent')
api.add_resource(FetchSingleStudentData,'/fetchStudent/<string:username>')
api.add_resource(FetchStudentPagination,'/fetchStudentPagination/<int:page>')
api.add_resource(ManageStudentData,'/manageStudent/<string:username>')

# Admin Endpoint

api.add_resource(AdminbRegister,'/register')
api.add_resource(AdminLogin,'/login')
api.add_resource(AdminLogout,'/logout')