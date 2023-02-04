# Complete the following "Matrix" class, implemented as specified in the comments (replace "pass" with your code).  


'''
Python Raw Coding by a C/C++ expert
Compiled by:
Md. Asaduzzaman Jabin
Ph.D. Student, ECE, UGA
'''


 
from copy import copy
from operator import add, eq, getitem, mul, setitem, sub


class Matrix:
    def __init__(self,data,num_rows): 
        # Input: data is a list of numerical values in row-order, num_rows is how many elements there are per row.  
        # Output: None: Side effect of the initialized matrix object, including num_rows and num_cols properties
        # i.e. A = Matrix([1,2,3,4],2) would be 
        # the 2x2 matrix with 1,2 in the first row, 3,4 in the second row, 
        # and A.num_rows == 2 and A.num_cols == 2   
        
        self.data = data
        self.num_rows = num_rows
        self.num_colums = len(self.data)//self.num_rows
        #print (self.num_colums)
        pass
    


    def __add__(self,other): 
        # Input: other is another Matrix object
        # Output: self + other is a new Matrix object (copied data)

        
        try:
            #print(len(self.data), len(other.data))
            data = list(range(len(self.data)))
            if(len(self.data) == len(other.data)):  # will ensure number of row == number of row, number of column = number of column for square matrix
                for i in range(0,len(self.data)):
                    data[i]= int(self.data[i]) + int(other.data[i])
                return data.copy()
        except Exception as err:
            return err

    def __sub__(self,other): 
        # Input: other is another Matrix object
        # Output: self - other is a new Matrix object (copied data)
        
        try:
            #print(len(self.data), len(other.data))
            data = list(range(len(self.data)))
            if(len(self.data) == len(other.data)):  # will ensure number of row == number of row, number of column = number of column for square matrix
                for i in range(0,len(self.data)):
                    data[i]= int(self.data[i]) - int(other.data[i])
                return data.copy()
        except Exception as err:
            return err

    def __mul__(self,other): 
        # Performs matrix multiplication in the linear algebra sense
        # Input: other is another Matrix object, where self.num_rows == other.num_cols
        # Output: self * other is a new Matrix object (copied data)
        
        data = list(range(len(self.data)))
        try:
            if self.num_rows == other.num_colums:  # will ensure number of row == number of row, number of column = number of column for square matrix
                for i in range((self.num_rows)): #copy
                    for j in range((other.num_colums)):  #copy
                        sum =0
                        for k in range((self.num_colums)):  
                            # 0 indexed 
                            sum += self.data[i*self.num_colums+k] * other.data[k*other.num_colums+j]  ## formula : Aij += Bik*Ckj
                        data[i*self.num_colums+j] = sum
                    
                return data.copy()
        except Exception as err:
            return err

    def __getitem__(self,location): 
        # Input: location is a 2-tuple, e.g. A[3,2] would get the element at row 3, column 2 
        # Output: The value at that location, which may be retrieved as location[0]*self.num_cols + location[1]

        # 0 indexed
        return self.data[(location[0])*self.num_colums + (location[1])]

    def __setitem__(self,location,value): 
        # Input: location is a 2-tuple and value is a number to set, e.g. A[3,2] = 7 would set the element at row 3, column 2 to 7
        # Output: None, Side effect of the element being set

        # 0 indexed
        self.data[(location[0])*self.num_colums + (location[1])]= value
        pass

    def __str__(self): 
        # Input: None
        # Output: returns a string representation of self
        # i.e. if A = Matrix([1,2,3,4],2), print(A) would yield
        # |1 2|
        # |3 4|

        # two process
        
        #return ",".join([str(x)for x in self.data])

        pos = 0
        s=""

        for i in range(self.num_rows):
            #convert row into your format (2 3 4)
            row = " ".join([str(x)for x in self.data[pos:pos+self.num_colums]])
            
            s2 = f"|{row}|\n"
            pos += self.num_colums  # rotate position
            s +=s2
        return s
            
    def __eq__(self, other):
        # Input: other is a Matrix to compare the elements to
        # Output: returns True if self[i,j] == other[i,j] for all valid i,j otherwise False

        #  0 indexed and num row == num column and num column == num column is must
            try:
                if self.num_rows == other.num_rows and self.num_colums == other.num_colums:  
                    # will ensure number of row == number of row, number of column = number of column for square matrix
                    for i in range (len(self.data)):
                        if(self.data[i]==other.data[i]): #if matched then keep checking
                            continue
                        else: return False
                    return True
            except Exception as err:
                return err

    def copy(self):
        # Input: None
        # Output: returns a new matrix, assigned to the same objects within self (i.e. a new underlying list, but the same internal objects)

        return Matrix(self.data.copy(),self.num_rows)

    def transpose(self):
        # Input: None
        # Output: None, Side effect of the rows becoming the columns and the columns becoming the rows.  Don't forget to change num_rows and num_cols

        #0 indexed
        data = list(range(len(self.data)))
        l= 0
        for i in range (self.num_rows):
            for j in range (self.num_colums):
                pos_prev = i*self.num_rows+j
                pos_next = j*self.num_rows+i        #tranposed position
                data[pos_next] = self.data[pos_prev]
        
        #self.data =data
        #swap num row and column
        temp = self.num_rows
        self.num_rows = self.num_colums
        self.num_rows = temp
        self.data = data
        pass

    def transposed(self):
        # Input: None
        # Output: Shallow copy of the matrix that is transposed

        return self.data.copy()

    def fill(num_rows,num_cols,value):
        # Input: num_rows and num_cols of the desired matrix to be filled with value
        # Output: a new matrix, with the specified number of rows and columns, all filled with the specified value
        data = list(range(num_rows*num_cols))
        for i in range(num_rows*num_cols):
            data[i]= value
        
        return Matrix(data, num_rows)


# A = Matrix([1,2,3,4],2)
# B = Matrix([1,3,2,4],2)

# print(str(A))
# print(str(B))


# print(add(A, B))
# print(sub(A, B))
# print(mul(A,B))
# print(getitem(A, [1,1]))
# setitem(A, [1,1], 6)
# print(str(A))
# print(eq(A,B))

# C = copy(A)
# print(str(C))

# Matrix.transpose(A)
# D = Matrix.transposed(A)
# print(str((D)))

# E = Matrix.fill(2,2,3)
# print(str(E))

'''
Output:
$ "C:/Users/Wrong Answer/miniconda3/python.exe" "c:/Users/..../test_matrix.py"
|1 2|
|3 4|

|1 3|
|2 4|

[2, 5, 5, 8]
[0, -1, 1, 0]
[5, 11, 11, 25]
4
|1 2|
|3 6|

False
|1 2|
|3 6|

[1, 3, 2, 6]
|3 3|
|3 3|

|1 2|
|3 4|

|1 3|
|2 4|

[2, 5, 5, 8]
[0, -1, 1, 0]
[5, 11, 11, 25]
4
|1 2|
|3 6|

False
|1 2|
|3 6|

[1, 3, 2, 6]
|3 3|
|3 3|
'''