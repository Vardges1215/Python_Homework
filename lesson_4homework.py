#Lesson 4
#We must make an online-shop

class Country:
	def __init__(self,name,continent):
		self.name = name
		self.continent = continent

	def country_presentation(self):
		print(f"The continent is {self.continent} and the name of country was {self.name}")

class Brand:
	def __init__(self,brand_name,buss_start_date):
		self.brand_name = brand_name
		self.buss_start_date = buss_start_date

	def brand_presentation(self):
		print(f"Brand name {self.brand_name}, business will be started in {self.buss_start_date}")

class Season:
	def __init__(self,the_season,average_temp):
		self.the_season = the_season
		self.average_temp = average_temp
	def season_presentation(self):
		print("It is {} now and average temperature is {} C".format(self.the_season,self.average_temp))

class Description(Country,Brand,Season):
	def __init__(self,name,continent,brand_name,buss_start_date,the_season,average_temp):

		Country.__init__(self,name,continent)
		Brand.__init__(self,brand_name,buss_start_date)
		Season.__init__(self,the_season,average_temp)


	def description_presentation(self):
		self.country_presentation()
		self.brand_presentation()
		self.season_presentation()


class Product(Country,Brand,Season):
	def __init__(self):
		self.product_name = "Coat"
		self.product_type = "Outwear"
		self.product_price = 120
		self.quantity = int(input("tell me quentity-> "))

	def porduct_presentation(self):

		print(f" name: {self.product_name}\n type: {self.product_type}\n price: {self.product_price} $\n quantity: {self.quantity}")
		if self.quantity > 10:
			self.product_price = self.product_price // 10
			return "sale:",self.product_price,"$"


itog = Description("Eurasia","France","Lacoste","10.12.1955","Summer","30")
itog.description_presentation()

itog2 = Product()
print(itog2.porduct_presentation())
