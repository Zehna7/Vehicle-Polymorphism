class BMW:
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower

    def start_engine(self):
        return f"The BMW {self.model}'s engine starts with a roar!"

    def drive(self):
        return f"The BMW {self.model} accelerates with {self.horsepower} horsepower!"

class Ferrari:
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower

    def start_engine(self):
        return f"The Ferrari {self.model}'s engine starts with an exhilarating sound!"

    def drive(self):
        return f"The Ferrari {self.model} zooms with {self.horsepower} horsepower!"

def test_car(car):
    print(car.start_engine())
    print(car.drive())

bmw_car = BMW(model="X5", horsepower=300)
ferrari_car = Ferrari(model="488 Spider", horsepower=670)

print("Testing BMW:")
test_car(bmw_car)

print("\nTesting Ferrari:")
test_car(ferrari_car)
