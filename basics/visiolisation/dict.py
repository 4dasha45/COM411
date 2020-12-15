import matplotlib.pyplot as plt
import random
def data():
  paths={}
  print("what tipe of line you like?")
  print("1):\n2)--\n3)-")
  line = input()
  print("what color wouldd do you lik\n1)red (r)\n2)blue(b)\n3)green(g)")
  color = input()
  print("what type of marker do you like?\n1)o\n2)s\n3)^")
  marker=input()
  paths['liny']=line
  paths['colorly']=color
  paths['marky']=marker
  return paths
def generate():
  print("how any line wuold you like to display? ")
  line_num = int(input())
  for line_nums in range(line_num):
    values = data()
    x = random.sample(range(1,10),5)
    y = random.sample(range(1,10),5)
    format=f"{values['line']}{values['color']}{values['marker']}"
    plt.plot(x,y,format)
def run():
  print("running...")
  generate()
  print("done!")
run()
