def display_in_box(word):
  dashs= 4 + len(word)
  print("-"*dashs)
  print("| {} |".format (word))
  print("-"*dashs)
def lower_case(word):
  print(word.lower())
def upper_case(word):
  print(word.upper())
def mirrored(word):
  mirrored==""
  for letter in reversed(word):
      mirrored += letter
  print("{} | {} ".format (word,mirrored))
def repeat(word):
  print("how many time would you like to repeat the word?")
  how_many=int(input())
  for times in range(how_many):
    if (how_many % 2 ==0):
      print(lower_case(word))
    else:
     print(upper_case(word))

 
  

def run():
  print("please enter the word!")
  word=input()

 
  function = 0
  while(function!=6):
      print("please chose one function from  belove list?")
      print("1)Display in box\n2)Display in lower case\n3)Display in upper case\n4)Display Mirrored\n5)Repeat\n6)Quat")
      function=int(input())

      if (function==1):
        display_in_box(word)
      elif(function==2):
        lower_case(word)
      elif(function==3):
        upper_case(word)
      elif(function==4):
        mirrored(word)
      elif(function==5):
        repeat(word)
      elif (function==6):
        break
      else:
        print("unknown option")
  
  
run()
