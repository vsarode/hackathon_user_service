from user_service.db.user_models.models import Complaint


def create_complaint(request_data):
    username = request_data['username']
    complaint_text = request_data['complaint_text']
    try:
        complaint_object = Complaint.objects.create(username=username,
                                                    complaint_text=complaint_text)
        return complaint_object
    except Exception as e:
        print e
        return None
