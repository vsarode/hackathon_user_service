def get_connection_dict_response(connection_object):
    print connection_object
    print "Hackathon...."
    response_dict = {'consumerType': connection_object.consumer_type,
                     'supplyType': connection_object.supply_type,
                     'surveyNumber': connection_object.survey_number,
                     'societyName': connection_object.society_name,
                     'district': connection_object.district,
                     'pincode': connection_object.pincode,
                     'customerId': connection_object.customer_id
                     }

    return response_dict
