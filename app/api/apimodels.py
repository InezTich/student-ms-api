
from marshmallow import fields,validate
from flask_marshmallow import Marshmallow
not_blank = validate.Length(min=1,error="Field can't blank")

ma=Marshmallow()

class AddStudentValidator(ma.Schema):
    fname = fields.String(required=True,validate=not_blank)
    sname = fields.String(required=True,validate=not_blank)
    email = fields.Email(required=True,validate=not_blank)
    username = fields.String(required=True,validate=not_blank)
    student_class = fields.String(required=True,validate=not_blank)



class AdminRegiserValidator(ma.Schema):
    username = fields.String(required=True,validate=not_blank)
    passwd = fields.String(required=True,validate=not_blank)
    email = fields.String(required=True,validate=not_blank)
    fname = fields.String(required=True,validate=not_blank)
    sname = fields.String(required=True,validate=not_blank)
    # rupdate = fields.String(required=True,validate=not_blank)


class AdminLoginWithEmail(ma.Schema):
    username = fields.String(required=True,validate=not_blank)
    passwd = fields.String(required=True,validate=not_blank)
