import numpy as np

#create one dimensional array
first = np.array([4,5,6], dtype='int16')
print(first)
print(type(first))


#create two dimensional array
second = np.array([[4,5,6],[7,8,9]])
print(second)

#get some array information
print("Dimension of array - first: ")
print(first.ndim)
print("Dimension of array - second: ")
print(second.ndim)
print("Shape of array first: ")
print(first.shape)
print("Shape of array second")
print(second.shape)
print("Datatype of array - first: ")
print(first.dtype)

third = np.array([[4.0,5.0,6.0],[7,8,9]])
print(third)

print("Datatype of array - second: ")
print(second.dtype)

print("Datatype of array - third: ")
print(third.dtype)


print("Array size - first:")
print(first.itemsize)
print("Count of values - first: ")
print(first.size)

print("Array size - second:")
print(second.itemsize)
print("Count of values - second: ")
print(second.size)

print("Array size - third:")
print(third.itemsize)
print("Count of values - third: ")
print(third.size)


print("Storage in bytes - first: ")
print(first.nbytes)

print("Storage in bytes - second: ")
print(second.nbytes)

print("Storage in bytes - third: ")
print(third.nbytes)


#access and update numpy arrays! -> element, rows, column

fourth = np.array([[8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8]])
print(fourth.shape)
print(fourth)

#arrayname[row, column]
print(fourth[1, 2])
print(fourth[1, 0])

#reverse order
print(fourth[0, -3])
#normal order
print(fourth[0, 1 ])

#rows only
print(fourth[1])
print(fourth[0])

#column only
print(fourth[:,2])
print(fourth[:,0])

#extract from middle of array
# arrayname[startindex:endindex:step]
print("For row 0 get column 0 to length 6")
print(fourth[0,0:6])

print("For row 0 get column 0 to length 8 with step 2")
print(fourth[0,0:8:2])


print("For row 1 get column 2 to length 8 with step 2")
print(fourth[1,2:8:2])


print("For row 1 get column 2 to length 6 with step 2")
print(fourth[1,2:6:2])

#update value in 2D array
"""
[[8 7 6 5 4 3 2 1]
 [1 2 3 4 5 6 7 8]]
 """
fourth[1, 4 ] = 44
print(fourth)

#update specific column to single value
"""
[[ 8  7  6  5  4  3  2  1]
 [ 1  2  3  4 44  6  7  8]]
"""
fourth[:,6] = 88
print(fourth)
"""
[[ 8  7  6  5  4  3 88  1]
 [ 1  2  3  4 44  6 88  8]]
"""
fourth[:,5] = [10, 100]
print(fourth)
"""
[[  8   7   6   5   4  10  88   1]
 [  1   2   3   4  44 100  88   8]]
"""

print("3D arrays")

threed = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(threed)
"""
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
"""
print("shape of threed:")
print(threed.shape)
"""

  [4]
"""
print(threed[0, 1 , 1])
"""

  [3, 4]
"""
print(threed[0, 1 , :])
"""
 [1, 2]
  [3, 4]
"""
print(threed[0, : , :])
"""
[[5 6]
 [7 8]]
"""
print(threed[1, : , :])
"""
[[3 4]
  [7 8]]

"""
print(threed[:,1,:])
"""
[[1 2]
[5 6]]
"""
print(threed[:,0, :])
print("Replace elements in threed: ")
"""
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
"""
#replacing the 1st row (index pos is 0) of each 2d matrix in 3d matrix
threed[:,0,:] = [[10,11],[12,13]]
print(threed)
#replacing the 2nd row (index pos is 1) of each 2d matrix in 3d matrix
threed[:,1,:] = [[21,22],[23,24]]
print(threed)
#will throw error
#ValueError: setting an array element with a sequence.
#threed[:,1,:] = [[21],[23,24]]
#threed[:,1,:] = [[21, 22, 30],[23,24]]

print("Initialize arrays with numpy using diff values!!!!")
print("All zeros matrix:")
allzeros = np.zeros(8)
print(allzeros)
allzeros2d =  np.zeros((4, 4))
print(allzeros2d)
allzeros2by3 = np.zeros((2, 3), dtype="int32")
print(allzeros2by3)

print("All ones matrix:")

allones2by3 = np.ones((2, 4), dtype="int32")
print(allones2by3)

allones4by3by2 = np.ones((4, 3, 2), dtype="int32")
print(allones4by3by2)

print("Any number matrix: ")
any4by4with88 = np.full((4,4), 88)
print(any4by4with88)

print("Create a matrix with shape same as any other matrix but fill with any default number:")
defaultfourth = np.full(fourth.shape, 4)
print(defaultfourth)
print("Alternate way:")
defaultfourthalternate = np.full_like(fourth, 8)
print(defaultfourthalternate)

print("Create matrix with random decimal values: ")
random4by2 = np.random.rand(4,2)
print(random4by2)

print("Create matrix with random integer values: ")
random4by2int = np.random.randint(20, size=(4,2))
print(random4by2int)

print("Create matrix with random integer values: ")
random4by2by2int = np.random.randint(5, 10, size=(4,2,2))
print(random4by2by2int)

print("Create matrix with random integer values: ")
random4by2by2int = np.random.randint(5, 50, size=(4,2,2))
print(random4by2by2int)

print("Create identity matrix of 2 by 2: ")
identitymatrix = np.identity(2)
print(identitymatrix)

identitymatrix = np.identity(2, dtype="int32")
print(identitymatrix)


