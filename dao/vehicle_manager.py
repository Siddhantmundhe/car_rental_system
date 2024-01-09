from DBPropertyUtil.db_conn import *
from entity.vehicle import Vehicle
from my_exceptions.my_exceptions import *


class VehicleManager:
    def __init__(self):
        self.connection = get_db_connection()

    def add_vehicle(self,vehicleID, make, model, year, daily_rate, status, passenger_capacity, engine_capacity):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            INSERT INTO Vehicle(vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            '''
            para = (
                get_ids('vehicle', 'vehicleID'),
                make,
                model,
                year,
                daily_rate,
                status,
                passenger_capacity,
                engine_capacity
            )
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Vehicle Added Successfully')
            return 1
        except Exception as e:
            print('An error occurred: ', e)

    def remove_vehicle(self, vehicle_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Lease WHERE vehicleID = %s AND CURDATE() BETWEEN startDate AND endDate
            '''
            para = (vehicle_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()

            if x is not None:
                print('Vehicle is currently rented ')
                return

            a = get_cnts('vehicle', 'vehicleID', vehicle_id)

            if a == 0:
                print('Invalid vehicle ID/vehicle does not exist')
                return

            sql2 = '''
                DELETE FROM Vehicle WHERE vehicleID = %s
            '''
            para = (vehicle_id,)
            my_cursor.execute(sql2, para)
            self.connection.commit()
            print('Vehicle removed successfully')
        except Exception as e:
            print('An error occurred: ', e)

    def list_available_vehicles(self):
        try:
            my_cursor = self.connection.cursor()
            sql = '''SELECT * FROM Vehicle WHERE status = %s'''
            para = ('Available',)
            my_cursor.execute(sql, para)
            vehicles = [Vehicle(*row) for row in my_cursor.fetchall()]
            return vehicles
        except Exception as e:
            print('An error occurred: ', e)

    def list_rented_vehicles(self):
        try:
            my_cursor = self.connection.cursor()
            sql = '''SELECT * FROM Vehicle WHERE status = %s'''
            para = ('notAvail',)
            my_cursor.execute(sql, para)
            vehicles = [Vehicle(*row) for row in my_cursor.fetchall()]
            return vehicles
        except Exception as e:
            print('An error occurred: ', e)

    def find_vehicle_by_id(self, vehicle_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''SELECT * FROM Vehicle WHERE vehicleID = %s'''
            para = (vehicle_id,)
            my_cursor.execute(sql, para)
            row = my_cursor.fetchone()
            if row:
                return Vehicle(*row)
            else:
                raise VehicleNotFoundException('Invalid Vehicle ID entered')
        except VehicleNotFoundException as vnfe:
            raise vnfe
        except Exception as e:
            print('An error occurred: ', e)