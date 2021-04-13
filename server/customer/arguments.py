from flask_restplus import fields
from api.restplus import api
import json

customer_arguments = api.model('customer',{
     'name': fields.String(required=True, description='name'),
    'email': fields.String(required=True, description='email')
    });