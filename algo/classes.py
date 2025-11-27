from datetime import datetime, timedelta
import math

# class to represent truck objects
class Truck:
    def __init__(self, id, packages=[]):
        self.id = id
        self.packages = packages
        self.departure_time = None

# custom class to represent a package
class Package:
    def __init__(self, id, address, deadline, city, zip, weight, delivery_status=None, delivery_time:datetime=None, truck: Truck=None):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time
        self.truck = truck

#custom hash table class uses linear chaining to prevent hash collisions 
class Hash_table:
    def __init__(self, hash_size=40):
        self.table = [[] for _ in range(hash_size)]
        self.hash_size = hash_size

    def hash(self, id):
        return id % self.hash_size
    
    def insert(self, id, package: Package):
        idx = self.hash(id)
        self.table[idx].append(package)
    
    def get(self, id):
        idx = self.hash(id)
        if(len(self.table[idx])):
            for package in self.table[idx]:
                if package.id == id:
                    return package
            return None
        else:
            return None



#Custom class that manages everything related to deliveries 
class DeliveryManager:
    def __init__(self, hash_table, address_idx, distance_matrix):
        self.hash = hash_table
        self.address_idx = address_idx
        self.distance_matrix = distance_matrix
        self.total_distance = 0.0

    #starts deliveries for a specific truck
    def deliver(self, truck: Truck, start_address="4001 South 700 East", time=datetime.strptime("08:00", "%H:%M")):
        starting_address_idx = self.address_idx.index(start_address)
        truck.departure_time = time
        total_distance = 0

        while len(truck.packages):
            up_next_location_idx = None
            up_next_package_id = None
            min_distance = float("inf")

            for package_id in truck.packages:
                package = self.hash.get(package_id)
                if package.address is None:
                    continue
                target_address = self.address_idx.index(package.address)
                distance_to_package = self.distance_matrix[starting_address_idx][target_address]

                if distance_to_package < min_distance:
                    min_distance = distance_to_package
                    up_next_package_id = package_id
                    up_next_location_idx = target_address

            total_distance += min_distance
            delivery_package = self.hash.get(up_next_package_id)
            delivery_package.delivery_status = "delivered"
            time += timedelta(minutes=math.ceil((min_distance / 18) * 60))
            delivery_package.delivery_time = time
            truck.packages.remove(up_next_package_id)
            starting_address_idx = up_next_location_idx

        return_to_hub_distance = self.distance_matrix[starting_address_idx][0]
        total_distance += return_to_hub_distance
        time += timedelta(minutes=math.ceil((return_to_hub_distance / 18) * 60))
        self.total_distance += total_distance
        return total_distance
    

    #prints the total distance covered delivering all packages
    def total_distance_traveled(self):
        return self.total_distance
    
    #prints the status of a package at a specific time
    def package_status_at_time(self, package_id: int, time: datetime):
        target_package = self.hash.get(package_id)
        if(target_package == None):
            print("Package not found.")
            return
        if(target_package.truck.departure_time is None or time < target_package.truck.departure_time):
            print("Status: at the hub")

        elif(time >= target_package.truck.departure_time):
            if(target_package.delivery_time is None or time < target_package.delivery_time):
                print("Status: en route")
            else:
                print(f"Status: delivered at {target_package.delivery_time.strftime('%H:%M')}")

    #prints the statuses of all packages in each truck
    def all_package_statuses(self, query_time: datetime):
        print("package id 40:", self.hash.get(40).address)
        print(f"TRUCK 1 PACKAGE STATUSES @: {query_time.strftime('%H:%M')}")
        for i in range(1, self.hash.hash_size + 1):
            package = self.hash.get(i)
            if package and package.truck.id == 1:
                print("Package ID:", package.id, package.address)
                self.package_status_at_time(package.id, query_time)
                print("\n")
        
        
        print(f"TRUCK 2 PACKAGE STATUSES @: {query_time.strftime('%H:%M')}")
        for i in range(1, self.hash.hash_size + 1):
            package = self.hash.get(i)
            if package and package.truck.id == 2:
                print("Package ID:", package.id, package.address)
                self.package_status_at_time(package.id, query_time)
                print("\n")

        print(f"TRUCK 3 PACKAGE STATUSES @: {query_time.strftime('%H:%M')}")
        for i in range(1, self.hash.hash_size + 1):
            package = self.hash.get(i)
            if package and package.truck.id == 3:
                print("Package ID:", package.id, package.address)
                self.package_status_at_time(package.id, query_time)
                print("\n")


#custom class that allows users to interact with the program main method serves as the entry point to the application
class User_interface:
    def __init__(self, delivery_manager: DeliveryManager):
        self.total_distance = 0
        self.delivery_manager = delivery_manager

    def main(self):
        print("Welcome to the WGUPS package delivery system.")
        print("Select an option:")
        print("1. View package status at a specific time")
        print("2. View total mileage traveled by all trucks")
        print("3. View all package statuses")
        print("4. Exit")

        user_input = None
        while input != "4":
            user_input = input("Enter your choice (1-4): ")
            if user_input == "1":
                package_id = int(input("Enter package ID: "))
                time_str = input("Enter time (HH:MM): ")
                query_time = datetime.strptime(time_str, "%H:%M")
                self.delivery_manager.package_status_at_time(package_id, query_time)
            elif user_input == "2":
                print(f"Total mileage traveled by all trucks: {self.delivery_manager.total_distance_traveled()} miles")
            elif user_input == "3":
                time_str = input("Enter time (HH:MM): ")
                query_time = datetime.strptime(time_str, "%H:%M")
                self.delivery_manager.all_package_statuses(query_time)
            elif user_input == "4":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


   

    

        



