from DBPropertyUtil.db_conn import *


class Payment:

    def __init(self, payment_id, lease_id, transaction_date, amount):
        self.connection = get_db_connection()
        self.payment_id = payment_id
        self.lease_id = lease_id
        self.transaction_date = transaction_date
        self.amount = amount

    def __str__(self):
        return f"Payment ID: {self.payment_id}\n" \
               f"Lease ID: {self.lease_id}\n" \
               f"Transaction Date: {self.transaction_date}\n" \
               f"Amount: {self.amount}"