print("Create identity matrix of 8 by 8: ")
identitymatrix = np.identity(8)
print(identitymatrix)

print("Use 1D matrix to create new n-dimensional matrix")
matrix1d = np.array([[1,2,3]])
ndim = np.repeat(matrix1d, 3)
print(ndim)
print("Create repeatation for each element in matrix1d as a new row")
"""
 [[1 2 3]
 [1 2 3]
 [1 2 3]]
"""
ndim = np.repeat(matrix1d, 3, axis=0)
print(ndim)
"""
[
    [1 1 1 1 1]
    [1 0 0 0 1]
    [1 0 8 0 1]
    [1 0 0 0 1]
    [1 1 1 1 1]
]
"""
checkone = np.ones((5,5))
print(checkone)
checkzero = np.zeros((3,3))
print(checkzero)
checkzero[1,1]=8
print(checkzero)
#rowindex:length, columnindex:length
checkone[1:4,1:4] = checkzero
print(checkone)

print("Matrix copy!")
copy1 = np.array([10,20,30])
copy2 = copy1
print(copy1)
print(copy2)
copy2[0]= 88
print(copy2)
print(copy1)
copy3 = copy1.copy()
print(copy3)
copy3[0]=8
print(copy3)
print(copy1)


print("Matrix maths: ")
copy = np.array([10,20,30])
addcopy = copy + 4
print(addcopy)

minuscopy = copy - 4
print(minuscopy)

multicopy = copy * 4
print(multicopy)

divcopy = copy / 4
print(divcopy)

ndim = np.random.randint(0, 5, size=(3,3))
print(ndim)
multindim = ndim * 4
print(multindim)

copy = np.array([10,20,30])
dopy = np.array([3,4,5])

chemy = copy + dopy
print(chemy)

print("3 by 3 array with random int between 0 to 6: ")
print(ndim)
print(ndim ** 3)

print("Sin and Cos values:")
print(np.sin(ndim))
print(np.cos(ndim))


print("numpy for linear algebra!")
one = np.full((3,2), 5)
two = np.random.randint(0, 6, size=(2,3))
print("One")
print(one)
print('Two')
print(two)

multiboth = np.matmul(one, two)
print(multiboth)

getdet = np.identity(4)
print(getdet)
print(np.linalg.det(getdet))

wo = np.random.randint(0, 6, size=(3,3))
print(wo)
print(np.linalg.det(wo))

ow = np.linalg.inv(wo)

print(ow)
print(np.linalg.det(ow))

print("Multiply wo and ow to get indentity matrix: ")
print(np.matmul(wo, ow))

print("Statistical functions in numpy: ")
print("Fourth: ")
print(fourth)
print("Mean: ")
print(np.mean(fourth))
print(np.mean(fourth, axis=0))
print(np.mean(fourth, axis=1))

print("Min: ")
print(np.min(fourth))
print(np.min(fourth, axis=0))
print(np.min(fourth, axis=1))
print("Max: ")
print(np.max(fourth))
print(np.max(fourth, axis=0))
print(np.max(fourth, axis=1))

print("Sum:")
print(np.sum(fourth))

print(np.sum(fourth, axis=0))
print(np.sum(fourth, axis=1))

print("Reorganizing the arrays: ")
print("Fourth: ")
print(fourth)
print("Shape:")
print(fourth.shape)
new8by2 = fourth.reshape(8,2)
print("Reshaped to 8 by 2: ")
print(new8by2)
print(new8by2.shape)
new4by4 = fourth.reshape(4,4)
print("Reshaped to 4 by 4: ")
print(new4by4)
print(new4by4.shape)
new2by2by2by2 = fourth.reshape(2,2,2,2)
print("Reshaped to 2 by 2 by 2 by 2: ")
print(new2by2by2by2)
print(new2by2by2by2.shape)

a1 = np.full(4, fill_value=4)
print(a1)
a2 = np.full(4, fill_value=9)
print(a2)
print("Vertical Stack: ")
print(np.vstack([a1, a2]))
print(np.vstack([a1, a2, a2, a1]))
print("Horizontal Stack: ")
print(np.hstack([a1, a2]))
a3 = np.full((2,3), 8)
print(a3)
a4 = np.full((2,4), 2)
print(a4)
print(np.hstack([a3, a4]))


"""
[
  [1  2  3  4  5]
  [6  7  8  9 10]
  [11 12 13 14 15]
  [16 17 18 19 20]
  [21 22 23 24 25]
]

"""
seq = np.arange(1,26)
print(seq)
square1to25 = seq.reshape(5,5)
print(square1to25)

print("Extract 11 12 16 17: ")
print(square1to25[2:4, 0:2])

print("Extract 2 8 14 20: ")
print(square1to25[[0,1,2,3], [1, 2, 3, 4 ]])

print("Extract 1 7 13 19 25 : ")
print(square1to25[[0,1,2,3, 4], [0, 1, 2, 3, 4 ]])

print("Extract 4 5 24 25: ")
print(square1to25[[0,4], 3:])

print("Histogram in numpy: ")
viewslots = np.arange(1000, 10000, step=1000)
print(viewslots)

youtubeviews = np.random.randint(1000, 10000, size=(30,))
print(youtubeviews)

print(np.histogram(youtubeviews, viewslots))
viewcount, viewrange = np.histogram(youtubeviews, viewslots)
print("View count: ")
print(viewcount)
print("View range:")
print(viewrange)