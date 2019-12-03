class Person:
	
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def say_hello(self, to_name):
		print(“hello, “ + to_name + “ my name is ” + self.name)

	def introduce(self):
		print(“My name is “ + self.name + “ and I am “ + str(self.age) + “years old”)

jo = Person(“jo”, 20)
* jo = name with init
* 20 = age with init

jo.say_hello(“devon”)
* devon = to_name

jo.introduce 

* using object.function to utilize functions within the class
* using variables within the class to match when defining the instance
    * name이라는 variable을 hard code하지 않고, object를 만들때 새로 define 하고 싶을때
    * __init__(self, variable):
		self.variable = variable

Inheritance: inheriting a larger class within a smaller class
* e.g. Person class, but police is a smaller subclass
* use case: defining classes that are completely different but share a main thing from a common class

Example

class Police(Person):
	def arrest(self, to_arrest):
		print (“you are under arrest, “ + to_arrest)

class Programmer(Person):
	def program(self, to_program):
		print (“I’m donzo with this project, I should work on “ + to_project + “next)

* Police & Programmer class inheriting Person class

jo = Person (“jo”, 20)
devon = Police (“devon”, 22)
david = Programmer (“david”, 23)

* all jo, devon, david can use functions in Person class
* only devon can arrest, and david can program

Q: 
* what if you inherit, but have additional init definitions? which parameters go first? Or is init not allowed within a subclass?

