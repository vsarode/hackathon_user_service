import django
django.setup()

from flask import Flask
from flask_restful import Api

from user_service.service_apis.Validate import Validate
from user_service.service_apis.ping import Ping
from user_service.service_apis.user import UserHandler
from user_service.service_apis.login import Login
from user_service.service_apis.logout import Logout
from user_service.service_apis.question import Question
from user_service.service_apis.bill import Bill
from user_service.service_apis.connection import Connection
from user_service.service_apis.complaint import Complaint


app = Flask(__name__)
api = Api(app)

api.add_resource(Ping, '/ping')
api.add_resource(UserHandler, '/user', '/user/<string:username>')
api.add_resource(Login, '/login')
api.add_resource(Logout,"/logout")
api.add_resource(Validate, '/validate')
api.add_resource(Connection, '/connection')
api.add_resource(Question,'/question')
api.add_resource(Bill,"/bill")
api.add_resource(Complaint,"/complaint")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
