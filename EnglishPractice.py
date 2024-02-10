from Dictionary import sozluk
from colorama import Fore, Back, Style
import random
keys = []
values = []
notes_keys = []
notes_values = []
previousword = ""
key_list = list(sozluk.keys())
val_list = list(sozluk.values())
def CreateKeys():
	global keys
	for i in key_list:
		keys.append(i)
def CreateValues():
	global values
	for i in val_list:
		values.append(i)	
true_counter = 0
CreateKeys()
CreateValues()
def ControlKey(object):
	hasdicword = False
	for item in key_list:
		if item == object:
			hasdicword = True
	return hasdicword
def ControlVal(object):
	hasdicword = False
	for item in val_list:
		if item == object:
			hasdicword = True
	return hasdicword
print("\n\n------------------------")
print("WELCOME TO THE WORD QUİZ\n If write \"/help\" you will see the other comments but first choos game type")
print("Please choose: 'en-tr' or 'tr-en'")
choice = input()
if choice == "en-tr":
	print("what is turkish mean of this?")
	while True:
		word =  random.choice(keys)
		print(Fore.BLUE+word)
		print(Fore.WHITE+"Type the correct answer")
		answer = input()
		if answer == "/help":
			print(Fore.GREEN+"quit:'exit the program'\npress enter:'if you are sure to know the word, you can pass with press enter(word is considered correct)'\nnote:'note to this word, in the exit you will see noted word and you can copy the words'\nPnote: 'note to previous word'\n control: Checks if the word is in the dictionary"+Fore.WHITE)
			print("------------------------------------")
			print(Fore.BLUE+word+Fore.WHITE)
			answer = input()
		if answer == "control":
			control = input(Fore.CYAN)
			result = ControlKey(control)
			if result == True:
				print(Fore.CYAN+f"Dictionary has {control}"+Fore.WHITE)
				print("------------------------------------")
				print(Fore.BLUE+word+Fore.WHITE)
				answer = input()
			else:
				print(f"Dictionary doesn't have {control}")	
				print("------------------------------------")
				print(Fore.BLUE+word+Fore.WHITE)
				answer = input()

		if answer == "Pnote":
			notes_keys.append(previousword)
			notes_values.append(sozluk[previousword])
			print(Fore.LIGHTRED_EX+"Previous word was noted"+Fore.WHITE)
			print("------------------------------------")
			print(Fore.BLUE+word+Fore.WHITE)
			answer = input()
		if answer == "note":
			notes_keys.append(word)
			notes_values.append(sozluk[word])
			print(Fore.LIGHTRED_EX+"This word was noted"+Fore.WHITE)
			print("------------------------------------")
			print(Fore.BLUE+word+Fore.WHITE)
			answer = input()

		if answer == "quit":
			break	
		if answer == "":
			print(Fore.YELLOW+f"\"{sozluk[word]}\" You're pass this word."+Fore.WHITE)
			keys.remove(word)
			true_counter+=1
			print(f"{true_counter}/{len(sozluk.keys())}")
			print("------------------------------------")
		elif answer.lower() == sozluk[word]:
			print(Fore.GREEN+"CORRECT"+Fore.WHITE)
			keys.remove(word)
			true_counter+=1
			print(f"{true_counter}/{len(sozluk.keys())}")
			print("------------------------------------")
		else:
			print(Fore.RED+f"INCORRECT correct answer is \"{sozluk[word]}\""+Fore.WHITE)
			print(f"{true_counter}/{len(sozluk.keys())}")
			print("------------------------------------")
		previousword = word
elif choice == "tr-en":
	print("what is english mean of this?")
	while True:
		word =  random.choice(values)
		print(Fore.BLUE+word)
		print(Fore.WHITE+"Type the correct answer")
		answer = input()
		if answer == "/help":
			print(Fore.GREEN+"quit:'exit the program'\npress enter:'if you are sure to know the word, you can pass with press enter(word is considered correct)'\nnote:'note to this word, in the exit you will see noted word and you can copy the words'\nPnote: 'note to previous word'"+Fore.WHITE)
			print("------------------------------------")
			print(Fore.BLUE+word+Fore.WHITE)
			answer = input()
		if answer == "control":
			control = input(Fore.CYAN)
			result = ControlVal(control)
			if result == True:
				print(Fore.CYAN+f"Dictionary has '{control}'"+Fore.WHITE)
				print("------------------------------------")
				print(Fore.BLUE+word+Fore.WHITE)
				answer = input()
			else:
				print(f"Dictionary doesn't have {control}")	
				print("------------------------------------")
				print(Fore.BLUE+word+Fore.WHITE)
				answer = input()			
		if answer == "Pnote":
			notes_keys.append(previousword)
			notes_values.append(key_list[val_list.index(previousword)])
			print(Fore.LIGHTRED_EX+"Previous word was noted"+Fore.WHITE)
			print("------------------------------------")
			print(Fore.BLUE+word+Fore.WHITE)
			answer = input()
		if answer == "note":
			notes_keys.append(word)
			notes_values.append(key_list[val_list.index(word)])
			print(Fore.LIGHTRED_EX+"This word was noted"+Fore.WHITE)
			print("------------------------------------")
			print(Fore.BLUE+word+Fore.WHITE)
			answer = input()

		if answer == "quit":
			break	
		if answer == "":
			print(Fore.YELLOW+f"\"{key_list[val_list.index(word)]}\" You're pass this word."+Fore.WHITE)
			values.remove(word)
			true_counter+=1
			print(f"{true_counter}/{len(sozluk.keys())}")
			print("------------------------------------")
		elif answer == key_list[val_list.index(word)]:
			print(Fore.GREEN+"CORRECT"+Fore.WHITE)
			values.remove(word)
			true_counter+=1
			print(f"{true_counter}/{len(sozluk.keys())}")
			print("------------------------------------")
		else:
			print(Fore.RED+f"INCORRECT correct answer is \"{key_list[val_list.index(word)]}\""+Fore.WHITE)
			print(f"{true_counter}/{len(sozluk.keys())}")
			print("------------------------------------")
		previousword = word

print("See you later")
if len(notes_keys) != 0:
	print("Your Notes:\n")
	for i in range(len(notes_keys)):
		print(Fore.LIGHTRED_EX+notes_keys[i]+"= "+notes_values[i]+Fore.WHITE)
input()	

