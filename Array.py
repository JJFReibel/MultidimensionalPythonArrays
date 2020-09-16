#2-D Array Class
class Array_2D:
  def __init__(self, x, y):
    rows, cols = (x, y)
    self.arr = [[0 for i in range(cols)] for j in range(rows)] 
  def set(self, x, y, value):
    self.arr[x][y] = value
  def get(self, x, y):
    return self.arr[x][y]

#3-D Array Class
class Array_3D:
  def __init__(self, x, y,z):
    rows, cols, thirds = (x, y, z)
    self.arr = [[[0 for i in range(cols)] for j in range(rows)] for k in range(thirds)]
  def set(self, x, y, z, value):
    self.arr[x][y][z] = value
  def get(self, x, y, z):
    return self.arr[x][y][z]
  
#Example Use of 2D Array
myArr2D = Array_2D(3,4)
myArr2D.set(2,2,"Hello Mars!")
print(myArr2D.get(2,2))

#Example Use of 3D Array
myArr3D = Array_3D(3,4,5)
myArr3D.set(2,2,2,"Hello Jupiter!")
print(myArr3D.get(2,2,2))
