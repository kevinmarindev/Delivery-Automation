# Kevin Marin, Student ID: 012688692,  Delivery algorithm

from classes import Package, Hash_table, Truck, DeliveryManager, User_interface
from packages import deliveries, truck1, truck2, truck3
from helpers import address_idx, distance_matrix
from datetime import datetime, timedelta

hash =  Hash_table()

for package in deliveries:
    hash.insert(package.id, package)


manager = DeliveryManager(hash, address_idx, distance_matrix)
manager.deliver(truck1, time=datetime.strptime("08:00", "%H:%M"))
manager.deliver(truck2, time=datetime.strptime("10:13", "%H:%M"))
manager.deliver(truck3, time=datetime.strptime("08:00", "%H:%M"))
print("delivery time of package1:", hash.get(1).delivery_time)


User_interface(manager).main()

