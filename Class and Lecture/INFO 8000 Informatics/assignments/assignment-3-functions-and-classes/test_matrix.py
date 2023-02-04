from matrix import *

A = Matrix([1,2,3,4],2)
B = Matrix([1,3,2,4],2)

print(str(A))
print(str(B))


print(add(A, B))
print(sub(A, B))
print(mul(A,B))
print(getitem(A, [1,1]))
setitem(A, [1,1], 6)
print(str(A))
print(eq(A,B))

C = copy(A)
print(str(C))

Matrix.transpose(A)
D = Matrix.transposed(A)
print(str(D))

E = Matrix.fill(2,2,3)
print(str(E))