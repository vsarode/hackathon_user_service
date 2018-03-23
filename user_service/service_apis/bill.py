from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handlers import bill_post_handler, \
    bill_get_handler
from user_service.utils.billing_entry_method import get_dict_for_bill_object


class Bill(Resource):
    def post(self):
        request_data = request.get_json()
        bill_object = bill_post_handler.bill_entry(request_data)
        if bill_object:
            return jsonify(get_dict_for_bill_object(bill_object))
        else:
            return {"success": False}

    def get(self):
        request_data = request.agrs
        pending_bill = bill_get_handler.get_bill_for_user(
            request_data['username'])
        return jsonify({"bill":get_dict_for_bill_object(pending_bill)})



    def put(self):
        pass

