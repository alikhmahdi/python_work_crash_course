class Car:
    """A simple attempt to represent a car."""


    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:
    """A simple attempt to model a battery for an electric car."""


    def __init__(self, battery_size_max, battery_size=0):
        """Initialize the battery's attributes."""
        self.battery_size_max = battery_size_max
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = self.battery_size * 3.5
        print(f"This car can go about {range} miles on {self.battery_size}-kWh charge.")


    def upgrade_battery(self, new_size):
        """Upgrade the battery size."""
        if self.battery_size <= self.battery_size_max and 0 <= new_size <= self.battery_size_max:
            self.battery_size = new_size
            print(f"Upgraded to a {new_size}-kWh battery.")
        else:
            print("This car already has the maximum battery size.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, battery_size_max, battery_size=0):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery(battery_size_max, battery_size)


tesla = ElectricCar("Tesla", "Model S", 2020, 100)
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.upgrade_battery(100)
tesla.battery.describe_battery()
tesla.battery.get_range()
