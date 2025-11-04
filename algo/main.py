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
from helpers import address_idx

hash =  Hash_table()

for package in deliveries:
    hash.insert(package.id, package)


truck3 = Truck(1, [2,5,7,8,10,11,17,21,22,23,24,26,27,33,35,39])


def deliver(truck: Truck, start_address="4001 South 700 East"):
    starting_address = start_address
    delivery_address = None
    print("yes")
    print(truck3.packages)
    for package_id in truck3.packages:
        print("ok")
        print(hash.get(package_id).address) 
        # package_adress = hash[package_id]
        # print(package_adress)



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