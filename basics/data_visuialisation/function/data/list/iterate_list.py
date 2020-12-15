def directions():
   directions=["move forvard","move backward","Turn left","Turn right"]
   return directions

def Menu():
   print("please select the directoin")
   dirs = directions()
   for index in range(len(dirs)):
     print(f"{index}: {dirs[index]}")

def run():
  Menu()

run()
