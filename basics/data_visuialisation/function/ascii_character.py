print("program started")
print("please enter the ascii code:") 
code = abs(int (input ()))

if (code>=32 and code <=126):
    ascii_letter = chr(code)
    print("the character repesented by ascii value {} is: {}. ".format(code, ascii_letter))
else:
    print("the character can not be display")
print("program ended")


