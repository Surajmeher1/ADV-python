import time

parking = {}
total_spots = 5

def available_spots():
    print("Available spots:", total_spots - len(parking))


def vehicle_entry():
    if len(parking) >= total_spots:
        print("Parking Full!")
        return

    vehicle_no = input("Enter vehicle number: ")
    entry_time = time.time()
    parking[vehicle_no] = entry_time
    print("Vehicle parked successfully")


def vehicle_exit():
    vehicle_no = input("Enter vehicle number: ")

    if vehicle_no not in parking:
        print("Vehicle not found!")
        return

    exit_time = time.time()
    entry_time = parking[vehicle_no]

    parked_hours = (exit_time - entry_time) / 3600
    fee = max(1, int(parked_hours)) * 20   # ₹20 per hour

    print("Parking fee:", fee)
    del parking[vehicle_no]


def show_vehicles():
    if not parking:
        print("No vehicles parked")
    else:
        for v in parking:
            print("Vehicle:", v)


while True:
    print("\n===== Parking Lot Management =====")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Show Parked Vehicles")
    print("4. Available Spots")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vehicle_entry()
    elif choice == "2":
        vehicle_exit()
    elif choice == "3":
        show_vehicles()
    elif choice == "4":
        available_spots()
    elif choice == "5":
        print("Program closed")
        break
    else:
        print("Invalid choice")