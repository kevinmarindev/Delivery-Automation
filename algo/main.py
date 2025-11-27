# Kevin Marin, Student ID: 012688692,  Delivery algorithm

#Main script file runs the actual program. entry point

from classes import Hash_table, DeliveryManager, User_interface
from packages import deliveries, truck1, truck2, truck3
from helpers import address_idx, distance_matrix
from datetime import datetime

#create hash table using the custom hash class
hash =  Hash_table()

#add packages to hash table
for package in deliveries:
    hash.insert(package.id, package)

#create an instance of the delivery manager class to manage everything related to deliveries.
manager = DeliveryManager(hash, address_idx, distance_matrix)
#set out trucks to deliver
manager.deliver(truck1, time=datetime.strptime("08:00", "%H:%M"))
    #truck 2 does not leave until the driver of truck one returns to hub which is at 10:13
manager.deliver(truck2, time=datetime.strptime("10:13", "%H:%M"))
manager.deliver(truck3, time=datetime.strptime("08:00", "%H:%M"))

#give the user an interface to obtain delivery and package information
User_interface(manager).main()

