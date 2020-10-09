#Lesson 2

class My_dict:
	def __init__(self,make_dict,duplicate_values,highest_num):
		self.make_dict = make_dict
		self.duplicate_values = duplicate_values
		self.highest_num = highest_num

#We must write a program to create a dictionary from a string.
	def my_string(self):
		text = "python"
 
		dict_string = {} 
		for i in text: 
			if i in dict_string: 
				dict_string[i] += 1
			else: 
				dict_string[i] = 1
		return dict_string
#Need to remove duplicate values from Dictionary.
	# def duplicates(self,duplicate_values):
		

answer = My_dict("python","loooop",101120)
print(answer.my_string())

