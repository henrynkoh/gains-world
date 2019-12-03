Lesson 5: Package & Module

Package: combination of modules with a particular purpose
* library = package

module: combinations of code for a particular functionality
* benefits: easy to utilize codes on public, without the need for redoing the work

Example

Goal: creating animal package (folder)
* dog, cat modules (files)

dog.py

class Dog:
	def hi(self):
		print(“woof”)

cat.py

class Cat:
	def hi(self):
		print(“meow”)

IMPORTANT: to enable animal folder as a package, need a special file named __init__.py

__init__.py
* must tell the animal package is combination of what modules

from .cat import Cat
from .dog import Dog

* . <- “within this directory” take Cat / Dog class from cat.py
* import * -> calling all functions

Q:
* __init__.py file -> what else has to be defined here? Do you need .cat import Cat here?

main.py

from animal import dog 
from animal import cat

* from animal package, bring a module named dog

Good tip
* good to go right into the code sample
* installing the most up-to-date version in a file like requirements.txt



