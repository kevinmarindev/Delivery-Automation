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
    starting_address = start_address
    starting_address_idx = address_idx.index(starting_address)
    print("starting idx", starting_address_idx)
    # delivery_address = None
    # print("yes")
    min_distance = float("inf")
    total_distance = 0
    delivery_address_idx = None
    # print("STRTING IT")
    print("STARTING IT =========================")

    while(len(truck.packages)):
        print("outer loop")
        up_next_idx = None
        for package_id in truck.packages:
            # print("========")
            package_address = hash.get(package_id).address
            if(package_address is None): continue
            package_idx = address_idx.index(package_address)
            # print("package id:",package_id, "package address idx:",package_idx, package_address)
            # print("distance to location", distance_matrix[starting_address_idx][package_idx])
            distance_to_package = distance_matrix[starting_address_idx][package_idx]
            # print("CURRENT MIN DISTNCE", min_distance)
            if(distance_to_package < min_distance):
                # print("found one short", package_id)
                min_distance = distance_to_package
                up_next_idx = package_id

        print("DONE LOOKING FOR CLOSEST PACKAGE \n")
        print("shortes distince", min_distance)
        print("package idx", up_next_idx)
        total_distance += min_distance
        truck.packages.remove(up_next_idx)
        min_distance = float("inf")
        # break

    print(truck.packages, len(truck.packages))
    print(total_distance)


deliver(truck3)


    


 # count = 0
    # while(count < len(truck.packages)):
        # start_idx = address_idx.index(starting_address)
        # delivery_idx = address_idx.index(delivery_address)
        #find closest package to deliver next
        # print(hash[truck.packages[count]])
        # print(truck.packages[count])
        # count = count + 1
        # min_distance = 0