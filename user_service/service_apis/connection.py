from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handlers import new_connection_post_handler
from user_service.utils.get_connection_dict_response import \
    get_connection_dict_response


class Connection(Resource):
    def post(self):
        request_data = request.get_json()
        connection_object = new_connection_post_handler.create_connection(
            request_data)
        return jsonify(
            {"Connection1": get_connection_dict_response(connection_object)})
