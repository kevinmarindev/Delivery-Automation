from classes import Package


# 1	195 W Oakland Ave	Salt Lake City	UT	84115	10:30 AM	21
# 2	2530 S 500 E	Salt Lake City	UT	84106	EOD	44
# 3	233 Canyon Rd	Salt Lake City	UT	84103	EOD	2
# 4	380 W 2880 S	Salt Lake City	UT	84115	EOD	4
# 5	410 S State St	Salt Lake City	UT	84111	EOD	5
# 6	3060 Lester St	West Valley City	UT	84119	10:30 AM	88
# 7	1330 2100 S	Salt Lake City	UT	84106	EOD	8
# 8	300 State St	Salt Lake City	UT	84103	EOD	9
# 9	300 State St	Salt Lake City	UT	84103	EOD	2
# 10	600 E 900 South	Salt Lake City	UT	84105	EOD	1
# 11	2600 Taylorsville Blvd	Salt Lake City	UT	84118	EOD	1
# 12	3575 W Valley Central Station bus Loop	West Valley City	UT	84119	EOD	1
# 13	2010 W 500 S	Salt Lake City	UT	84104	10:30 AM	2
# 14	4300 S 1300 E	Millcreek	UT	84117	10:30 AM	88
# 15	4580 S 2300 E	Holladay	UT	84117	9:00 AM	4
# 16	4580 S 2300 E	Holladay	UT	84117	10:30 AM	88
# 17	3148 S 1100 W	Salt Lake City	UT	84119	EOD	2
# 18	1488 4800 S	Salt Lake City	UT	84123	EOD	6
# 19	177 W Price Ave	Salt Lake City	UT	84115	EOD	37
# 20	3595 Main St	Salt Lake City	UT	84115	10:30 AM	37
# 21	3595 Main St	Salt Lake City	UT	84115	EOD	3
# 22	6351 South 900 East	Murray	UT	84121	EOD	2
# 23	5100 South 2700 West	Salt Lake City	UT	84118	EOD	5
# 24	5025 State St	Murray	UT	84107	EOD	7
# 25	5383 South 900 East #104	Salt Lake City	UT	84117	10:30 AM	7
# 26	5383 South 900 East #104	Salt Lake City	UT	84117	EOD	25
# 27	1060 Dalton Ave S	Salt Lake City	UT	84104	EOD	5
# 28	2835 Main St	Salt Lake City	UT	84115	EOD	7
# 29	1330 2100 S	Salt Lake City	UT	84106	10:30 AM	2
# 30	300 State St	Salt Lake City	UT	84103	10:30 AM	1
# 31	3365 S 900 W	Salt Lake City	UT	84119	10:30 AM	1
# 32	3365 S 900 W	Salt Lake City	UT	84119	EOD	1
# 33	2530 S 500 E	Salt Lake City	UT	84106	EOD	1
# 34	4580 S 2300 E	Holladay	UT	84117	10:30 AM	2
# 35	1060 Dalton Ave S	Salt Lake City	UT	84104	EOD	88
# 36	2300 Parkway Blvd	West Valley City	UT	84119	EOD	88
# 37	410 S State St	Salt Lake City	UT	84111	10:30 AM	2
# 38	410 S State St	Salt Lake City	UT	84111	EOD	9
# 39	2010 W 500 S	Salt Lake City	UT	84104	EOD	9
# 40	380 W 2880 S	Salt Lake City	UT	84115	10:30 AM	45


