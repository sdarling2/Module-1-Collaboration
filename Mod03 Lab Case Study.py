# Mod03 Lab_Case Study: Lists, Functions, and Classes
# Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")  # vehicle type is always "car"
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Main program
def main():
    print("Enter vehicle information:\n")
    
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    
    # Validate doors input
    while True:
        doors = input("Number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        print("Please enter 2 or 4.")
    
    # Validate roof input
    while True:
        roof = input("Type of roof (solid or sun roof): ").lower()
        if roof in ["solid", "sun roof"]:
            break
        print("Please enter 'solid' or 'sun roof'.")
    
    # Create object
    car = Automobile(year, make, model, doors, roof)
    
    # Output
    print("\nVehicle Information:")
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")


# Run the program
if __name__ == "__main__":
    main()