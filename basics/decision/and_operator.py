def display_ladder(steps):
  for step in range(steps):
    print("||")
    print("**")
  print("||")

  
def create_leader():
  print("please enter number of steps")
  steps=int(input())
  display_ladder(steps)
create_leader()
    
print("what did i hear?")
voice=input()
print("what did i see?")
image=input()
if(voice=="grrr") and (image=="two red eyes"):
  print("There is a scary creature. I should get out of here!")
else:
  print("I am little scared but i will continue")

