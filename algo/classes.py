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



class Package:
    def __init__(self, id, address, deadline, city, zip, weight, delivery_status=None, delivery_time=None):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time


class Truck:
    def __init__(self, id, packages:[]=[], status="idle"):
        self.id = id
        self.packages = packages
        self.status= status


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

        
        


        

