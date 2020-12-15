import os
def cwd():
  path = os.getcwd()
  print(f"the current working directori is {path}")
  print(f"the directory contains following: ")
  for file in os.listdir(path):
    print(file)
def run():
  print("processing...")
  cwd()
