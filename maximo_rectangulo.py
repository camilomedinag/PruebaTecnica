import numpy as np
def maximo_rectangulo(M):
    M=np.array(M)
    (n,m)=(np.shape(M)) #Dimensión de la matriz 
    c=(M==np.zeros((n,m)))+M*(-(n*m)) #Matriz de penalización
    
    return suma_max(c)
def kadane(vector,inicio, final, n):  
    Sum = 0 #Suma y suma total definidas en 0 para arrancar
    maxSum = 0
    i = None
    final[0] = -1 #determinar inicialmente el final como el último elemento del vector
    inicio_temp= 0 #Variable para mover el inicio de la suma en el vector 
    for i in range(n): 
        Sum += vector[i]  
        if Sum < 0: 
            Sum = 0
            inicio_temp = i + 1
        elif Sum > maxSum: 
            maxSum = Sum
            inicio[0] = inicio_temp  
            final[0] = i 
            
    if final[0] != -1:  
        return maxSum  
    maxSum = vector[0]  #Cuando todos los numeros del vector resultan ser negativos
    inicio[0] = final[0] = 0

    for i in range(1, n): #Revisa que el máximo elemento del vector, no sea mayor a la suma máxima
        if vector[i] > maxSum: 
            maxSum = vector[i]  
            inicio[0] = final[0] = i 
    return maxSum
 
def suma_max(M): 
    (n,m)=(np.shape(M)) #Dimensión de la matriz 
    maxSum, Columna = -1, None
    limite_columna, fila, limite_fila = None, None, None
    izquierda, derecha, i = None, None, None
      
    temp = [None] *n
    Sum = 0
    inicio = [0] 
    final = [0]  

    for izquierda in range(m): 

        temp = [0] *n  

        for derecha in range(izquierda, m): 

            for i in range(n): 
                temp[i] += M[i][derecha]  

            Sum = kadane(temp, inicio, final, n)  
  
            if Sum > maxSum: 
                maxSum = Sum
                Columna = izquierda 
                limite_columna = derecha 
                fila = inicio[0]  
                limite_fila = final[0] 
   
    return (fila,(Columna),(limite_columna-Columna+1),(limite_fila-fila+1))




