class Calorie:
    """Represent amount of calories calculated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        return 10*self.weight + 6.25*self.height - 5*self.age + 5 - 10*self.temperature
