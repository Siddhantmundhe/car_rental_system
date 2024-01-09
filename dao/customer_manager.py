from DBPropertyUtil.db_conn import *
from entity.customer import Customer
from my_exceptions.my_exceptions import *


class CustomerManager:

    def __init__(self):
        self.connection = get_db_connection()

    def add_new_customer(self, first_name, last_name, email, phone_number):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                INSERT INTO Customer(customerID, firstName, lastName, email, phoneNumber)
                VALUES (%s, %s, %s, %s, %s)
                '''

            para = (get_ids('customer', 'customerID'), first_name, last_name, email, phone_number)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Customer Added Successfully')
        except Exception as e:
            print('An error occurred: ', e)


    def update_customer_info(self, customer_id, first_name=None, last_name=None, email=None, phone_number=None):
        try:
            my_cursor = self.connection.cursor()

            if first_name:
                sql = '''
                UPDATE Customer SET firstName = %s WHERE customerID = %s
                '''
                para = (first_name, customer_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('First Name updated successfully')

            if last_name:
                sql = '''
                UPDATE Customer SET lastName = %s WHERE customerID = %s
                '''
                para = (last_name, customer_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Last Name updated successfully')

            if email:
                sql = '''
                UPDATE Customer SET email = %s WHERE customerID = %s
                '''
                para = (email, customer_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Email updated successfully')

            if phone_number:
                sql = '''
                UPDATE Customer SET phoneNumber = %s WHERE customerID = %s
                '''
                para = (phone_number, customer_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Phone Number updated successfully')

            print('Customer Details updated successfully')

        except Exception as e:
            print('An error occurred: ', e)

    def get_customer_details(self, customer_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * FROM Customer WHERE customerID = %s
            '''
            para = (customer_id,)
            my_cursor.execute(sql, para)
            x = list(my_cursor.fetchone())
            print(*x, sep=',')
        except Exception as e:
            print('An error occurred: ', {e})

    def get_customer_by_id(self, customer_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * FROM Customer WHERE customerID = %s
            '''
            para = (customer_id,)
            my_cursor.execute(sql, para)
            temp = my_cursor.fetchone()

            if temp is None:
                raise CustomerNotFoundException('Invalid Customer ID')
            x = Customer(*temp)
            return x
        except CustomerNotFoundException as cnfe:
            raise cnfe
        except Exception as e:
            print('An error occurred: ', {e})

    def list_customers(self):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * FROM Customer
            '''
            my_cursor.execute(sql)
            x = [list(i) for i in my_cursor.fetchall()]
            print(*x, sep='\n')
        except Exception as e:
            print('An error occurred: ', {e})

    def remove_customer(self, customer_id):
        try:
            my_cursor = self.connection.cursor()
            x = get_cnts('customer', 'customerID', customer_id)

            if x == 0:
                raise CustomerNotFoundException('Enter a valid Customer ID')

            sql = '''
                SELECT * FROM Lease WHERE customerID = %s AND CURDATE() BETWEEN startDate AND endDate
            '''
            para = (customer_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()

            if x is not None:
                print('Lease already exists cannot delete the customer')
                return
            sql_b = '''DELETE FROM Lease WHERE customerID = %s'''
            sql = '''DELETE FROM Customer WHERE customerID = %s'''
            para = (customer_id,)
            my_cursor.execute(sql_b, para)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Customer Removed Successfully')
        except CustomerNotFoundException as e:
            print('An error occurred: ', e)
        except Exception as e:
            print('An error occurred: ', e)