class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.color = coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old and is {self.color} in color!"

    def speak(self, voice):
        return f"{self.name} says {voice}!"


philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.color}.")
