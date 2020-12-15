# import matplotlib.pyplot as plt

# x = [0,2,4,6,8,10]
# y = [0,20,40,60,80,100]

# plt.xlabel("x values")
# plt.ylabel("y values")

# plt.plot(x, y)
# plt.show()
import matplotlib.pyplot as plt

def small():
  x = [3,3,4,4,3]
  y = [3,4,4,3,3]
  plt.plot(x,y,'r:o')
   
 
def mediume():
  x = [2,2,5,5,2]
  y = [2,5,5,2,2]
  
  plt.plot(x,y,'g--s')
  
  
def large():
  x = [1,1,6,6,1]
  y = [1,6,6,1,1]
  
  plt.plot(x,y,'b-p')
  
def run():
  small()
  mediume()
  large()
  plt.show()
run()