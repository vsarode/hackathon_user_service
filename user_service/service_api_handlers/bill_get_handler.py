from datetime import datetime

from user_service.db.user_models.models import BillingEntry


def get_bill_for_user(username):
    pending_bills = BillingEntry.objects.filter(user__username=username,
                                                is_paid=False)
    last_bill = None
    for bill in pending_bills:
        if bill.month.month == datetime.now().month:
            last_bill = pending_bills
    return last_bill
