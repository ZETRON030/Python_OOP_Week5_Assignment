# conventional class
class Animal:
    def eat(self):
        print("The animal eats.")

# Subclasses for specific animals
class Lion(Animal):
    def eat(self):
        print("eats animal flesh.")

class Hen(Animal):
    def eat(self):
        print("eats maize.")

class Shark(Animal):
    def eat(self):
        print("eats other  smaller fishes.")

class Cobra(Animal):
    def eat(self):
        print("eats Chicken eggs.")
        

#  demo code
def animal_eat_demo():
    animals = [Lion(), Hen(), Shark(), Cobra()]
    
    for animal in animals:
        print(f"{animal.__class__.__name__}")
        animal.eat()

# execute demo code
animal_eat_demo()

