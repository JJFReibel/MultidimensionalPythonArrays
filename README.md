# MultidimensionalPythonArrays
Multidimensional arrays in Python made easy
Implementation includes 2D, 3D, and 4D arrays in Python
Classes are Array_2d, Array_3D, and Array_4D
These classes are convenient for matrices as well as for graphing coordinates. The 2D and 3D arrays are good for space coordinates, while the 3D arrays can also be used for 2D space coordinates and a time, such as for position per given time, for graphs, gifs, and more. The 4D array is especially useful for 3D space coordinates and a value of time, to keepd track of a moving 3D body's position at different time intervals.
Functions, besides the constructors, include get, set, expand, and reduce.
For get, specify coordinates, and the value will be returned.
For set, specify the coordinates, and then the value.
For expand, specify new dimensions that are greater than before.
For reduce, specify dimensions that are less than before.
Future versions of this library may include a reset function, that can reset the dimensions with some being larger while others are smaller. As it stands, for safety, expand is designed for all coordinate elements to increase or stay the same, while reduce is designed for all coordinates to decrease or stay the same. Use each individually in the order necessary, and make clones to manipulate data.
