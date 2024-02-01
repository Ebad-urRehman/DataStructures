""" In this file python built in dictionary functions which uses hash tables are overrided and replace with user_built functions which done the same work as dictionary which uses hash map"""

""" for details see ipynb file"""

class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.bucket_arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % 10

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        found = False
        # we have to update the value in list keeping duplicate values in mind
        # for overwriting value we are checking if key value alreading exist in the main list
        # sublists are tuple here which are added for every key and value when they found for the first time
        # and overwrited when we encourter the same key
        print(self.bucket_arr[hash])
        for index, sublist in enumerate(self.bucket_arr[hash]):
            print("run")
            if len(sublist) == 2 and sublist[0] == key:
                print(index)
                print(sublist[0], key)
                self.bucket_arr[hash][index] = (key, value)
                found = True
                break
            # as we are using tuple here thus it is not possible to directly change value instead we insert a new tuple here
        if not found: # The case where we have to insert new key with value
            self.bucket_arr[hash].append((key, value))    
                
    
    def __getitem__(self, key):
        hash = self.get_hash(key)
        for element in self.bucket_arr[hash]:
            if element[0] == key:
                return element[1]
        return 
    def __delitem__(self, key):
        hash = self.get_hash(key)
        for index, key_value in enumerate(self.bucket_arr[hash]):
            if key_value[0] == key:
                del self.bucket_arr[hash][index]


if __name__ == "__main__":
    my_hash = Hash_table()
    my_hash["march 3"] = 130
    my_hash["march 6"] = 40
    my_hash["march 3"] = 178
    my_hash["march 17"] =34
    print(my_hash["march 17"])
    del my_hash["march 6"]
    print(my_hash.bucket_arr)

    