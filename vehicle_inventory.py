#-------------------------------------------------------------------------------------------------------------------------------------
# Program Objective: Create an automobile class that will be used by a dealership as a vehicle inventory program.
# The following attributes are the automobile class:
# -private string make
# -private string model
# -private string color
# -private int year
# -private int mileage
# This program have appropriate methods such as:
# -constructor
# -add a new vehicle
# -remove a vehicle
# -update vehicle attributes
# At the end of your program, it will allow the user to output all vehicle inventory to a text #file.
#--------------------------------------------------------------------------------------------------------------------------------------
class Automobile:
    
    def __init__(self):
        self.car_make = ''
        self.car_model = ''
        self.car_color = ''
        self.car_year = 0
        self.car_mileage = 0
    def addVehicle(self):
        try:
            self.car_make = input('Enter make: ')
            self.car_model = input('Enter model: ')
            self.car_color = input('Enter color: ')
            self.car_year = int(input('Enter year: '))
            self.car_mileage = int(input('Enter mileage: '))
            return True
        except ValueError:
            print('Please try again. Please use only whole numbers for mileage and year.\n*Do not use commas to speart the numbers.')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self.car_make, self.car_model, self.car_color, self.car_year, self.car_mileage])

class Inventory:
    def __init__(self):
        self.vehicles = []
    def addVehicle(self):
        vehicle = Automobile()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            print ()
            print('Vehicle added, Thank you')
    def viewInventory(self):
        print('\t'.join(['','Make','Model', 'Color', 'Year', 'Mileage']))
        for idx, vehicle in enumerate(self.vehicles) :
            print(idx + 1, end='\t')
            print(vehicle)

automotive_inventory = Inventory()

while True:

    print ('''
Automative Inventory Command Center

    1.Add a Vehicle
    
    2.Delete a Vehicle
    
    3.View Inventory
    
    4.Update Existing Inventory
    
    5.Export Inventory
    
    6.Quit
    ''')
    userInput=input('Please choose one of the above options: ') 
        #add a vehicle to the inventory
    if userInput=="1": 
        automotive_inventory.addVehicle()
        # delete a vehicle from the inventory
    elif userInput=='2':
        if len(automotive_inventory.vehicles) < 1:
            print('Sorry there are no vehicles in inventory')
            continue
        automotive_inventory.viewInventory()
        item = int(input('Enter the number associated with the vehicle to remove: '))
        if item - 1  > len(automotive_inventory.vehicles):
            print('Invalid number')
        else:
            automotive_inventory.vehicles.remove(automotive_inventory.vehicles[item - 1])
            print ()
            print('Vehicle has been removed')
            # view the list of all the vehicles
    elif userInput == '3': 
        if len(automotive_inventory.vehicles) < 1:
            print('Sorry there are no vehicles in inventory')
            continue
        automotive_inventory.viewInventory()
           # edit a vehicle from the inventory  
    elif userInput == '4':
        if len(automotive_inventory.vehicles) < 1:
            print('Sorry there are no vehicles in inventory')
            continue
        automotive_inventory.viewInventory()
        item = int(input('Enter the number associated with the vehicle to update: '))
        if item - 1  > len(automotive_inventory.vehicles):
            print('Invalid number')
        else:
            automobile = Automobile()
            if automobile.addVehicle() == True :
                automotive_inventory.vehicles.remove(automotive_inventory.vehicles[item - 1])
                automotive_inventory.vehicles.insert(item - 1, automobile)
                print ()
                print('Vehicle has been updated')
            # export the list of the inventory to a text file
    elif userInput == '5':
        if len(automotive_inventory.vehicles) < 1:
            print('Sorry there are no vehicles in inventory')
            continue
        i = open('VihicleInventory.txt', 'w')
        i.write('\t'.join(['Make','', 'Model','','Year','', 'Color','', 'Mileage']))
        i.write('\n')
        for vechicle in automotive_inventory.vehicles:
            i.write('%s\n' %vechicle)
        i.close()
        print('Vehicle inventory has been exported to file named VihicleInventory.txt')
    elif userInput == '6':
        # exit the loop
        print('Good Bye. Have a great day!')
        break
    else:
        #invalid user input
        print('Invalid input, please try again')
