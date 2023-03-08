#Emily Nixon and Rosemary Hoffman
def o_present(word):
    total = 0
    for n in word:
        if n == "o":
            total = total + 1
    print(total)

o_present("common")
o_present("like")
o_present("orange")

#The negative index goes from right to left rather than left to right
#A possible use of the negative index would be that it could show the last character printed in a statement
