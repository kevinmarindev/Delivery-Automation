# Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the hash table:

# •   delivery address

# •   delivery deadline

# •   delivery city

# •   delivery zip code

# •   package weight

# •   delivery status (i.e., at the hub, en route, or delivered), including the delivery time


# B.  Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:

# •   delivery address

# •   delivery deadline

# •   delivery city

# •   delivery zip code

# •   package weight

# •   delivery status (i.e., at the hub, en route, or delivered), including the delivery time


import math
from classes import Package, Hash_table, Truck
from packages import deliveries
from helpers import address_idx, distance_matrix
from datetime import datetime, timedelta

hash =  Hash_table()

for package in deliveries:
    hash.insert(package.id, package)


truck1 = Truck(1, [1,7,10,13,14,15,16,19,20,21,29,30,34,37,39,40])
truck2 = Truck(2, [3,6,8,9,11,12,17,18,22,23,24,27,33,35,36,38])
truck3 = Truck(3, [2,4,5,25,26,28,31,32])


def deliver(truck: Truck, start_address="4001 South 700 East", time=datetime.strptime("08:00", "%H:%M")):
    starting_address_idx = address_idx.index(start_address)
    # print("starting idx", starting_address_idx)
    total_distance = 0

    while(len(truck.packages)):
        print("PACKAGES LEFT:", len(truck.packages))
        print(truck.packages)
        up_next_location_idx = None
        up_next_package_id = None
        min_distance = float("inf")
        print("Total distance traveled so far:", total_distance)

        for package_id in truck.packages:
            # package_address = hash.get(package_id).address
            package = hash.get(package_id)
            if(package.address is None): continue
            target_address = address_idx.index(package.address)
            distance_to_package = distance_matrix[starting_address_idx][target_address]

            if(distance_to_package < min_distance):
                min_distance = distance_to_package
                up_next_package_id = package_id
                up_next_location_idx = target_address

        print("DONE LOOKING FOR CLOSEST PACKAGE")
        print("shortes distince", min_distance)
        print("package ID:", up_next_package_id)
        total_distance += min_distance
        
        delivery_package = hash.get(up_next_package_id)
        print("DELIVERING PACKAGE TO:", delivery_package.address)
        delivery_package.delivery_status = "delivered"
        time += timedelta(minutes= math.ceil((min_distance / 18) * 60))  # Assuming average speed of 18 mph
        print("ARRIVAL TIME:", time.strftime("%H:%M"))
        truck.packages.remove(up_next_package_id)


        min_distance = float("inf")
        starting_address_idx = up_next_location_idx
        print("\n")


    print(truck.packages, len(truck.packages))
    print(total_distance)


deliver(truck2, time=datetime.strptime("09:40", "%H:%M"))
