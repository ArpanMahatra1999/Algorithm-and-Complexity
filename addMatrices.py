#defining array length
N = 4

#defining function according to algorithm
def addMatrices(A,B,C):
    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j] + B[i][j]

#defining A
A = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]

#defining B
B = [[16,15,14,13],
    [12,11,10,9],
    [8,7,6,5],
    [4,3,2,1]]

#to store results
C = A[:][:]

#calling function
addMatrices(A,B,C)

#finding resultant of matrix in same order
print("Resultant matrix of Additing of ", A ," and ", B ," is ")
for i in range(N):
    for j in range(N):
        print(C[i][j])
