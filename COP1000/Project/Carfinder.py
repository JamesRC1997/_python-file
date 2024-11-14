#Project for the program called Carfinder
AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
def search_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
        print(f"{vehicle_name} is an authorized vehicle")
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")
def add_vehicle(vehicle_name):
    if vehicle_name not in AllowedVehiclesList:
        AllowedVehiclesList.append(vehicle_name)
        print(f'You have added "{vehicle_name}" as an authorized vehicle')
    else:
        print(f'"{vehicle_name}" is already an authorized vehicle')

def main():
    while True:
        print_menu()
        choice = input()
        if choice == '1':
            print_vehicles()
        elif choice == '2':
            vehicle_name = input("Please Enter the full Vehicle name:\n")
            search_vehicle(vehicle_name)
        elif choice == '3':
            vehicle_name = input("Please Enter the full Vehicle name you would like to add:\n")
            add_vehicle(vehicle_name)       
        elif choice == '4':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()