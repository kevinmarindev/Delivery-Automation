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


from classes import Package, Hash_table, Truck
from packages import deliveries
from helpers import address_idx, distance_matrix

hash =  Hash_table()

for package in deliveries:
    hash.insert(package.id, package)


truck3 = Truck(1, [2,5,7,8,10,11,17,21,22,23,24,26,27,33,35,39])


def deliver(truck: Truck, start_address="4001 South 700 East"):
    starting_address_idx = address_idx.index(start_address)
    # print("starting idx", starting_address_idx)
    total_distance = 0

    while(len(truck.packages)):
        print("PACKAGES LEFT:", len(truck.packages))
        up_next_location_idx = None
        min_distance = float("inf")

        for package_id in truck.packages:
            package_address = hash.get(package_id).address

            if(package_address is None): continue
            up_next_location_idx = address_idx.index(package_address)
            distance_to_package = distance_matrix[starting_address_idx][up_next_location_idx]

            if(distance_to_package < min_distance):
                min_distance = distance_to_package
                up_next_idx = package_id

        print("DONE LOOKING FOR CLOSEST PACKAGE")
        print("shortes distince", min_distance)
        print("package idx", up_next_idx)
        total_distance += min_distance
        truck.packages.remove(up_next_idx)
        min_distance = float("inf")
        starting_address_idx = up_next_location_idx
        print("\n")


    print(truck.packages, len(truck.packages))
    print(total_distance)


deliver(truck3)
