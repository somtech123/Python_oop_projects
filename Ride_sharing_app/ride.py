import uuid
class Ride:
    def __init__(self, rider, origin: str, destination: str, fare: float):
        self.ride_id = str(uuid.uuid4())[:8]
        self.rider = rider
        self.origin = origin
        self.destination = destination
        self.fare = fare
        self.payment = None
        self.status = 'REQUESTED'
        self.driver = None


    def assign_driver(self, driver):
        self.driver = driver
        self.status = 'ONGOING'

    
    def complete_ride(self):
        if self.driver:
            self.status = 'COMPLETED'
            self.driver.available = True
            return f'Ride {self.ride_id} completed by {self.driver.name}'
        return 'No driver assigned'
    
    def __repr__(self):
        return f'<Ride {self.ride_id} | {self.rider.name} -> {self.destination} | Fare {self.fare} | {self.status}'
    



