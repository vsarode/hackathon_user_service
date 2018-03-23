from user_service.db.user_models.models import Connection
from user_service.utils.exceptions import GenericCustomException


def create_connection(request_data):
    consumer_type = request_data['consumerType']
    supply_type = request_data['supplyType']
    survey_number = request_data['surveyNumber']
    society_name = request_data['societyName']
    district = request_data['district']
    pin_code = request_data['pincode']
    try:
        connection_object = Connection.objects.create(
            consumer_type=consumer_type, supply_type=supply_type,
            survey_number=survey_number, society_name=society_name,
            district=district, pincode=pin_code)
        connection_object.customer_id = "MSEB" + str(
            10000 + connection_object.id)
        connection_object.save()
        return connection_object
    except Exception as e:
        print e
        raise GenericCustomException(
            message="Error while creating connection !!")
