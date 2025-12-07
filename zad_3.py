class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House at {self.address}:\n"
                f"Area: {self.area} m2\n"
                f"Rooms: {self.rooms}\n"
                f"Price: {self.price} PLN\n"
                f"Plot size: {self.plot} m2")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat at {self.address}:\n"
                f"Area: {self.area} m2\n"
                f"Rooms: {self.rooms}\n"
                f"Price: {self.price} PLN\n"
                f"Floor: {self.floor}")


house = House(area=120, rooms=5, price=500000, address="Warsaw, Kopernika 8", plot=300)

flat = Flat(area=60, rooms=3, price=300000, address="Krakow, Warszawska 12", floor=2)

print(f'{house}\n\n{flat}')
