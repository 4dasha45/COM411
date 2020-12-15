def display_lader(steps):
  for step in range(steps):
    print("| |")
    print("***")
  print("| |")
def create_leader():
  print("how many steps remain")
  steps=int(input())
  display_lader(steps)
create_leader()
