class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def save_the_day(self):
        return f"{self.name} is saving the day with {self.power} in {self.city}!"

    def __str__(self):
        return f"Superhero: {self.name}, Power: {self.power}, City: {self.city}"

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} mph!"

    def __str__(self):
        return f"Flying Superhero: {self.name}, Power: {self.power}, City: {self.city}, Flight Speed: {self.flight_speed} mph"

# Example usage
if __name__ == "__main__":
    flying_hero = FlyingSuperhero("Captain Code", "Super Coding Skills", "Tech City", 150)
    print(flying_hero.fly())
    print(flying_hero)