import sympy as sp
from functools import partial
import mpmath
ANGKA_BENA = 3
mpmath.mp.dps = ANGKA_BENA 
round3 = partial(round, ndigits=3)
sp.init_printing(use_unicode=True)
x,y,z = sp.symbols("x y z")

P = sp.Matrix([
    [2.51,1.48,4.53],
    [1.48,0.93,-1.30],
    [2.68,3.04,-1.48]
])
Q = sp.Matrix([0.05,1.03,-0.53])
A = sp.Matrix([[1,2,3,-1],
              [2,5,4,8],
              [4,2,2,1],
              [6,4,-1,-2]])

B = sp.Matrix([10,8,-2,4])

M = sp.Matrix([
    [2,3,-1],
    [4,-2,5],
    [1,2,3]
])
N = sp.Matrix([10,5,15])

# sp.pprint(A)
# x is the entry of the matrix, i is the iterator in the for loop
# A.row_op(1, lambda x,i: x - 2*A.row(0)[i])
# print(A[0,0])
# def _quickAndDirtyDivisionByDiagonal(Matrix):
#     Matrix = Matrix.copy()
#     dim = sp.shape(Matrix)[0]
#     dim2 = sp.shape(Matrix)[1]
#     newMatrix = [[0 for i in range(dim2)] for j in range(dim)]
#     for i in range(dim):
#         for j in range(dim2):
#             newMatrix[i][j] = Matrix[i,j]
#     for i in range(dim):
#         for j in range(dim2):
#             newMatrix[i][j] /= newMatrix[i][i]
#     return sp.Matrix(newMatrix)
def roundEquation(expr,significand):
    return expr.xreplace(sp.core.rules.Transform(lambda x: x.round(significand), lambda x: isinstance(x, sp.Float)))
def _getSolution(augmentedMatrix, isL = False):
    dim = sp.shape(augmentedMatrix)[0]
    newVector = augmentedMatrix[:,dim]
    Matrix = augmentedMatrix[:,:dim]
    variables = sp.symbols(f"a:{len(newVector)}")
    systemOfEquation = [0] * dim
    solution = [0] * dim

    for line in range(dim):
        for variable in range(dim):
            systemOfEquation[line] += Matrix[line,variable]*variables[variable]
        systemOfEquation[line] = sp.Eq(systemOfEquation[line],newVector[line])
    iter = range(dim) if isL else range(dim-1,-1,-1)
    for system in iter:
        eqbuf = 0
        if system == iter[0]:
            print("&",sp.latex(roundEquation(sp.simplify(systemOfEquation[system]),ANGKA_BENA)),r"\\")
            solution[system] = sp.solve(systemOfEquation[system],variables[system])[0]
        else:
            eqbuf = systemOfEquation[system]
            for variable in range(dim):
                if solution[variable] != 0:
                    eqbuf = eqbuf.subs(variables[variable],solution[variable])
                print("&",sp.latex(roundEquation(sp.simplify(eqbuf),ANGKA_BENA)),r"\\")
            solution[system] = sp.solve(eqbuf,variables[system])[0]
    # print("solution")    
    # print(sp.latex(solution))
    return sp.Matrix(solution)
def gaussianRowEchelonFormWithSteps(Matrix,Vector,plain=False):
    dim = sp.shape(Matrix)[0] #row echelon form is taken from its ROWS
    Matrix = Matrix.copy()
    Matrix = Matrix.row_join(Vector)
    print(sp.latex(Matrix))
    for i in range(dim):
        for j in range(i+1,dim):
            pivot = Matrix[i,i]
            pointToDelete = Matrix[j,i]
            Matrix.row_op(j, lambda x, k : x + ((-pointToDelete/(pivot))*Matrix.row(i)[k]))
            tmp = Matrix.applyfunc(round3)
            print("&",sp.latex(Matrix) , f'R_{j} +', r'\frac{', sp.N(-pointToDelete,3), '}{', sp.N(pivot,3), '}R_{' , i, r'}\\')
    if plain:
        return Matrix
    else:
        return (Matrix[:,:dim],_getSolution(Matrix))
