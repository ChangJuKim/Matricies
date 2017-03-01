import math


def print_matrix( matrix ):
    s = "["
    for i in range(len(matrix)):
        s += "["
        for j in range(len(matrix[i])):
            s += str(matrix[i][j]) + " "
        s = s[:-1]
        s += "]\n"
    print s[:-1] + "]"

def ident( matrix ):
    matrix[:] = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

def scalar_mult( matrix, s ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = s * matrix[i][j]

#helper for matrix_mult
def make_new_matrix(r, c):
    matrix = []
    for i in range(r):
        matrix.append([])
        for j in range(c):
            matrix[i].append(0)
    return matrix

#copies m1 -> m2
def copy_to_matrix(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m2)):
            m2[i][j] = m1[i][j]
            

#m1 * m2 -> m2
#m1 = i x j
#m2 = k x n
def matrix_mult( m1, m2 ):
    l = make_new_matrix(len(m2), len(m2[0]))
    for n in range(len(m2[0])):
        for i in range(4):
            #print("~~~~~~~~~~~~~~~~~")
            #print_matrix(l)
            for j in range(4):
                l[i][n] += m1[i][j] * m2[j][n]
    copy_to_matrix(l, m2)
                
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    m = [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]]
    print("Calling ident to a matrix: ")
    ident(m)
    print_matrix(m)

    print("\nScalar mult of identity matrix: ")
    scalar_mult(m, 10)
    print_matrix(m)

    print("\nMatrix mult of l: ")
    print_matrix(l)
    print("With m: ")
    print_matrix(m)
    print("Result: ")
    matrix_mult(m, l)
    print_matrix(l)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
