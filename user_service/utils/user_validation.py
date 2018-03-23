from user_service.db.user_models.models import Connection
from user_service.utils.exceptions import UnauthorisedException


def check_is_valid_customer_registration_get_object(customer_id):
    try:
        connection_object = Connection.objects.get(customer_id=customer_id,
                                                   is_valid=True)
        return connection_object
    except:
        raise UnauthorisedException(message="Customer id not valid !!")
