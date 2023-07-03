class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def speak(self):
        raise notImplementedError("Child classes must implement this method")

class Dog(Animal):
    def speak(self):
        return "Bark"

class Horse(Animal):
    def speak(self):
        return "neigh"

class Simba(Animal):
    def speak(self):
        return "Roar"
class cat(Animal):
    def speak(self):
        return "meow"

dog=Dog("Bosco","red")
print(dog.name)
print(dog.color)
print(Dog.speak(""))

cat=cat("Pussy","pink")
print(cat.color)
print(cat.name)
print(cat.speak())

horse=Horse("Bojack", "Grey")
print(horse.name)
print((horse.color))
print(horse.speak())

simba=Simba("Mufasa", "Blue")
print(simba.name, simba.color, simba.speak())