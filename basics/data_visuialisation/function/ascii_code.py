print("program started")
print("Please enter a standard character:")
word=input()
if (len(word)==1):
    print("th ascii code for {}is {}".format(word,ord(word)))
else:
    print("A single character was expected")
print("end the program")