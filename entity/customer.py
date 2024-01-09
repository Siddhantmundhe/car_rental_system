from DBPropertyUtil.db_conn import *

class Customer:

    def __init__(self, customer_id, first_name, last_name, email, phone_number):
        self.connection = get_db_connection()
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"Customer ID: {self.customer_id}\n" \
               f"First Name: {self.first_name}\n" \
               f"Last Name: {self.last_name}\n" \
               f"Email: {self.email}\n" \
               f"Phone Number: {self.phone_number}"