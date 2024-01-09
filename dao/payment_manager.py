from DBPropertyUtil.db_conn import *
from datetime import date , timedelta

class PaymentManager:
    def __init__(self):
        self.connection = get_db_connection()

    def record_payment(self, lease_id, amount):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            INSERT INTO Payment(paymentID, leaseID, transactionDate, amount)
            VALUES (%s, %s, %s, %s)
            '''
            para = (get_ids('payment', 'paymentID') ,lease_id, date.today(), amount)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Payment recorded successfully.')

        except Exception as e:
            print('An error occurred: ', e)