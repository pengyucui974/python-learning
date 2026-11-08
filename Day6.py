class Animal:
    def speak(self):
        pass
        # print("Animal")


class Dog(Animal):
    def speak(self):
        print("Dog1")

class Cat(Animal):
    def speak(self):
        print("Cat1")

def make_noise(animal:Animal):
    animal.speak()


make_noise(Dog())
make_noise(Cat())

print("Git practice")
print("hello python")