'''
This script takes an input from the user and prints the meaning 
The script and data file need to be stored in the same directory. 
'''
def diction():
	import json
	new_word = []
	use_case = True
	data = open("data.json")
	data_json = json.load(data)

	while use_case == True:
		item = (input("What word would you like to check the meaning please? ")).lower()
		calc = len(item)
		if item == "":
			use_case = False
			break
		if item in data_json.keys():
			print("########################################################")
			for element in (data_json[item]):
				print(element)
			print("########################################################")	
		else:
			for element in (data_json.keys()):
				for letter in item:
					if letter not in element:
						new_word = []
						break
					else:
						new_word.append(letter)

				if len(new_word) == calc:
					corr = input(f"There is no such word as {item}, Do you mean {element} | Yes(Y) or No(N)")
					if corr == "Y":
						print (data_json[element])
						break
					else:
						print("No such word")
diction()