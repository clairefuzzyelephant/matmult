
def parse_input(dim, matrix):
    dimensions = dim.split(' ')
    for i in range(len(dimensions)):
        dimensions[i] = int(dimensions[i])
    mlist = matrix.split(' ')
    for i in range(len(mlist)):
        mlist[i] = int(mlist[i])
    mat = []
    for i in range(dimensions[0]):
        row = []
        for j in range(dimensions[1]):
            row.append(mlist[i*dimensions[1]+j])
        mat.append(row)
    return mat


def mult(A, B):
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(B)):
            sum = 0
            ind = 0
            while ind < len(B):
                sum += A[i][ind] * B[ind][j]
                ind += 1
            row.append(sum)
        C.append(row)
    return C

if __name__ == '__main__':
    dim1 = raw_input( "Dimensions of matrix 1 with each entry separated by a space: " )
    mat1 = raw_input( "Matrix 1 with each entry separated by a space: ")
    A = parse_input(dim1, mat1)
    dim2 = raw_input( "Dimensions of matrix 2 with each entry separated by a space: " )
    mat2 = raw_input( "Matrix 2 with each entry separated by a space: ")
    B = parse_input(dim2, mat2)

    result = mult(A, B)
    print("Result:")
    for row in result:
        print(row)
