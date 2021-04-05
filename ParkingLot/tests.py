import parking_lot_1

def test_sum():
    P = parking_lot_1.ParkingLot('Google Parking Lot', '123, Fort, Mumbai')
    F1 = parking_lot_1.ParkingLevel('F1')
    F1.addSpot(parking_lot_1.VehicleType.CAR, 3)
    F1.addSpot(parking_lot_1.VehicleType.BIKE, 3)
    P.addLevel(F1)

    T1 = parking_lot_1.Ticket(parking_lot_1.Car('MH05 AB 5454'))
    lol = P.processEntry(T1)
    assert lol == 'Entry Completed For : MH05 AB 5454', "Should be 6"


if __name__ == "__main__":
    test_sum()
    print("Everything passed")
