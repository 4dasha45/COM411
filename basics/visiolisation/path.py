import matplotlib.pyplot as plt

def coordinate():
  print("enter x values please")
  x = int(input())
  print("enter y values please")
  y = int(input())
  
  return (x,y)
def path():
  print("Retreiving path...")
  x_values = []
  y_values = []
  for itrate in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  return(x_values,y_values)
def run():
  values = path()  
  plt.plot(values[0],values[1],"r--o")
  plt.xlabel("x_values")
  plt.ylabel("y_values")
  plt.show()
run()
