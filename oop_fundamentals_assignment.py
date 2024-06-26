# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
class Vehicle: 
    def __init__(self, reg_number, type, owner):
        self.reg = reg_number
        self.type = type
        self.owner = owner 
# Implement a method update_owner to change the vehicle's owner        
    def update_owner():
        owner = ()
        print()
        new_owner = input("Hello previous owner, please enter your name: ")
        owner = new_owner
        
        return owner
    
    new_info = update_owner()
    print(f"Congratulations {new_info} you are no longer the owner! The Vehicle is officially sold")
print()   
# Then, create a few instances of Vehicle and demonstrate changing the owner.
vehicle = Vehicle("AS 1542 E", "Volkswagon", "Dr. Asiedu")
print(f'This {vehicle.type} with registration no. {vehicle.reg} now belongs to {vehicle.owner}')
print()
Ryan_vehicle  = Vehicle("AS 1542 E", "Volkswagon", "Ryan")
print(f'This {vehicle.type} with registration no. {vehicle.reg} now belongs to {Ryan_vehicle.owner}')
print()
Tamar_vehicle  = Vehicle("AS 1542 E", "Volkswagon", "Tamar")
print(f'This {vehicle.type} with registration no. {vehicle.reg} now belongs to {Tamar_vehicle.owner}')


def add_participant():
    people = []
    while True:
        print()
        add_name = input("Please add a name to be added:   ")
        people.append(add_name)
        print(add_name, "has been added")
        print()
        add_more = input("Would you like to add more people to the list? y/n: ")
        if add_more == "y":
            continue
        else: 
            break
    return people

new_list = add_participant()
print()
print("Your newlist is:  ")

for person in new_list:
    print(person)
    
    
    
    
    
    
#  Use the existing Event class by adding an attribute to keep track of the number of participants.
# Implement a method add_participant that increases the count 
# and a method get_participant_count to retrieve the current count.

class Event:
    
    def __init__(self, name, date):
            self.name = name
            self.date = date
            
            
    def add_participant():
        people = []
        while True:
            print()
            add_name = input("Please add a name to be added:   ")
            people.append(add_name)
            print(add_name, "has been added")
            print()
            add_more = input("Would you like to add more people to the list? y/n: ")
            if add_more == "y":
                continue
            else: 
                break
        return people
    
    new_list = add_participant()
    print()
    print("Your newlist is:  ")
    
    for person in new_list:
        print(person)