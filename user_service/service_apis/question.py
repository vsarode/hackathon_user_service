from flask import request
from flask_restful import Resource

from user_service.service_api_handlers import question_post_handler, user_get_handler


class Question(Resource):
    def post(self):
        request_data = request.get_json()
        user_object = user_get_handler.get_single_user(request_data)

        if not user_object:
            return  {"success":False,"message":"Invalid user"}

        question_object=question_post_handler.verifie(request_data)
        if not question_object:
            question_object = question_post_handler.create_question(request_data, user_object)
            print "hello"


