print("Where should i look?")
look=input()
#check the bedroom
if(look=="in the bedroom"):
  print("Where in the bedroom should I look?")
  where=input()

  if(where=="under the bed"):
    print("Found some shoes but no battery")

  else:
    print("Found some mess but no battery.")

#check the bathroom
elif(look=="in the bathroom"):
  print("Where in the bathroom should I look?")

  whereone=input()
  if(whereone=="in the bathtub"):
    print("Found a rubber duck but no battery")

  else:
    print("Found a wet surface but no battery.")

#check in the lab
elif(look=="in the lab"):
  print("Where in the lab should I look?")

  wheretwo=input()
  if(wheretwo=="on the table"):
    print("Yes!! I found my battrey!")

#unknown place
else:
  print("I do not know where that is but I will keep looking.")



