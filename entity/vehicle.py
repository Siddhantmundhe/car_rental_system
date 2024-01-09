from DBPropertyUtil.db_conn import *


class Vehicle:

    def __init__(self, vehicle_id, make, model, year, daily_rate, status, passenger_capacity, engine_capacity):
        self.connection = get_db_connection()
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.status = status
        self.passenger_capacity = passenger_capacity
        self.engine_capacity = engine_capacity

    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id}\n" \
               f"Make: {self.make}\n" \
               f"Model: {self.model}\n" \
               f"Year: {self.year}\n" \
               f"Daily Rate: {self.daily_rate}\n" \
               f"Status: {self.status}\n" \
               f"Passenger Capacity: {self.passenger_capacity}\n" \
               f"Engine Capacity: {self.engine_capacity}"