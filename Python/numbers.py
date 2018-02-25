def print_numbers(numbers):
	print ("Telephone numbers: ")
	for x in numbers.keys():
		print ("Name:", x, "\tNumber:", numbers[x])
	print
	
def add_number(numbers, name, number):
	numbers[name] = number
	
def lookup_number(numbers, name):
	if name in numbers:
		return "The number is " + numbers[name]
	else:
		return name + "was not found"
		
def remove_number(numbers, name):
	if name in numbers:
		del numbers[name]
	else:
		print (name, "was not found")
		
def load_numbers(numbers, filename):
	in_file = open(filename, "r")
	while True:
		in_line = in_file.readline()
		if not in_line:
			break
		in_line = in_line[:1]
		name, number = in_line.split(",")
		numbers[name] = number
	in_file.close()
	
def save_numbers(numbers, filename):
	out_file = open(filename, "w")
	for x in numbers.keys():
		out_file.write(x + "," + numbers[x] + "\n")
	out_file.close()
	
def print_menu():
	print ('1. Print Phone Numbers.')
	print ('2. Add a phone number.')
	print ('3. Remove a phone number.')
	print ('4. Lookup a phone number.')
	print ('5. Load numbers.')
	print ('6. Save numbers.')
	print ('7. Quit.')
	
phone_list = {}
menu_choice = 0
print_menu()
while True:
	menu_choice = input("\nType in a number (1-7): ")
	
	if menu_choice == '1':
		print_numbers(phone_list)
		
	elif menu_choice == '2':
		print ("Add Name and Number.")
		name = input("Name: ")
		phone = input("Number: ")
		add_number(phone_list, name, phone)
		
	elif menu_choice == '3':
		print ("Remove name and number.")
		name = input("Name: ")
		remove_number(phone_list, name)
		
	elif menu_choice == '4':
		print ("Lookup number.")
		name = input("Name: ")
		print (lookup_number(phone_list, name))
		
	elif menu_choice == '5':
		filename = input("Filename to load: ")
		load_numbers(phone_list, filename)
		
	elif menu_choice == '6':
		filename = input("Filename to save: ")
		save_numbers(phone_list, filename)
		
	elif menu_choice == '7':
		break
	else:
		print_menu()
		
print("Goodbye!")
input()
