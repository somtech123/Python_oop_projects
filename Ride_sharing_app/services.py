
from ride import Ride
from payment import Payment


class RideService:
    def __init__(self):
        self.rides = []
        self.drivers = []
        self.payments = []

    def register_driver(self, driver):
        self.drivers.append(driver)

    def find_available_driver(self):
        for driver in self.drivers:
            if driver.available:
                return driver
        return None
    
    def show_payment(self):
        for payment in self.payments:
            print(payment)

    def show_rides(self):
        for ride in self.rides:
            print(ride)

    def create_ride(self, rider, origin, destination, fare, processor):
        ride = Ride(rider, origin, destination, fare)
        driver = self.find_available_driver()



        if driver:
            driver.accept_ride(ride)
        #process payment
        payment = Payment(ride.ride_id, fare, processor)
        result = payment.process_payment()
        ride.payment = payment
        self.payments.append(payment)

        self.rides.append(ride)
        print(result)
        return ride
