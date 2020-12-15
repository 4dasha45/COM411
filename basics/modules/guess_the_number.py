import random
print("please enter the minimum value:")
min_value=int(input())
print("print the maximum value:")
max_value=int(input())
your_guess=random.randrange(min_value,max_value)
print("i am thinking of a number between {} and {}. can you guess what it is?".format(min_value,max_value))

answer=0
while(answer != your_guess):
  print("please enter your guess")
  answer=int(input())
  if(your_guess ==answer ):
    print("Congratulations!")
  elif(your_guess < answer):
    print("Guess higher")    
  else:
    print("Guess lower")

print("Game over!")

    
    
