#polymorphism

class Dog():
    def speak(self):
        print("Bhow bhow")

class Cat():
    def speak(self):
        print("Meow meow")

dog=Dog()
cat=Cat()

cat.speak()
dog.speak()