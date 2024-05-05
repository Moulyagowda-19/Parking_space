class ParkingSpace:
    def __init__(self):
        self.slots = [None] * 20

    def park_vehicle(self, vehicle_number):
        for i in range(len(self.slots)):
            if self.slots[i] is None:
                self.slots[i] = vehicle_number
                print(f"Vehicle with number {vehicle_number} parked in slot {i+1}.")
                return
        print("Sorry, parking space is full.")

    def exit_vehicle(self, vehicle_number):
        if vehicle_number in self.slots:
            slot = self.slots.index(vehicle_number)
            self.slots[slot] = None
            print(f"Vehicle with number {vehicle_number} exited from slot {slot+1}.")
        else:
            print("Vehicle not found in parking space.")

def main():
    parking_space = ParkingSpace()

    while True:
        action = input("Do you want to park or exit a vehicle? (park/exit/quit): ").lower()

        if action == "park":
            vehicle_number = input("Enter the vehicle number: ")
            parking_space.park_vehicle(vehicle_number)
        elif action == "exit":
            vehicle_number = input("Enter the vehicle number: ")
            parking_space.exit_vehicle(vehicle_number)
        elif action == "quit":
            print("Exiting the parking system.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
