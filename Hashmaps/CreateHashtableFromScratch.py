# Question: Implement a Hashtable

# Implement a simple hashtable without using any special collections classes or helpers (you can use native Java arrays). Your implementation should minimally meet the following requirements:

#     Support generics for both key and value types
#     Implement the standard get, put, remove, size, clear, and isEmpty operations as defined in java.util.Map
#     Support an initial default capacity of 16 entries
#     Support dynamic allocation of additional capacity as needed


# idea:
# [_|_|_|_|_|_]
#-> [key, value] ->

class Hashtable:
    def __init__(self, initial_size):
        self.initial_size = initial_size
        self.size = 0
        self.table = [[] for x in range(initial_size)]

    def print_table(self):
        print self.table

    def put_into_hash(self, key, value):
        hashed_key = hash(key)
        print "hashed_key:"
        print hashed_key
        index = hashed_key%self.initial_size
        pair = (key, value)
        print "index"
        print index
        self.table[index].append(pair)
        self.print_table()
        self.size += 1


    def get_from_hash(self, key):
        hashed_key = hash(key)
        index = hashed_key%self.initial_size
        print "index"
        print index
        for node in self.table[index]:
            print node
            if key == node[0]:
                return node[1]
        return None

    def remove(self, key):
        hashed_key = hash(key)
        index = hashed_key%self.initial_size    #    0  , 1
        node_list = self.table[index] # [(int, [()])]
        print node_list
        for i, node in enumerate(node_list):
            if key == node[0]:
                node_list.pop(i)
                self.size -= 1
        self.print_table()

    def get_size(self):
        return self.size

    def clear_table(self):
        self.table = [[]]*initial_size

hashtable = Hashtable(16)
print hashtable
hashtable.put_into_hash("sdfs", "hello")
print hashtable
print hashtable.get_from_hash("sdfs")

hashtable.put_into_hash("yes", "dude")
hashtable.put_into_hash("3", "p")
hashtable.remove("yes")
