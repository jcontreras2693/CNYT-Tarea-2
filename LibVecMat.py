import copy
import math

def multesccomp(num,comp):
    return num*comp[0],num*comp[1]

def suma(a,b):
    """retorna la suma entre dos numeros complejos"""
    return (a[0]+b[0]),(a[1]+b[1])

def resta(a,b):
    """retorna la resta entre dos numeros complejos"""
    return (a[0]-b[0]),(a[1]-b[1])

def conjug(a):
    """retorna el conjugado de un numero complejo"""
    return a[0],(a[1]*(-1))

def producto(a,b):
    """retorna el producto entre dos numeros complejos"""
    if a==(0,0) and b==(0,0):
        return a
    elif a[0]==b[0] and a[1]==(b[1]*-1):
        return (a[0]**2)+(a[1]**2),0
    return ((a[0]*b[0])-(a[1]*b[1])),((a[0]*b[1])+(a[1]*b[0]))

def advec(a,b):
    """retorna la suma entre dos vectores complejos"""
    resp=[]
    for i in range(len(a)):
        resp.append(suma(a[i],b[i]))
    return resp

def susvec(a,b):
    """retorna la resta entre dos vectores complejos"""
    resp=[]
    for i in range(len(a)):
        resp.append(resta(a[i],b[i]))
    return resp

def invadvec(vec):
    return advec(vec,multescvec(-1,vec))

def multescvec(num,vector):
    resp=[]
    try:
        for i in range(len(vector)):
            x=vector[i]
            y=(x[0]*num,x[1]*num)
            resp.append(y)
    except TypeError:
        for i in range(len(vector)):
            resp.append(vector[i]*num)
    return resp

def admat(mat1,mat2):
    copia=copy.deepcopy(mat1)
    for i in range(len(mat1)):
        x=mat1[i]
        for j in range(len(x)):
            copia[i][j]=suma(mat1[i][j],mat2[i][j])
    return copia

def susmat(mat1,mat2):
    copia=copy.deepcopy(mat1)
    for i in range(len(mat1)):
        x=mat1[i]
        for j in range(len(x)):
            copia[i][j]=resta(mat1[i][j],mat2[i][j])
    return copia

def transmatvec(mat):
    for i in range(len(mat)):
        x=mat[i]
        try:
            for j in range(len(x)):
                if i<=j:
                    temp=mat[i][j]
                    mat[i][j]=mat[j][i]
                    mat[j][i]=temp
        except TypeError:
            return mat
    return mat

def invadmat(mat):
    x=copy.deepcopy(mat)
    return admat(mat,multescmat(-1,x))

def multescmat(num,mat):
    matc=copy.deepcopy(mat)
    for i in range(len(mat)):
        try:
            for j in range(len(mat[i])):
                matc[i][j]=multesccomp(num,mat[i][j])
        except TypeError:
            matc[i]=multescvec(num,mat[i])
    return matc

def conjugmatvec(mat):
    for i in range(len(mat)):
        x=mat[i]
        try:
            for j in range(len(x)):
                mat[i][j]=conjug(mat[i][j])
        except TypeError:
            resp=[]
            for k in range(len(mat)):
                resp.append(conjug(mat[k]))
            return resp
    return mat

def adjunmatvec(mat):
    mat=transmatvec(mat)
    for i in range(len(mat)):
        x=mat[i]
        try:
            for j in range(len(x)):
                mat[i][j]=conjug(mat[i][j])
        except TypeError:
            resp=[]
            for k in range(len(mat)):
                resp.append(conjug(mat[k]))
            return resp
    return mat

def prodmat(mat1,mat2):
    copia=copy.deepcopy(mat1)
    mat2=transmatvec(mat2)
    for i in range(len(mat1)):
        x=mat1[i]
        for j in range(len(x)):
            copia[i][j]=valmultvecrealcomp(mat1[i],mat2[j])
    return copia

def valmultvecrealcomp(arr1,arr2):
    sumai=(0,0)
    sumatoria=0
    x=False
    for i in range(len(arr1)):
        try:
            sumai=suma(sumai,producto(arr1[i],arr2[i]))
            x=True
        except TypeError:
            sumatoria+=arr1[i]*arr2[i]
    if x:
        return sumai
    return sumatoria

def accmatvec(mat,vec):
    resp=[]
    for i in range(len(mat)):
        x=mat[i]
        for j in range(len(x)):
            y=(valmultvecrealcomp(mat[i],vec))
        resp.append(y)
    return resp

def prodintvec(vec1,vec2):
    try:
        return valmultvecrealcomp(adjunmatvec(vec1),vec2)
    except TypeError:
        return valmultvecrealcomp(transmatvec(vec1),vec2)

def normavec(vec):
    """
    norma o modulo
    """
    x=prodintvec(vec, vec)
    return math.sqrt(pow(x[0],2)+pow(x[1],2))

def disvec(vec1,vec2):
    vec=susvec(vec1,vec2)
    return normavec(vec)

def matunit(mat):
    unit=copy.deepcopy(mat)
    for i in range(len(unit)):
        for j in range(len(unit[i])):
            if i==j:
                unit[i][j]=1
            else:
                unit[i][j]=0
    return unit

def isunit(mat):
    m1=elround(prodmat(adjunmatvec(mat),mat))
    m2=elround(prodmat(mat,adjunmatvec(mat)))
    m3=elround(matunit(mat))
    return isequal(m1,m3) and isequal(m2,m3)

def isequal(mat1,mat2):
    try:
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                if mat1[i][j]!=mat2[i][j]:
                    return False
    except TypeError:
        return False
    return True
def elround(mat):
    for i in range(len(mat)):
        try:
            for j in range(len(mat[i])):
                mat[i][j]=(round(mat[i][j][0],3),round(mat[i][j][1],3))
        except TypeError:
            for j in range(len(mat[i])):
                mat[i][j]=round(mat[i][j],3)
    return mat

def ishermitian():
    return

def prodtenmatvec(mat1,mat2):
    vecten=[]
    lineas=[]
    if type(mat1[1]) is int:
        for i in range(len(mat1)):
            vecten+=(multescvec(mat1[i],mat2))
    elif type(mat1[1]) is tuple:
        for i in range(len(mat1)):
            for j in range(len(mat1)):
                vecten.append(producto(mat1[i],mat2[j]))
    elif type(mat1[1]) is list:
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                if type(mat1[i][j]) is int:
                    linea=multescvec(mat1[i][j],mat2[i])
                lineas.append(linea)
            vecten.append(lineas)
        for k in range(len(vecten)):
            for h in range(len(vecten[k])):
                reserva=[]
                for g in range(len(vecten[k][h])):
                    reserva+=vecten[k][h][g]
                vecten[k][h]=reserva
    return


#[[3,2],[6,1]],[1,2]
#[[(1,3),(5,1)],[(2,1),(0,7)]],[(1,2),(3,1)]
#x=1/math.sqrt(2)
#q=isunit([[(1,0),(1,0)],[(1,0),(1,0)]])
#print(q)
e=prodtenmatvec([[0,1],[1,0]],[[0,1],[1,0]])
print(e)
#q=prodmat(adjunmatvec([[(x,0),(x,0)],[(x,0),(-x,0)]]),[[(x,0),(x,0)],[(x,0),(-x,0)]])
#print(q)
#for i in range(len(q)):
#    print(q[i])
#w=adjunmatvec((2,3))
#print(w)
#print(invadvec([(1,2),(0,1)]))
