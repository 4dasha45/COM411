def directions():
  directions["move forward","move backward","turn left","turn right"]
  return directions

def Menu():
  print("please select a direction")
  dire=directions()
  for index in range(len (dire)):
    print("{}: {}".format(index, dire[index]))
  index = int(input())
  return dire[index]
def run():
  route=[]
  print("Working out escape route...")
  for repeat in range (5):
    route.append(Menu())

  print("escope route:{route}")

run()