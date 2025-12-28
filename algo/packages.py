from classes import Package, Truck

truck1 = Truck(1, [1,7,10,13,14,15,16,19,20,21,29,30,34,37,39,40])
truck2 = Truck(2, [3,8,9,11,12,17,18,22,23,24,26,27,33,35,36,38])
truck3 = Truck(3, [2,4,5,6,25,28,31,32])

deliveries = [
    Package(1, "195 W Oakland Ave", "10:30 AM", "Salt Lake City", "84115", 21.0, "at the hub", truck=truck1),
    Package(2, "2530 S 500 E", "EOD", "Salt Lake City", "84106", 44.0, "at the hub", truck=truck3),
    Package(3, "233 Canyon Rd", "EOD", "Salt Lake City", "84103", 2.0, "at the hub", truck=truck2),
    Package(4, "380 W 2880 S", "EOD", "Salt Lake City", "84115", 4.0, "at the hub", truck=truck3),
    Package(5, "410 S State St", "EOD", "Salt Lake City", "84111", 5.0, "at the hub", truck=truck3),
    Package(6, "3060 Lester St", "10:30 AM", "West Valley City", "84119", 88.0, "awaiting", truck=truck3),
    Package(7, "1330 2100 S", "EOD", "Salt Lake City", "84106", 8.0, "at the hub", truck=truck1),
    Package(8, "300 State St", "EOD", "Salt Lake City", "84103", 9.0, "at the hub", truck=truck2),
    Package(9, "300 State St", "EOD", "Salt Lake City", "84103", 2.0, "at the hub", truck=truck2),
    Package(10, "600 E 900 South", "EOD", "Salt Lake City", "84105", 1.0, "at the hub", truck=truck1),
    Package(11, "2600 Taylorsville Blvd", "EOD", "Salt Lake City", "84118", 1.0, "at the hub", truck=truck2),
    Package(12, "3575 W Valley Central Station bus Loop", "EOD", "West Valley City", "84119", 1.0, "at the hub", truck=truck2),
    Package(13, "2010 W 500 S", "10:30 AM", "Salt Lake City", "84104", 2.0, "at the hub", truck=truck1),
    Package(14, "4300 S 1300 E", "10:30 AM", "Millcreek", "84117", 88.0, "at the hub", truck=truck1),
    Package(15, "4580 S 2300 E", "9:00 AM", "Holladay", "84117", 4.0, "at the hub", truck=truck1),
    Package(16, "4580 S 2300 E", "10:30 AM", "Holladay", "84117", 88.0, "at the hub", truck=truck1),
    Package(17, "3148 S 1100 W", "EOD", "Salt Lake City", "84119", 2.0, "at the hub", truck=truck2),
    Package(18, "1488 4800 S", "EOD", "Salt Lake City", "84123", 6.0, "at the hub", truck=truck2),
    Package(19, "177 W Price Ave", "EOD", "Salt Lake City", "84115", 37.0, "at the hub", truck=truck1),
    Package(20, "3595 Main St", "10:30 AM", "Salt Lake City", "84115", 37.0, "at the hub", truck=truck1),
    Package(21, "3595 Main St", "EOD", "Salt Lake City", "84115", 3.0, "at the hub", truck=truck1),
    Package(22, "6351 South 900 East", "EOD", "Murray", "84121", 2.0, "at the hub", truck=truck2),
    Package(23, "5100 South 2700 West", "EOD", "Salt Lake City", "84118", 5.0, "at the hub", truck=truck2),
    Package(24, "5025 State St", "EOD", "Murray", "84107", 7.0, "at the hub", truck=truck2),
    Package(25, "5383 South 900 East #104", "10:30 AM", "Salt Lake City", "84117", 7.0, "awaiting", truck=truck3),
    Package(26, "5383 South 900 East #104", "EOD", "Salt Lake City", "84117", 25.0, "at the hub", truck=truck2),
    Package(27, "1060 Dalton Ave S", "EOD", "Salt Lake City", "84104", 5.0, "at the hub", truck=truck2),
    Package(28, "2835 Main St", "EOD", "Salt Lake City", "84115", 7.0, "awaiting", truck=truck3),
    Package(29, "1330 2100 S", "10:30 AM", "Salt Lake City", "84106", 2.0, "at the hub", truck=truck1),
    Package(30, "300 State St", "10:30 AM", "Salt Lake City", "84103", 1.0, "at the hub", truck=truck1),
    Package(31, "3365 S 900 W", "10:30 AM", "Salt Lake City", "84119", 1.0, "at the hub", truck=truck3),
    Package(32, "3365 S 900 W", "EOD", "Salt Lake City", "84119", 1.0, "awaiting", truck=truck3),
    Package(33, "2530 S 500 E", "EOD", "Salt Lake City", "84106", 1.0, "at the hub", truck=truck2),
    Package(34, "4580 S 2300 E", "10:30 AM", "Holladay", "84117", 2.0, "at the hub", truck=truck1),
    Package(35, "1060 Dalton Ave S", "EOD", "Salt Lake City", "84104", 88.0, "at the hub", truck=truck2),
    Package(36, "2300 Parkway Blvd", "EOD", "West Valley City", "84119", 88.0, "at the hub", truck=truck2),
    Package(37, "410 S State St", "10:30 AM", "Salt Lake City", "84111", 2.0, "at the hub", truck=truck1),
    Package(38, "410 S State St", "EOD", "Salt Lake City", "84111", 9.0, "at the hub", truck=truck2),
    Package(39, "2010 W 500 S", "EOD", "Salt Lake City", "84104", 9.0, "at the hub", truck=truck1),
    Package(40, "380 W 2880 S", "10:30 AM", "Salt Lake City", "84115", 45.0, "at the hub", truck=truck1)
]

