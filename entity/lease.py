from DBPropertyUtil.db_conn import *


class Lease:

    def __init__(self, lease_id, vehicle_id, customer_id, start_date, end_date, lease_type):
        self.connection = get_db_connection()
        self.lease_id = lease_id
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.start_date = start_date
        self.end_date = end_date
        self.lease_type = lease_type

    def __str__(self):
        return f"Lease ID: {self.lease_id}\n" \
               f"Vehicle ID: {self.vehicle_id}\n" \
               f"Customer ID: {self.customer_id}\n" \
               f"Start Date: {self.start_date}\n" \
               f"End Date: {self.end_date}\n" \
               f"Type: {self.lease_type}"