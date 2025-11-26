#! /bin/python3
import random, math
import pyperclip

def password_generator(password_length):
    valid_character_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                            "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "|", ";", "0", "1", "2",
                            "3","4","5","6","7","8","9"] # 80
    password = ""
    temp_pass = []
    for i in range(password_length):
        rand_int = math.ceil(random.random()*(len(valid_character_list)-1))
        rand_letter = valid_character_list[rand_int]
        temp_pass.append(rand_letter)
        password = "".join(temp_pass)
    pyperclip.copy(password)
    print("Your password is: " + password + "\nYour password has been copied to your clipboard.")

try:
    input_length = int(input("Enter password character length: "))
    password_generator(input_length)
except ValueError:
    print("Please enter an integer next time. ")
except pyperclip.PyperclipException:
    print("Please install a copy/paste mechanism on your system.")
