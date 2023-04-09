
from app import db
from app.models import Student

class StudentClass():
    def AddStudent(self,data):
        ''' This method will add a new student to database '''
        ''' Check to ensure incoming registeration email data does not exist already '''

        CheckEmailAndUser = db.session.query(Student.username)\
            .filter((Student.email==data['email']) | (Student.username==data['username'])).first()
        
        if CheckEmailAndUser:
            return  {'status': 2, 'message': 'Username or Email already registered', 'code':409 }
        else:
            try:
                newStudent=Student()
                newStudent.fname=data['fname']
                newStudent.sname=data['sname']
                newStudent.email=data['email']
                newStudent.username=data['username'] 
                newStudent.student_class=data['student_class']
                db.session.add(newStudent)
                db.session.commit() # save data to database
            
            except Exception as e:
                ## log to file here
                print(e)
                return {"status": 2, "message": f"an error occured while adding {data['fname']} {data['sname']} to student table", "code": 500}
            else:
                return {"status":1, "message": f"You have successfully added {data['fname']} {data['sname']} to student table", "code": 200}

    def FetchAllStudent(self):
        ''' This method will fetch all student data from database '''

        try:
            AllStudent = db.session.query(Student.fname,Student.sname,Student.email,Student.username).all()
        except Exception as e:
            return {"status": 2, "message": "An occured while fetching students","code": 500}
            
        else:
            all_student=[]
            if not AllStudent:
                return {"status": 2, "message": "No student found", "code": 404}
            else:
                for i in AllStudent:
                    ## query
                    all_student.append(i._asdict())

                return {"status": 1, "message": "All student successfully returned", "data": all_student, "code": 200}

    def FetchSingleStudent(self,username):
        ''' This method will return single student '''
        try:
            SingleStudent = db.session.query(Student.fname,Student.sname,Student.email,Student.username)\
            .filter(Student.username == username).first() 
        except Exception as e:
            return {"status": 2, "message": f"An occured while fetching single student","code": 500}
        else:
            if not SingleStudent:
                return {"status": 2, "message": "No student found","code": 404}
            else:
                return {"status": 1, "message": "Student founded", "data": SingleStudent._asdict(), "code": 200 }
            
    def FetchWithPage(self,page, perpage):
        ''' This method will fetch all student data from database with pagination '''

        try:
            print("start here ===>>>>") 

            AllStudent = db.session.query(Student.fname,Student.sname,Student.email,Student.username)\
            .order_by(Student.id.desc())\
            .paginate(page=page,per_page=perpage,error_out=False)

            print(AllStudent)
        except Exception as e:
            return {"status": 2, "message": "An occured while fetching students","code": 500}
            
        else:
            all_student=[]
            if not AllStudent:
                return {"status": 2, "message": "No student found", "code": 404}
            else:
                for i in AllStudent.items:
                    ## query
                    all_student.append(i._asdict())

                return {"status": 1, "message": "All student successfully returned", "data": all_student, "code": 200}
            

    def UpdateStudentData(self,data,username):
        checkUser = db.session.query(Student.username).filter(Student.username==username).first()
        if not checkUser:
            return {"status" : 2, "message" : "No student found", "code" : 404}
        else:
            try:
                Student.query.filter_by(username=username).update(data)
                db.session.commit()

            except Exception as e:
                print(e)
                return {'status':2, 'message':'Error found','code':500}
            else:
                return {'status':1,'message':'Record update successfully','code':200}
            
    def DeleteStudentData(self,username):
        checkUser = db.session.query(Student.username).filter(Student.username==username).first()
        if not checkUser:
            return {"status" : 2, "message" : "No student found", "code" : 404}
        else:
            try:
                Student.query.filter_by(username=username).delete()
                db.session.commit()

            except Exception as e:
                print(e)
                return {'status':2, 'message':'Error found','code':500}
            else:
                return {'status':1,'message':'Record update successfully','code':200}
            