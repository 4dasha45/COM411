print(" Hello\n enter the activity to be performed")
activity = input()
if ( activity=="calculate"):
    print("CHOSE ONE ACTIVITY TO BE PERFORMED")
    print("MULTIPLICATION\nADDITION\nSUBTRACTION\nDIVISION")
    activity2=input()
    if (activity2=="multiplication"):
       print("enter your first number please")
       first_number =int (input())
       print("enter your second number please")
       second_number = int (input())
       print("{}*{}" .format (first_number*second_number))
    elif(activity2 =="addition"):
        print("enter your first number")
        first_number =int (input())
        print ("enter your second number")
        second_number+int (input())
        print("{}+{}".format (first_number + second_number))
    elif (activity2 == "subtraction"): 
      print("{}-{}".format (first_number - second_number))
    elif (activity2 == "division"):
      print("enter yoyr first number")
        first_number = int (input())
        print("enter your second number")
        second _number = int (input())
        print("{} / {}". format (first_number/second_number))
    else:
      print("the option is not exist")







else:
  print("activity not exist")
print("activity completed")  
