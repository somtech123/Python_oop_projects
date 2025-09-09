from services import RideService
from user import Rider, Driver
from vehicle import Car, Bike
from payment_processor import PayPalPaymentProcessor, StripePaymentProcessor, CryptoPaymentProcessor


class FrontEndRunner:

    def run(self):
        services = RideService()

        #register drivers

        d1= Driver('D1','Alice', Car('Toyota Corolla','CVI123'))
        d2 =  Driver('D2','Alice', Bike('Yamaha','ABC123'))

        services.register_driver(d1)
        services.register_driver(d2)

        #Riders
        r1 = Rider('R1','Dre')
        r2 = Rider('R2', 'JOHN')

        #request ride with diffrent payment methods
        ride1 = r1.request_ride(services, 'Downtown', 'Airport',60, StripePaymentProcessor())
        print(ride1)

        ride2 = r2.request_ride(services, 'Mall', 'Plateau',90, CryptoPaymentProcessor())
        print(ride2)

        ride3 = r1.request_ride(services, 'Station', 'Markrt',60, PayPalPaymentProcessor())
        print(ride3)


        print(ride1.complete_ride())

        print('\nAll Rides')
        services.show_rides()

        print('\nAll payments')
        services.show_payment()



