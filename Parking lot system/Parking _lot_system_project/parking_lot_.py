from parking_classes import (
    Car,
    ParkingLot,
    ParkingFullError,
    SpotOccupiedError,
    VehicleNotFoundError
)


def main():
    parking_lot = ParkingLot(3)

    while True:
        print("\n===== PARKING LOT SYSTEM =====")
        print("1. Park a car")
        print("2. Check out a car")
        print("3. Show parking spots")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                plate = input("Enter plate number: ")
                owner = input("Enter owner name: ")
                seats = int(input("Enter number of seats: "))

                car = Car(plate, owner, seats)
                spot_number = parking_lot.park_vehicle(car)

                print(
                    f"Car parked successfully in "
                    f"spot {spot_number}."
                )

            elif choice == "2":
                plate = input("Enter plate number: ")
                hours = int(input("Enter hours parked: "))

                if hours <= 0:
                    print("Hours must be greater than zero.")
                    continue

                vehicle, fee, spot_number = (
                    parking_lot.checkout(plate, hours)
                )

                print("\nCheck-out complete!")
                print(
                    f"Vehicle: Car ({vehicle.plate_number})"
                )
                print(f"Owner: {vehicle.owner_name}")
                print(f"Hours: {hours}")
                print(f"Fee: ${fee:.2f}")
                print(f"Spot {spot_number} is now free.")

            elif choice == "3":
                parking_lot.show_spots()

            elif choice == "4":
                print("Thank you for using our system!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ParkingFullError as error:
            print(f"Sorry, {error}")

        except SpotOccupiedError as error:
            print(f"Sorry, {error}")

        except VehicleNotFoundError as error:
            print(f"Sorry, {error}")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()