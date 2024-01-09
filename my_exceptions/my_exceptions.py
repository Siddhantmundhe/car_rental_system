class VehicleNotFoundException(Exception):
    def __init__(self, message="Vehicle not found"):
        self.message = message
        super().__init__(self.message)

class LeaseNotFoundException(Exception):
    def __init__(self, message="Lease not found"):
        self.message = message
        super().__init__(self.message)

class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found"):
        self.message = message
        super().__init__(self.message)

class InvalidDateException(Exception):
    def __init__(self, message="Start date cannot be a past date"):
        self.message = message
        super().__init__(self.message)
