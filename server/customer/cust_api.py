# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from api.restplus import api
import pymysql
from flask import jsonify
from flask_restplus import Resource
from customer.arguments import customer_arguments
from db_conn import db
ns = api.namespace('customer', description='APIs related to Customer')

@ns.route('/<int:cust_id>')
class CustomerAPI(Resource):
    """
    Customer Resource
    """
    def get(self,cust_id):
        conn = None
        cursor = None
        try:
            conn = db.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id as customer_id, name as customer_name, email as customer_email FROM customers where id=%s",cust_id)
            rows = cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()

   

    def put(self,cust_id):
        conn = None
        cursor = None
        try:
            _name = request.json['name']
            _email = request.json['email']
            conn = db.connect()
            sql="UPdate  customers set name =%s,email=%s where id=%s"
            data = (_name, _email ,cust_id)
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            return 'Success'
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()
@ns.route('/')
class AllCustomerAPI(Resource):
    """
    Customer Resource
    """
    def get(self):
        print("in Get ALl");
        conn = None
        cursor = None
        try:
            conn = db.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id as customer_id , name as customer_name , email as customer_email  FROM customers")
            rows = cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()
            
    @api.expect(customer_arguments)
    def post(self ):
        try:        
            _name = request.json['name']
            _email = request.json['email']
            # validate the received values
            if _name and _email  :
                #do not save password as a plain text
                sql = "INSERT INTO customers(name, email) VALUES(%s, %s)"
                data = (_name, _email)
                conn = db.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                
                return 'Added successfully'
            else:
                return 'Error while adding user'
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()
            return '', 401