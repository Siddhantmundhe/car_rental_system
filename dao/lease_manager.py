from DBPropertyUtil.db_conn import *
from entity import vehicle
from entity.lease import Lease
from my_exceptions.my_exceptions import *
from datetime import datetime

from datetime import datetime

class LeaseManager:
    # ... (other methods remain the same)

    def create_lease(self, vehicle_id, customer_id, start_date, end_date, lease_type):
        try:
            current_date = datetime.now().date()

            # Convert start_date to datetime.date if it's a string
            if isinstance(start_date, str):
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()

            if start_date < current_date:
                raise InvalidDateException('Start date cannot be a past date.')

            my_cursor = self.connection.cursor()
            sql = '''
            INSERT INTO Lease(leaseID, vehicleID, customerID, startDate, endDate, leasetype)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            para = (get_ids('lease', 'leaseID'), vehicle_id, customer_id, start_date, end_date, lease_type)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Lease created successfully')
            return 1
        except InvalidDateException as ide:
            raise ide
        except Exception as e:
            print('An error occurred: ', e)


    def return_vehicle(self, lease_id):
        try:
            my_cursor = self.connection.cursor()
            sql1 = '''
            SELECT vehicleID FROM Lease WHERE leaseID = %s AND CURDATE() BETWEEN startDate AND endDate
            '''
            para1 = (lease_id,)
            my_cursor.execute(sql1, para1)
            x = my_cursor.fetchone()[0]

            if x is None:
                print('Invalid Lease ID')
                return

            sql2 = '''
                UPDATE Vehicle SET status = 'available' WHERE vehicleID = %s
            '''
            para2 = (x,)
            my_cursor.execute(sql2, para2)
            self.connection.commit()
            print('Car returned successfully')
        except Exception as e:
            print('An error occurred: ', e)

    def list_active_leases(self):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Lease WHERE CURDATE() BETWEEN startDate AND endDate
            '''
            my_cursor.execute(sql)
            leases = [Lease(*row) for row in my_cursor.fetchall()]
            return leases

        except Exception as e:
            print('An error occurred: ', e)

    def list_lease_history(self):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Lease
            '''
            my_cursor.execute(sql)
            leases = [Lease(*row) for row in my_cursor.fetchall()]
            return leases

        except Exception as e:
            print('An error occurred: ', e)

    def get_lease_by_id(self, lease_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''SELECT * FROM Lease WHERE leaseID = %s'''
            para = (lease_id,)
            my_cursor.execute(sql, para)
            row = my_cursor.fetchone()
            if row:
                return Lease(*row)
            else:
                raise LeaseNotFoundException('Invalid Lease ID entered')
        except LeaseNotFoundException as lnfe:
            raise lnfe
        except Exception as e:
            print('An error occurred: ', e)