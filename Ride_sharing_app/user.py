class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name



class Driver(User):
    def __init__(self, user_id, name, vehicle):
        super().__init__(user_id, name)
        self.vehicle = vehicle
        self.available = True

    def accept_ride(self, ride):
        if self.available:
            ride.assign_driver(self)
            self.available = False
            return f'{self.name} accepted ride '
        return f'{self.name} is not available'
    

class Rider(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.ride_history = []

    def request_ride(self, service, origin, destination, fare, processor):
        ride = service.create_ride(self, origin, destination, fare, processor)
        self.ride_history.append(ride)
        return ride
