import pyshark
import os.path

name_of_this_tool = "$aturn's R1ng"
separator = "-----------------------------------------"

general_flag = True
flag = True

def colour(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

print(colour(150, 0, 255, "Main Menu. \nType help to see all the commands available."))

while general_flag:
	print(separator)
	input_field1 = input(name_of_this_tool + "> ")
	if input_field1 == "help":
		help_file = open("help.txt", "r")
		print(help_file.read())
	elif input_field1 == "":
		general_flag = True
		flag = False
	elif input_field1 == "clear":
		os.system("clear")
	elif input_field1 == "quit":
		print(colour(255, 0, 0, "Quitting."))
		exit()
	elif input_field1 == "pn":
		print(colour(150, 0, 255, "Type the path to a packet capture file."))
		print(separator)
		input_field2 = input(name_of_this_tool + "> ")
		packet_capture_file_existence = os.path.isfile(input_field2)
		if packet_capture_file_existence:
			print(colour(0, 255, 150, "File Exists."))
			packet_capture_file_in_pyshark = pyshark.FileCapture(input_field2)
			flag = True
		else:
			print(colour(255, 0, 0, "File doesn't exist. \nQuitting."))
			exit()
		while flag:
			try:
				print(colour(150, 0, 255, "Type the packet number."))
				print(separator)
				packet_number = input(name_of_this_tool + "> ")
				packet_number_to_int = int(packet_number)
				packet = packet_capture_file_in_pyshark[packet_number_to_int]
				print(packet.show())
			except:
				print(colour(255, 0, 0, "Something went wrong. \nQuitting."))
				exit()
			print(colour(150, 0, 255, "Choose an option: \n1. [ENTER](Keep analyzing this file) \n2. B(Go back to the main menu) \n3. Q(Quit)"))
			print(separator)
			options = input(name_of_this_tool + "> ")
			if options == "":
				flag = True
			elif options == "B":
				general_flag = True
				flag = False
			elif options == "Q":
				print(colour(255, 0, 0, "Quitting."))
				exit()
			else:
				print(colour(255, 0, 0, "Invalid option. \nQuitting."))
				exit()
	else:
		print(colour(255, 0, 0, "Unknown command. \nQuitting."))
		exit()