deliveries = [
    Package(1, "195 W Oakland Ave", "10:30 AM", "Salt Lake City", "84115", 21.0, "at hub"),
    Package(2, "2530 S 500 E", "EOD", "Salt Lake City", "84106", 44.0, "at hub"),
    Package(3, "233 Canyon Rd", "EOD", "Salt Lake City", "84103", 2.0, "at hub"),
    Package(4, "380 W 2880 S", "EOD", "Salt Lake City", "84115", 4.0, "at hub"),
    Package(5, "410 S State St", "EOD", "Salt Lake City", "84111", 5.0, "at hub"),
    Package(6, "3060 Lester St", "10:30 AM", "West Valley City", "84119", 88.0, "awaiting"),
    Package(7, "1330 2100 S", "EOD", "Salt Lake City", "84106", 8.0, "at hub"),
    Package(8, "300 State St", "EOD", "Salt Lake City", "84103", 9.0, "at hub"),
    Package(9, "300 State St", "EOD", "Salt Lake City", "84103", 2.0, "at hub"),
    Package(10, "600 E 900 South", "EOD", "Salt Lake City", "84105", 1.0, "at hub"),
    Package(11, "2600 Taylorsville Blvd", "EOD", "Salt Lake City", "84118", 1.0, "at hub"),
    Package(12, "3575 W Valley Central Station bus Loop", "EOD", "West Valley City", "84119", 1.0, "at hub"),
    Package(13, "2010 W 500 S", "10:30 AM", "Salt Lake City", "84104", 2.0, "at hub"),
    Package(14, "4300 S 1300 E", "10:30 AM", "Millcreek", "84117", 88.0, "at hub"),
    Package(15, "4580 S 2300 E", "9:00 AM", "Holladay", "84117", 4.0, "at hub"),
    Package(16, "4580 S 2300 E", "10:30 AM", "Holladay", "84117", 88.0, "at hub"),
    Package(17, "3148 S 1100 W", "EOD", "Salt Lake City", "84119", 2.0, "at hub"),
    Package(18, "1488 4800 S", "EOD", "Salt Lake City", "84123", 6.0, "at hub"),
    Package(19, "177 W Price Ave", "EOD", "Salt Lake City", "84115", 37.0, "at hub"),
    Package(20, "3595 Main St", "10:30 AM", "Salt Lake City", "84115", 37.0, "at hub"),
    Package(21, "3595 Main St", "EOD", "Salt Lake City", "84115", 3.0, "at hub"),
    Package(22, "6351 South 900 East", "EOD", "Murray", "84121", 2.0, "at hub"),
    Package(23, "5100 South 2700 West", "EOD", "Salt Lake City", "84118", 5.0, "at hub"),
    Package(24, "5025 State St", "EOD", "Murray", "84107", 7.0, "at hub"),
    Package(25, "5383 South 900 East #104", "10:30 AM", "Salt Lake City", "84117", 7.0, "awaiting"),
    Package(26, "5383 South 900 East #104", "EOD", "Salt Lake City", "84117", 25.0, "at hub"),
    Package(27, "1060 Dalton Ave S", "EOD", "Salt Lake City", "84104", 5.0, "at hub"),
    Package(28, "2835 Main St", "EOD", "Salt Lake City", "84115", 7.0, "awaiting"),
    Package(29, "1330 2100 S", "10:30 AM", "Salt Lake City", "84106", 2.0, "at hub"),
    Package(30, "300 State St", "10:30 AM", "Salt Lake City", "84103", 1.0, "at hub"),
    Package(31, "3365 S 900 W", "10:30 AM", "Salt Lake City", "84119", 1.0, "at hub"),
    Package(32, "3365 S 900 W", "EOD", "Salt Lake City", "84119", 1.0, "awaiting"),
    Package(33, "2530 S 500 E", "EOD", "Salt Lake City", "84106", 1.0, "at hub"),
    Package(34, "4580 S 2300 E", "10:30 AM", "Holladay", "84117", 2.0, "at hub"),
    Package(35, "1060 Dalton Ave S", "EOD", "Salt Lake City", "84104", 88.0, "at hub"),
    Package(36, "2300 Parkway Blvd", "EOD", "West Valley City", "84119", 88.0, "at hub"),
    Package(37, "410 S State St", "10:30 AM", "Salt Lake City", "84111", 2.0, "at hub"),
    Package(38, "410 S State St", "EOD", "Salt Lake City", "84111", 9.0, "at hub"),
    Package(39, "2010 W 500 S", "EOD", "Salt Lake City", "84104", 9.0, "at hub"),
    Package(40, "380 W 2880 S", "10:30 AM", "Salt Lake City", "84115", 45.0, "at hub")
]

