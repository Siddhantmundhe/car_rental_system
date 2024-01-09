from DBPropertyUtil.db_conn import get_ids, get_cnts
from entity.customer import Customer
from entity.vehicle import Vehicle
from entity.lease import Lease
from datetime import date
from dao.customer_manager import CustomerManager
from dao.vehicle_manager import VehicleManager
from dao.lease_manager import LeaseManager
from dao.payment_manager import PaymentManager
from my_exceptions.my_exceptions import InvalidDateException


def print_menu():
    print("\nCar Rental System Menu:")
    print("1. Customer Management")
    print("2. Vehicle Management")
    print("3. Lease Management")
    print("4. Payment Management")
    print("0. Exit")

def customer_menu(customer_manager):
    while True:
        print("\nCustomer Management Menu:")
        print("1. Add New Customer")
        print("2. Update Customer Info")
        print("3. Get Customer Details by ID")
        print("4. List All Customers")
        print("5. Remove Customer")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone_number = input("Enter Phone Number: ")
            customer_manager.add_new_customer(first_name, last_name, email, phone_number)

        elif choice == "2":
            customer_id = input("Enter Customer ID: ")
            first_name = input("Enter New First Name (leave empty to skip): ")
            last_name = input("Enter New Last Name (leave empty to skip): ")
            email = input("Enter New Email (leave empty to skip): ")
            phone_number = input("Enter New Phone Number (leave empty to skip): ")
            customer_manager.update_customer_info(customer_id, first_name, last_name, email, phone_number)

        elif choice == "3":
            customer_id = input("Enter Customer ID: ")
            customer_manager.get_customer_details(customer_id)

        elif choice == "4":
            customer_manager.list_customers()

        elif choice == "5":
            customer_id = input("Enter Customer ID: ")
            customer_manager.remove_customer(customer_id)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def vehicle_menu(vehicle_manager):
    while True:
        print("\nVehicle Management Menu:")
        print("1. Add New Vehicle")
        print("2. Remove Vehicle")
        print("3. List Available Vehicles")
        print("4. List Rented Vehicles")
        print("5. Find Vehicle by ID")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            daily_rate = input("Enter Daily Rate: ")
            status = input('Enter vehicle status available/notAvailable: ')
            passenger_capacity = input("Enter Passenger Capacity: ")
            engine_capacity = input("Enter Engine Capacity: ")
            vehicle_manager.add_vehicle(get_ids('vehicle', 'vehicleID'), make, model, year, daily_rate, status, passenger_capacity, engine_capacity)

        elif choice == "2":
            vehicle_id = input("Enter Vehicle ID: ")
            vehicle_manager.remove_vehicle(vehicle_id)

        elif choice == "3":
            available_vehicles = vehicle_manager.list_available_vehicles()
            print("Available Vehicles:")
            for vehicle in available_vehicles:
                print(vehicle.make)

        elif choice == "4":
            rented_vehicles = vehicle_manager.list_rented_vehicles()
            print("Rented Vehicles:")
            for vehicle in rented_vehicles:
                print(vehicle.make)

        elif choice == "5":
            vehicle_id = input("Enter Vehicle ID: ")
            vehicle = vehicle_manager.find_vehicle_by_id(vehicle_id)
            if vehicle:
                print("Found Vehicle:")
                print(vehicle)
            else:
                print(f"Vehicle with ID {vehicle_id} not found.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def lease_menu(lease_manager):
    while True:
        print("\nLease Management Menu:")
        print("1. Create Lease")
        print("2. Return Vehicle")
        print("3. List Active Leases")
        print("4. List Lease History")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                customer_id = input("Enter Customer ID: ")
                vehicle_id = input("Enter Vehicle ID: ")
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                lease_type = input("Enter Lease Type Daily/Monthly: ")
                lease_manager.create_lease(vehicle_id, customer_id,start_date, end_date, lease_type)
            except InvalidDateException as ide:
                print(f"Error: {ide}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == "2":
            lease_id = input("Enter Lease ID: ")
            lease_manager.return_vehicle(lease_id)

        elif choice == "3":
            active_leases = lease_manager.list_active_leases()
            print("Active Leases:")
            for lease in active_leases:
                print(lease)

        elif choice == "4":
            lease_history = lease_manager.list_lease_history()
            print("Lease History:")
            for lease in lease_history:
                print(lease)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def payment_menu(payment_manager, lease_manager):
    while True:
        print("\nPayment Management Menu:")
        print("1. Record Payment")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            lease_id = input("Enter Lease ID: ")
            amount = input("Enter Payment Amount: ")
            lease = get_cnts('lease', 'leaseID', lease_id)

            if lease > 0:
                payment_manager.record_payment(lease_id, amount)
            else:
                print(f"Lease with ID {lease_id} not found.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    customer_manager = CustomerManager()
    vehicle_manager = VehicleManager()
    lease_manager = LeaseManager()
    payment_manager = PaymentManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_menu(customer_manager)
        elif choice == "2":
            vehicle_menu(vehicle_manager)
        elif choice == "3":
            lease_menu(lease_manager)
        elif choice == "4":
            payment_menu(payment_manager, lease_manager)
        elif choice == "0":
            print("Thank You For Showing Interest In  The Car Rental System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()