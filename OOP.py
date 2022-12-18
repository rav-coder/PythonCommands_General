
# hold customer id, name, balance

# methods: deposit, withdraw

# self to define a instance
class Account:

	# variable outside any methods will be a class variable
	count = 0

	@classmethod         # class method using the decorator
	def increment_count(cls):
		cls.count += 1

	@classmethod
	def getCount(cls):
		return cls.count

	@staticmethod      # access using Account.print_Val()
	def print_Val():   # we wont access class or instance variables in static method, no parameter
		print("Static method")

	def __init__(self,cust_id,name,initial_bal=0): # call is implicit with double underscore in python
		self.id = cust_id
		self.__name = name   # double underscore means its a private variable (so need getter and setter)
		self.balance = initial_bal
		Account.count+=1 # classname and class variable, all instances will have the same count value
		# can do Account.increment_count() also

	def getBalance(self):
		return self.balance

	def getName(self):
		return self.__name

	def deposit(self,amount):
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self,amount):
		if amount > self.balance:
			return "Insufficient balance"
		else:
			self.balance -= amount
			return self.balance


class Saving_Account(Account):    # inheritance
	def __init__(self,id,name,initial_bal=0):
		super().__init__(id,name,initial_bal) # use method from parent class
		self.limit = 1000  

	def withdraw(self,amount):     # Methods overriding
		if amount < self.limit:
			super().withdraw(amount)
			self.limit -= amount
		else:
			print("Daily limit reached")

cust4 = Saving_Account("104","QWE")  # for methods it will search for init method in Saving account, if not found it will go to parent class
print(cust4.deposit(100))

customer1 = Account("101","ABC") #passes customer1 as the first argument so we need keyword self

customer1.deposit(200)
customer1.withdraw(10)

print(customer1.id,customer1.getName(),customer1.getBalance())

customer2 = Account("102","XYZ")
print(customer2._Account__name)  # can access private variable this way, not fully restricted in python
print(customer1.__dict__) # in dictionary its stored this way {'id': '101', '_Account__name': 'ABC', 'balance': 190}

customer2.deposit(20)

customer3 = Account("103","DEF")
customer3.deposit(20)
print(Account.getCount())

# when modified by classname all instances will change
Account.count+= 2
print(customer1.count)

# can still change for one instance using customer1.count +=1

l = [customer1,customer2,customer3]

for obj in l:
	if obj.balance < 30:
		print(obj.id,obj.getName())


# we also can have multiple inheritance as well
class A:
	pass
class B:
	pass
class C(A,B):  # C, A, B will be the order (left to right)
	pass