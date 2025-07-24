#Dictionaries in python are also classifird as hash tables
person= {
    "name":"Dedan", #name is an index storing the value "Dedan"
    "age": 17,  #age is an index storing the value 17
    "email":"dedan@gmail.com"}

#access
print(person["email"]) #prints the key "email" value
#add or update
person["country"]="Kenya" #adds a new key "country" with value "Kenya"
print(person)

#delete
del person["age"] #deletes the key "age" and its value
print(person)

#hash maps/hash tables
class HashMap:
    def __init__(self,size):
        self.size = size #size of the hash table
        self.table = [[]for _ in range(size)] #creates a list of empty lists for each index

    def put(self,key,value):
        h = hash(key) % self.size #hashes the key and gets the index
        for pair in self.table[h]: #checks if the key already exists
            if pair[0] == key: #if key exists, update the value
                pair[1] = value #updates the value if key exists
                return
        self.table[h].append([key, value]) #if key does not exist, append the key-value pair

    def get(self,key): #retrieves the value for a given key
        h = hash(key) % self.size #hashes the key to find the index
        for pair in self.table[h]: #
            if pair[0] == key: #if key matches, return the value
                return pair[1]
        return None #if key does not exist, return None
    
hm= HashMap(10) #creates a hash map of size 10
hm.put("name", "Okware") #adds a key-value pair
hm.put("age", 97) #adds another key-value pair

print(hm.get("name")) #retrieves the value for the key "name"
print(hm.get("age")) #retrieves the value for the key "age"
print(hm.get("email")) #retrieves the value for the key "email" which does not exist, should return None