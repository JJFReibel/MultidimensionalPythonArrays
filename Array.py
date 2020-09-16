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
#EDIT: Code still has a number of bugs that are being worked on

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
    
#3-D Array Class
class Array_3D:
  def __init__(self, x, y, z):
    rows, cols, thirds = (x, y, z)
    self.arr = [[[0 for i in range(cols)] for j in range(rows)] for k in range(thirds)]
  def set(self, x, y, z, value):
    self.arr[x][y][z] = value
  def get(self, x, y, z):
    return self.arr[x][y][z]

#4-D Array Class
class Array_4D:
  def __init__(self, x, y, z, t):
    rows, cols, thirds, tyme = (x, y, z, t)
    self.arr = [[[[0 for i in range(cols)] for j in range(rows)] for k in range(thirds)] for l in range(tyme)]
  def set(self, x, y, z, t, value):
    self.arr[x][y][z][t] = value
  def get(self, x, y, z, t):
    return self.arr[x][y][z][t]
  
#Example Use of 2D Array
myArr2D = Array_2D(5,2)
myArr2D.set(1,1,"Hello Mars!")
print(myArr2D.get(1,1))
print(myArr2D.arr)
print("Length column before expansion: " + str(len(myArr2D.arr)))
print("Length row before expansion: " + str(len(myArr2D.arr[0])))
myArr2D.output()
myArr2D.expand(7,3)
print("Length column after expansion: " + str(len(myArr2D.arr)))
print("Length row after expansion: " + str(len(myArr2D.arr[0])))
myArr2D.output()

#Example Use of 3D Array
myArr3D = Array_3D(3,4,5)
myArr3D.set(2,2,2,"Hello Jupiter!")
print(myArr3D.get(2,2,2))


#Example Use of 4D Array
myArr4D = Array_4D(3,4,5,6)
myArr4D.set(2,2,2,2,"Hello Comet!")
print(myArr4D.get(2,2,2,2))
