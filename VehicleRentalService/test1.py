from vehicle_renting_service import BranchService, Branch, VehicleType, Vehicle, SUV, Hatchback, Sedan
import unittest

class TestSum(unittest.TestCase):

    def test_create_branches(self):
        branchService = BranchService()

        # Adding branches
        branchService.addBranch('Vasant Vihar')
        branchService.addBranch('Cyber City')

        self.assertEqual(len(branchService.branches), 2, "Should add the branches to the memory")

    def test_price_allocation(self):
        branchService = BranchService()

        # Adding branches
        branchService.addBranch('Vasant Vihar')
        branchService.addBranch('Cyber City')

        # Allocating prices
        branchService.allocatePrice('Vasant Vihar', VehicleType.Sedan, 100)
        branchService.allocatePrice('Vasant Vihar', VehicleType.Hatchback, 80)
        branchService.allocatePrice('Cyber City', VehicleType.Sedan, 200)
        branchService.allocatePrice('Cyber City', VehicleType.Hatchback, 50)

        self.assertEqual(branchService.branches['Vasant Vihar'].prices[VehicleType.Sedan], 100, 'Should add correct prices for the branch')
        self.assertEqual(branchService.branches['Vasant Vihar'].prices[VehicleType.Hatchback], 80, 'Should add correct prices for the branch')
        self.assertEqual(branchService.branches['Cyber City'].prices[VehicleType.Sedan], 200, 'Should add correct prices for the branch')
        self.assertEqual(branchService.branches['Cyber City'].prices[VehicleType.Hatchback], 50, 'Should add correct prices for the branch')

    def test_adding_vehicles(self):
        branchService = BranchService()

        branchService.addBranch('Vasant Vihar')
        branchService.addBranch('Cyber City')

        # Allocating prices
        branchService.allocatePrice('Vasant Vihar', VehicleType.Sedan, 100)
        branchService.allocatePrice('Cyber City', VehicleType.Sedan, 200)

        # Adding vehicles
        branchService.addVehicle('DL 01 MR 9310', VehicleType.Sedan, 'Vasant Vihar')
        branchService.addVehicle('DL 01 MR 9311', VehicleType.Sedan, 'Cyber City')

        self.assertEqual(len(branchService.branches['Vasant Vihar'].vehicles[VehicleType.Sedan]), 1, 'Should add vehicles for the branch')
        self.assertEqual(len(branchService.branches['Cyber City'].vehicles[VehicleType.Sedan]), 1, 'Should add vehicles for the branch')


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
