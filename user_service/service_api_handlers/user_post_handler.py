from user_service.db.user_models.models import User
from user_service.utils.exceptions import GenericCustomException
from user_service.utils.user_validation import \
    check_is_valid_customer_registration_get_object


def create_user(request_data):
    username = request_data['username']
    customerID = request_data['customerID']
    password = request_data['password']
    phone = request_data['phone']
    connection_object = check_is_valid_customer_registration_get_object(
        customerID)
    try:
        user_object = User.objects.create(username=username,
                                          cunnection=connection_object,
                                          password=password, phone=phone)
        return user_object
    except Exception as e:

        raise GenericCustomException(message="Error while creating user !!")