def gaussianRowEchelonFormWithStepsAndPivoting(Matrix,Vector):
    dim = sp.shape(Matrix)[0] #row echelon form is taken from its ROWS
    Matrix = Matrix.copy()
    Matrix = Matrix.row_join(Vector)
    for i in range(dim):
        max = -float('inf')
        maxIndex = -1
        for k in range(i,dim):
            if  sp.Abs(Matrix[i,k])> max:
                max = Matrix[i,k]
                maxIndex = k
        if maxIndex != Matrix[i,i]:
            Matrix.row_swap(i,maxIndex)
            tmp = Matrix.applyfunc(round3)
            print("&",sp.latex(tmp) , 'R_{',i ,r'}\leftrightarrow R_{' , maxIndex,r"}\\")

        for j in range(i+1,dim):
            pivot = Matrix[i,i]
            pointToDelete = Matrix[j,i]
            Matrix.row_op(j, lambda x, k : x + ((-pointToDelete/(pivot))*Matrix.row(i)[k]))
            tmp = Matrix.applyfunc(round3)
            print("&",sp.latex(tmp) , f'R_{j} +', r'\frac{', -pointToDelete, '}{', pivot, '}R_{' , i, r'}\\')
    print("elimination done")
    return (Matrix[:,:dim],_getSolution(Matrix))

def gaussJordanWithSteps(Matrix,Vector):
    rowEchelonForm = gaussianRowEchelonFormWithSteps(Matrix,Vector,plain=True)
    dim = sp.shape(rowEchelonForm)[0]
    rowEchelonForm = rowEchelonForm.copy()
    for i in range(dim):
        for j in range(0,i):
            pivot = rowEchelonForm[i,i]
            pointToDelete = rowEchelonForm[j,i]
            rowEchelonForm.row_op(j, lambda x, k : x + ((-pointToDelete/(pivot))*rowEchelonForm.row(i)[k]))
            print("&",sp.latex(rowEchelonForm) , f'R_{j} +', r'\frac{', -pointToDelete, '}{', pivot,3, '}R_{' , i, r'}\\')
    for i in range(dim):
        pivot = rowEchelonForm[i,i]
        rowEchelonForm.row_op(i,lambda x,k : x/pivot)
        print("&",sp.latex(rowEchelonForm), r"\frac{R_{", i,r"}}{", pivot,r"}\\") if pivot != 1 else ...

    return (rowEchelonForm[:,:dim],rowEchelonForm[:,dim:])
def getInverseOfMatrix(Matrix):
    dim = sp.shape(Matrix)[0]
    Matrix = Matrix.copy()
    Identity = sp.eye(dim)
    inverseMatrix = gaussJordanWithSteps(Matrix,Identity)[1]
    return inverseMatrix
def getLU(Matrix):
    dim = sp.shape(Matrix)[0] 
    U = Matrix.copy()
    L = sp.zeros(dim,dim)
    for i in range(dim):
        # this is for finding the L Matrix
        pivot = U[i,i]
        if pivot == 1:
            for k in range(i,dim):
                L[k,i] = U[k,i]
        else:
            for k in range(i,dim):
                L[k,i] = U[k,i]/pivot
        for j in range(i+1,dim):
            #this is OBE
            pointToDelete = U[j,i] 
            U.row_op(j, lambda x, k : x + ((-pointToDelete/(pivot))*U.row(i)[k]))
    return (L,U)
def solveLU(L,U,B):
    Y = _getSolution(L.row_join(B),isL=True)
    print("Y is obtained")
    X = _getSolution(U.row_join(Y))
    return X 

# print(sp.latex(gaussJordanWithSteps(A,B)))

# sp.pprint(gaussianRowEchelonFormWithSteps(A,B))
# sp.pprint(gaussJordanWithSteps(A,B))
# print(sp.latex(getInverseOfMatrix(A)))
# print(sp.latex(getLU(A)))
L,U = getLU(A)
# print()
print(sp.latex(gaussJordanWithSteps(M,N)))
