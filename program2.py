class Dog:
    animal = 'dog'

    def __init__(self, breed, color):

        self.breed = breed
        self.color = color


Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
print(Rodger)
print(Rodger.animal)
print(Rodger.breed)
print(Rodger.color)
print(Buzo.breed)

print(Dog.animal)