import numpy as np
def maximo_cuadrado(M):
    M=np.array(M) #convierte en array
    (n,m)=np.shape(M)
    A=np.ones((n,m)) # MAtriz de 1's para comparar
    b=min(n,m) #cuadrado más grande contenido en la matriz 
    M_previo = M.copy()
    M_trans = M.copy()
    if (M_trans==A).all(): #Revisa si la matriz inicial solo contiene 1's
        return (0,0,0)
    else:
        for dimension in range(1,b+1):
            M_trans[(n-dimension)][(m-dimension)]=1 #Reemplaza la esquina con 1
            for i in range (0,(n-dimension)): #Reemplaza la ultima columna disponible por 1's
                M_trans[i][(m-dimension)]=1
            for j in range (0,(m-dimension)): #Reemplaza la ultima fila disponible por 1's
                M_trans[(n-dimension)][j]=1
            for k in range (0,(m-dimension)): #Reemplaza los que tienen 1´s adyacentes por 1´s
                for l in range (0,(n-dimension)):
                    if (M_previo[l+1][k]==1 or M_previo[l][k+1]==1 or M_previo[l+1][k+1]==1):
                        M_trans[l][k]=1
            if (M_trans==A).all(): #revisa que queden 0´s en la nueva matriz 
                B=(M_previo==np.zeros((n,m)))
                indices = np.where(B == 1)
                return (indices[0][0],indices[1][0],(dimension))
            if (M_trans==A).all():
                break
            else:
                M_previo=M_trans.copy()
        
            
            
            

