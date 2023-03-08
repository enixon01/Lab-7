#Emily Nixon and Rosemary Hoffman
message = str(input("What is the message you are trying to send? \n"))
def too_long(message):
    if len(message)>140:
        print("That message is too long to send.")
    else:
        None
too_long(message)

import unicodedata
unicodedata.lookup("snake")
unicodedata.lookup("dog")
unicodedata.lookup("rose")
