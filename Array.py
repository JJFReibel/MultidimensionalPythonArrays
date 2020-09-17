# MIT License

# Copyright (c) 2020 Jean-Jacques François Reibel

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#Multidimensional arrays in Python made easy.
#2D and 3D arrays implemented with functions
#Example use of 2D and 3D arrays (good for 2D and 3D space, or 2D positions at certain times)
#Eample use of 4D array (good for 3D positions at certain times)

#2-D Array Class
class Array_2D:
  def __init__(self, x, y):
    rows, cols = (x, y)
    self.arr = [[None]*x for _ in range(y)]
  def set(self, x, y, value):
    self.arr[x][y] = value
  def get(self, x, y):
    return self.arr[x][y]
  def output(self):
    for i in range(len(self.arr)):
      for j in range(len(self.arr[0])):
        print(self.arr[i][j])
      print()
  def expand(self, x, y):
    arr2 = [[None]*x for _ in range(y)]
    for i in range(len(self.arr)):
      for j in range(len(self.arr[0])):
        arr2[i][j] = self.arr[i][j]
    self.arr.clear()
    self.arr = arr2
  def reduce(self, x, y):
    arr2 = [[None]*x for _ in range(y)]
    for i in range(len(arr2)):
      for j in range(len(arr2[0])):
        arr2[i][j] = self.arr[i][j]
    self.arr.clear()
    self.arr = arr2
    
#3-D Array Class
class Array_3D:
  def __init__(self, x, y, z):
    rows, cols, thirds = (x, y, z)
    self.arr = [[[None]*x for _ in range(y)] for _ in range(z)]
  def set(self, x, y, z, value):
    self.arr[x][y][z] = value
  def get(self, x, y, z):
    return self.arr[x][y][z]
  def output(self):
    for i in range(len(self.arr)):
      for j in range(len(self.arr[0])):
        for k in range(len(self.arr[0][0])):
          print(self.arr[i][j][k])
        print()
  def expand(self, x, y, z):
    arr2 = [[[None]*x for _ in range(y)] for _ in range(z)]
    for i in range(len(self.arr)):
      for j in range(len(self.arr[0])):
        for k in range(len(self.arr[0][0])):
          arr2[i][j][k] = self.arr[i][j][k]
    self.arr.clear()
    self.arr = arr2
  def reduce(self, x, y, z):
    arr2 = [[[None]*x for _ in range(y)] for _ in range(z)]
    for i in range(len(arr2)):
      for j in range(len(arr2[0])):
        for k in range(len(arr2[0][0])):
          arr2[i][j][k] = self.arr[i][j][k]
    self.arr.clear()
    self.arr = arr2

#4-D Array Class
class Array_4D:
  def __init__(self, x, y, z, t):
    rows, cols, thirds, tyme = (x, y, z, t)
    self.arr = [[[[None]*x for _ in range(y)] for _ in range(z)] for _ in range(t)]
  def set(self, x, y, z, t, value):
    self.arr[x][y][z][t] = value
  def get(self, x, y, z, t):
    return self.arr[x][y][z][t]
  def output(self):
    for i in range(len(self.arr)):
      for j in range(len(self.arr[0])):
        for k in range(len(self.arr[0][0])):
          for t in range(len(self.arr[0][0][0])):
            print(self.arr[i][j][k][t])
          print()
  def expand(self, x, y, z, t):
    arr2 = [[[[None]*x for _ in range(y)] for _ in range(z)] for _ in range(t)]
    for i in range(len(self.arr)):
      for j in range(len(self.arr[0])):
        for k in range(len(self.arr[0][0])):
          for t in range(len(self.arr[0][0][0])):
            arr2[i][j][k] = self.arr[i][j][k]
    self.arr.clear()
    self.arr = arr2
  def reduce(self, x, y, z, t):
    arr2 = [[[[None]*x for _ in range(y)] for _ in range(z)] for _ in range(t)]
    for i in range(len(arr2)):
      for j in range(len(arr2[0])):
        for k in range(len(arr2[0][0])):
          for t in range(len(arr2[0][0][0])):
            arr2[i][j][k][t] = self.arr[i][j][k][t]
    self.arr.clear()
    self.arr = arr2
  
#Example Use of 2D Array
myArr2D = Array_2D(5,2)
myArr2D.set(1,1,"Hello Mars!")
print(myArr2D.get(1,1))
print(myArr2D.arr)
print("Length 2D row before expansion: " + str(len(myArr2D.arr)))
print("Length 2D column before expansion: " + str(len(myArr2D.arr[0])))
myArr2D.output()
myArr2D.expand(7,3)
print("Length 2D row after expansion: " + str(len(myArr2D.arr)))
print("Length 2D column after expansion: " + str(len(myArr2D.arr[0])))
myArr2D.output()
myArr2D.reduce(1,2)
print("Length 2D row after reduction: " + str(len(myArr2D.arr)))
print("Length 2D column after reduction: " + str(len(myArr2D.arr[0])))
myArr2D.output()


#Example Use of 3D Array
myArr3D = Array_3D(5,2,3)
myArr3D.set(0,0,1,"Hello Mars!")
myArr3D.set(0,0,2,"Hello Mars!")
myArr3D.set(0,0,3,"Hello Mars!")
print("Length 3D third before expansion: " + str(len(myArr3D.arr)))
print("Length 3D row before expansion: " + str(len(myArr3D.arr[0])))
print("Length 3D column before expansion: " + str(len(myArr3D.arr[0][0])))
print()
myArr3D.output()
myArr3D.expand(7,3,4)
print("Length 3D third after expansion: " + str(len(myArr3D.arr)))
print("Length 3D row after expansion: " + str(len(myArr3D.arr[0])))
print("Length 3D column after expansion: " + str(len(myArr3D.arr[0][0])))
myArr3D.output()
myArr3D.reduce(1,2,3)
print("Length 3D third after reduction: " + str(len(myArr3D.arr)))
print("Length 3D row after reduction: " + str(len(myArr3D.arr[0])))
print("Length 3D column after expansion: " + str(len(myArr3D.arr[0][0])))
myArr3D.output()

#Example Use of 4D Array
myArr4D = Array_4D(5,2,3,4)
myArr4D.set(0,0,0,1,"Hello Mars!")
myArr4D.set(0,0,0,2,"Hello Mars!")
myArr4D.set(0,0,0,3,"Hello Mars!")
print("Length 4D tyme before expansion: " + str(len(myArr4D.arr)))
print("Length 4D third before expansion: " + str(len(myArr4D.arr[0])))
print("Length 4D row before expansion: " + str(len(myArr4D.arr[0][0])))
print("Length 4D column before expansion: " + str(len(myArr4D.arr[0][0][0])))
print()
myArr4D.expand(7,3,4,5)
print("Length 4D tyme after expansion: " + str(len(myArr4D.arr)))
print("Length 4D third after expansion: " + str(len(myArr4D.arr[0])))
print("Length 4D row after expansion: " + str(len(myArr4D.arr[0][0])))
print("Length 4D column after expansion: " + str(len(myArr4D.arr[0][0][0])))
myArr4D.output()
myArr4D.reduce(1,2,3,2)
print("Length 4D tyme after reduction: " + str(len(myArr4D.arr)))
print("Length 4D third after reduction: " + str(len(myArr4D.arr[0])))
print("Length 4D row after expansion: " + str(len(myArr4D.arr[0][0])))
print("Length 4D column after expansion: " + str(len(myArr4D.arr[0][0][0])))

myArr4D.output()
