class A():
	def __init__(self):
		print "This is class A"
	def mod(self):
		print "This is mod method from A"

class B(A):
	def __init__(self):
		print "This is class B"
	def mul(self):
		print "This is mul method from B"

class C(A):
	def __init__(self):
		print "This is class C"
	def sub(self):
		print "This is sub method from C"

class D(B, C):
	def __init__(self):
		print "This is class D"
	def add(self):
		print "This is add method from D"

d_obj = D()
d_obj.add()
d_obj.mod()




b_obj = B()




c_obj = C()

class returnString():
	"""docstring for """
	
	def drawString(self, string, times):
		print string * times


class fiveTimes(returnString):
	""""""
	def function1(self):
		return returnString().drawString("Hello  ",5)

class threeTimes(returnString):
	"""docstring for threeTimes"""
	
		
	def function1(self):
		return returnString().drawString("Hello ",3)


three_obj = threeTimes()
three_obj.function1()

five_obj = fiveTimes()
five_obj.function1()

		
print "Polymorphism examples..."

class Animal():
	"""docstring for Animal"""
	
	def makeNoise(self):
		print "All animals make different noises."

class Dog(Animal):
	"""docstring for Dog"""
	def makeNoise(self):
		print "The Dog says...bhow bhow bhow !!!"

class Cat(Animal):
	"""docstring for Cat"""
	def makeNoise(self):
		print "The Cat says...meow meow meow !!!"
		

object_1 = Animal()
object_1.makeNoise()

object_2 = Dog()
object_2.makeNoise()

object_3 = Cat()
object_3.makeNoise()



