#Project for the program called Carfinder
def load_vehicles_from_file():
    try:
        with open("C:\_python file\COP1000\Project\AllowedVehicleList.txt", 'r') as file:
            vehicles = [line.strip() for line in file.readlines()]
        return vehicles
    except FileNotFoundError:
        print("Error: C:\_python file\COP1000\Project\AllowedVehicleList.txt not found.")
        return []

def save_vehicle_to_file(vehicle_name):
    with open("C:\_python file\COP1000\Project\AllowedVehicleList.txt", 'a') as file:
        file.write(f"{vehicle_name}\n")
        
def remove_vehicle_from_file(vehicle_name):
    vehicles = load_vehicles_from_file()
    vehicles.remove(vehicle_name)
    with open("C:\_python file\COP1000\Project\AllowedVehicleList.txt", 'w') as file:
        for vehicle in vehicles:
            file.write(f"{vehicle}\n")
            
def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

def print_vehicles(vehicles):
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in vehicles:
        print(vehicle)

def search_vehicle(vehicles, vehicle_name):
    if vehicle_name in vehicles:
        print(f"{vehicle_name} is an authorized vehicle")
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def add_vehicle(vehicles, vehicle_name):
    if vehicle_name not in vehicles:
        vehicles.append(vehicle_name)
        save_vehicle_to_file(vehicle_name)
        print(f'You have added "{vehicle_name}" as an authorized vehicle')
    else:
        print(f'"{vehicle_name}" is already an authorized vehicle')
        
def delete_vehicle(vehicles, vehicle_name):
    if vehicle_name in vehicles:
        confirmation = input(f'Are you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? (yes/no)\n')
        if confirmation.lower() == 'yes':
            vehicles.remove(vehicle_name)
            remove_vehicle_from_file(vehicle_name)
            print(f'You have REMOVED "{vehicle_name}" as an authorized vehicle')
        else:
            print(f'"{vehicle_name}" was not removed')
    else:
        print(f'"{vehicle_name}" is not an authorized vehicle')

def main():
    vehicles = load_vehicles_from_file()
    
    while True:
        print_menu()
        choice = input()
        if choice == '1':
            print_vehicles(vehicles)
        elif choice == '2':
            vehicle_name = input("Please Enter the full Vehicle name:\n")
            search_vehicle(vehicles, vehicle_name)
        elif choice == '3':
            vehicle_name = input("Please Enter the full Vehicle name you would like to add:\n")
            add_vehicle(vehicles, vehicle_name)
        elif choice == '4':
            vehicle_name = input("Please Enter the full Vehicle name you would like to remove:\n")
            delete_vehicle(vehicles, vehicle_name)     
        elif choice == '5':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()