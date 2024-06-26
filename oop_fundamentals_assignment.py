# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.

class Vehicle: 
    def __init__(self, reg_number, type, owner):
        self.reg = reg_number
        self.type = type
        self.owner = owner 
        
    def update_owner():
        owner = ()
        print()
        new_owner = input("Hello new owner, please enter your name: ")
        owner = new_owner
        
        return owner
    
    new_info = update_owner()
    print(f"Congratulations {new_info}! You are the new owner of this vehicle")
  
vehicle = Vehicle("AS 1542 E", "Volkswagon", "Dr. Asiedu")
print(f'But the other {vehicle.type} with registration no. {vehicle.reg} belongs to {vehicle.owner}')