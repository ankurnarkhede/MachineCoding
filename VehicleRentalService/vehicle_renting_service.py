
import uuid
from enum import Enum


class VehicleType (Enum):
    SUV = 0,
    Hatchback = 1
    Sedan = 2

class Vehicle:
    def __init__(self, num):
        self.id = uuid.uuid4()
        self.num = num

class Sedan(Vehicle):
    def __init__(self, num):
        super().__init__(num)
        self.type = VehicleType.Sedan

class Hatchback(Vehicle):
    def __init__(self, num):
        super().__init__(num)
        self.type = VehicleType.Hatchback

class SUV(Vehicle):
    def __init__(self, num):
        super().__init__(num)
        self.type = VehicleType.SUV


class Branch:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

        # Hash containing array of vehicles
        # {
        #     'SUV': [vehicleObj1, vehicleObj2, ...],
        #     'Sedan': [vehicleObj1, vehicleObj2, ...]
        # }
        self.vehicles = {}

        # Hash containing prices of behicles
        # {
        #     'SUV': <price>,
        #     'Sedan': <price>
        # }
        self.prices = {}

    def getVehicles(self):
        return self.vehicles

    def getPrices(self):
        return self.prices


class BranchService:
    def __init__(self):
        self.branches = {}

    def addBranch(self, name):
        branch = Branch(name)

        # fill vehicles object in branch to contain an array
        for vehicle in VehicleType:
            branch.getVehicles()[vehicle] = []

        self.branches[name] = branch
        return branch

    def getBranch(self, name):
        return self.branches.get(name)


    def addVehicle(self, number, type, branch_name):
        branch = self.getBranch(branch_name)

        if (not branch):
            print('ERROR:: Branch not found')
            return

        switcher = {
            VehicleType.Sedan: Sedan,
            VehicleType.Hatchback: Hatchback,
            VehicleType.SUV: SUV
        }

        # create vehicle
        vehicle = switcher.get(type)(number)

        # add vehicle to branch
        branch.getVehicles()[type].append(vehicle)


    def allocatePrice(self, branch_name, type, price):
        branch = self.getBranch(branch_name)

        if (not branch):
            print('ERROR:: Branch not found')
            return

        # add price of that vehicle in branch
        branch.getPrices()[type] = price


branchService = BranchService()

# Adding branches
branchService.addBranch('Vasant Vihar')
branchService.addBranch('Cyber City')

# Allocating prices
branchService.allocatePrice('Vasant Vihar', VehicleType.Sedan, 100)
branchService.allocatePrice('Vasant Vihar', VehicleType.Hatchback, 80)
branchService.allocatePrice('Cyber City', VehicleType.Sedan, 200)
branchService.allocatePrice('Cyber City', VehicleType.Hatchback, 50)

# Adding vehicles
branchService.addVehicle('DL 01 MR 9310', VehicleType.Sedan, 'Vasant Vihar')
branchService.addVehicle('DL 01 MR 9311', VehicleType.Sedan, 'Cyber City')
branchService.addVehicle('DL 01 MR 9312', VehicleType.Hatchback, 'Cyber City')



