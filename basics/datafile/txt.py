import os 
def search(location):
  print("searching...")
  file = open("location.txt")
  for location in os.listdir(file):
    print(f"looled in {file}")
  print("done!")
# def run():
   

