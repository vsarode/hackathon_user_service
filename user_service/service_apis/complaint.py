from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handlers import complaint_post_handler


class Complaint(Resource):
    def post(self):
            request_data = request.get_json()
            complaint_object = complaint_post_handler.create_complaint(request_data)
            if complaint_object:
                return jsonify({"Complaint": "succcess"})

            else:
                return {"success": False}
