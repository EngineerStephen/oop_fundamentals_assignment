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