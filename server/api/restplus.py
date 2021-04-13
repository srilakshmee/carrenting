from flask_restplus import Api
from flask import jsonify

api = Api(version='1.0', title='API',
          description='API for Vehicle Renting')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled error occurred. Please try after sometime'
    return {'message': message}, 500


@api.errorhandler(Exception)
def handle_user_exception(error):
    Logger.logr.error('in restplus handle_user_exception')
    print(error.message)
    return { 'message' : error.message} , error.status_code
