import numpy as np
def iterador_celdas_libres(M,i,j):
    M=np.array(M) #convierte en array
    (n,m)=np.shape(M) #Dimensiones de la matriz 
    if celda_libre(M,i,j)==False: #Determina si la celda dada es libre o no lo es 
        return False
    posicion=[(i,j)] #Posición de la celda libre inicial
    ind_posicion=iter(posicion) #Iterador sobre las posiciones 
    len(posicion)
    c=0
    while c<len(posicion): #Evita error de StopIteration
        (k,l)=(next(ind_posicion))
        izquierda=max(0,l-1)
        derecha=min(l+1,m-1)
        arriba=max(0,k-1)
        abajo=min(k+1,n-1)
        if celda_libre(M,k,izquierda)==True and ((k,izquierda)) not in posicion: #Revisa que la celda indicada sea libre y no este en el iterador
            posicion.append((k,izquierda))
        if celda_libre(M,k,derecha)==True and ((k,derecha)) not in posicion:
            posicion.append((k,derecha))
        if celda_libre(M,arriba,l)==True and ((arriba,l)) not in posicion:
            posicion.append((arriba,l))
        if celda_libre(M,abajo,l)==True and ((abajo,l)) not in posicion:
            posicion.append((arriba,l))
        if celda_libre(M,arriba,derecha)==True and ((arriba,derecha)) not in posicion:
            posicion.append((arriba,derecha))
        if celda_libre(M,arriba,izquierda)==True and ((arriba,izquierda)) not in posicion:
            posicion.append((arriba,izquierda))
        if celda_libre(M,abajo,derecha)==True and ((abajo,derecha)) not in posicion:
            posicion.append((abajo,derecha))
        if celda_libre(M,abajo,izquierda)==True and ((abajo,izquierda)) not in posicion:
            posicion.append((abajo,izquierda))
        c+=1
    return posicion
    
    
    
def celda_libre(M,i,j):
    M=np.array(M) #convierte en array
    (n,m)=np.shape(M)
    izquierda=max(0,j-1) #Evita errores de indices en los bordes de la matriz
    derecha=min(j+1,m-1)
    arriba=max(0,i-1)
    abajo=min(i+1,n-1)
    if M[i][j]==1:
        return False
    elif (M[i][izquierda]==1 or M[i][derecha]==1 or M[abajo][j]==1 or M[arriba][j]==1
          or M[arriba][derecha]==1 or M[arriba][izquierda]==1 or M[abajo][derecha]==1 or M[abajo][izquierda]==1):
        return False
    else:
        return True 
    
           