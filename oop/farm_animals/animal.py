def can_eat() -> bool:
    return True


class Animal:
    def __init__(self, type_of_animal, age, gender, sound, move):
        self.type = type_of_animal
        self.age = age
        self.gender = gender
        self.sound_ = sound
        self.move_ = move

    def sound(self):
        return f"A {self.type} {self.sound_}!"

    def movement(self):
        return f"A {self.type} {self.move_}s!"