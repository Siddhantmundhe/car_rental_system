import unittest
from my_exceptions.my_exceptions import CustomerNotFoundException, VehicleNotFoundException, \
    LeaseNotFoundException
from dao.lease_manager import LeaseManager
from dao.vehicle_manager import VehicleManager
from dao.payment_manager import PaymentManager
from dao.customer_manager import CustomerManager



class TestCarRentalSystem(unittest.TestCase):
    def setUp(self):
        self.lease_manager = LeaseManager()
        self.vehicle_manager = VehicleManager()
        self.payment_manager = PaymentManager()
        self.customer_manager = CustomerManager()


    def test_exception_customer_not_found(self):
        with self.assertRaises(CustomerNotFoundException):
            self.customer_manager.get_customer_by_id(15)

    def test_exception_vehicle_not_found(self):
        with self.assertRaises(VehicleNotFoundException):
            self.vehicle_manager.find_vehicle_by_id(20)

    def test_exception_lease_not_found(self):
        with self.assertRaises(LeaseNotFoundException):
            self.lease_manager.get_lease_by_id(20)

    def test_create_vehicle_success(self):
        make = 'Toyota'
        model = 'Camry'
        year = 2022
        daily_rate = 50.0
        status = 'available'
        passenger_capacity = 5
        engine_capacity = 2500

        vehicle_id = self.vehicle_manager.add_vehicle(self, make, model, year, daily_rate, status, passenger_capacity, engine_capacity)

        self.assertIsInstance(vehicle_id, int)
        self.assertGreater(vehicle_id, 0)

    def test_create_lease_success(self):
        customer_id = 1
        vehicle_id = 10
        start_date = '2023-12-26'
        end_date = '2023-12-31'
        lease_type = 'Daily'

        lease_id = self.lease_manager.create_lease(
            customer_id, vehicle_id, start_date, end_date, lease_type
        )

        self.assertIsInstance(lease_id, int)
        self.assertGreater(lease_id, 0)





if __name__ == '__main__':
    unittest.main()