class ParkingFullError(Exception):
    pass


class SpotOccupiedError(Exception):
    pass


class VehicleNotFoundError(Exception):
    pass


class Vehicle:
    def __init__(self, plate_number, owner_name):
        self.plate_number = plate_number
        self.owner_name = owner_name


class Car(Vehicle):
    def __init__(self, plate_number, owner_name, seats):
        super().__init__(plate_number, owner_name)
        self.seats = seats


class ParkingSpot:
    def __init__(self, spot_number):
        self.spot_number = spot_number
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def park(self, vehicle):
        if not self.is_available():
            raise SpotOccupiedError("This spot is occupied!")

        self.vehicle = vehicle

    def remove(self):
        if self.is_available():
            raise VehicleNotFoundError("This spot is empty!")

        vehicle = self.vehicle
        self.vehicle = None
        return vehicle


class ParkingLot:
    def __init__(self, capacity):
        self.spots = [
            ParkingSpot(i)
            for i in range(1, capacity + 1)
        ]

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if (
                spot.vehicle is not None
                and spot.vehicle.plate_number
                == vehicle.plate_number
            ):
                raise SpotOccupiedError(
                    "This plate number is already parked!"
                )

        for spot in self.spots:
            if spot.is_available():
                spot.park(vehicle)
                return spot.spot_number

        raise ParkingFullError("The parking lot is full!")

    def find_vehicle(self, plate_number):
        for spot in self.spots:
            if (
                spot.vehicle is not None
                and spot.vehicle.plate_number == plate_number
            ):
                return spot

        raise VehicleNotFoundError(
            "Plate number not found!"
        )

    def checkout(self, plate_number, hours):
        spot = self.find_vehicle(plate_number)
        vehicle = spot.remove()
        fee = hours * 2

        return vehicle, fee, spot.spot_number

    def show_spots(self):
        for spot in self.spots:
            if spot.is_available():
                print(f"Spot {spot.spot_number}: Available")
            else:
                print(
                    f"Spot {spot.spot_number}: "
                    f"Occupied by "
                    f"{spot.vehicle.plate_number}"
                )