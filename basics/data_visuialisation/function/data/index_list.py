def movements():
  path=["move forward",10,"move backward",5,"moveleft",3,"move right",1]
  return path
def run():
  print("moving...")
  path = movements()
  print(f"{path [0]} for {path [1]} steps")
  print(f"{path [2]} for {path [3]} speps")
  print(f"{path [4]} for {path [5]} steps")
  print(f"{path [6]} for {path [7]} steps ")
run()