class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        x = len(lista) #se obtiene la longitud de la lista
        for i in range(x//2): #se recorre la mitad de la lista
            lista[i], lista[x-i-1]=lista[x-i-1], lista[i] #se intercambian los elementos
        return lista #se retorna la lista invertida
        pass
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i in range(len(lista)): #se recorre la lista
            if lista[i] == elemento: #se verifica si el elemento en la posición i es igual al elemento buscado
                return i #se retorna la posición del elemento
        return -1 #si no se encuentra el elemento se retorna -1
        pass
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        resultado = [] #se crea una lista vacía
        for item in lista: #se recorre la lista
            if not any(item is x for x in resultado): #se verifica si el elemento no está en la lista resultado
                resultado.append(item) #se agrega el elemento a la lista resultado
        return resultado #se retorna la lista sin duplicados
        pass 
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        i = 0 
        j = 0
        Resultado = [] #se crea una lista vacía
        while i<len(lista1)and j <len(lista2): #se recorren las listas
            if lista1[i]<lista2[j]: #se verifica si el elemento de la lista1 es menor al de la lista2
                Resultado.append(lista1[i]) #se agrega el elemento de la lista1 a la lista resultado
                i +=1 #se aumenta el contador de la lista1
            else:
                Resultado.append(lista2[j]) #se agrega el elemento de la lista2 a la lista resultado
                j+=1 #se aumenta el contador de la lista2
        Resultado.extend(lista1[i:]) #se agregan los elementos restantes de la lista1
        Resultado.extend(lista2[j:]) #se agregan los elementos restantes de la lista2
        return Resultado #se retorna la lista combinada y ordenada
        pass
    
    def rotar_lista(self, lista, k): 
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista: #se verifica si la lista está vacía
            return lista #se retorna la lista vacía
        k = k% len(lista) #se obtiene el residuo de la división de k entre la longitud de la lista
        return lista[-k:]+lista[:-k] #se retorna la lista rotada
        pass
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        v = len(lista)+1 #se obtiene la longitud de la lista
        sum = v*(v+1)//2 #se calcula la suma de los números del 1 al n
        SumaActual = sum(lista) #se calcula la suma de los elementos de la lista
        return sum - SumaActual #se retorna el número faltante
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for i in conjunto1: #se recorre el conjunto1
            if i not in conjunto2: #se verifica si el elemento i no está en el conjunto2
                return False #se retorna False
        return True #si todos los elementos están en el conjunto2 se retorna True
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila= [] #se crea una lista vacía

        def push(x): #se define la función push
            pila.append(x) #se agrega el elemento x a la pila

        def pop(): #se define la función pop
            return pila.pop() if pila else None #se elimina el último elemento de la pila

        def peek(): #se define la función peek
            return pila[-1] if pila else None #se retorna el último elemento de la pila si no está vacía 

        def is_empty(): #se define la función is_empty
            return len(pila) == 0 #se retorna True si la pila está vacía
        return { #se retorna un diccionario con las funciones
        "push": push, 
        "pop": pop, 
        "peek": peek,
        "is_empty": is_empty}
    pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = [] #se crea una lista vacía

        def enqueue(x): #se define la función enqueue
            cola.append(x) #se agrega el elemento x a la cola

        def dequeue(): #se define la función dequeue
            return cola.pop(0) if cola else None #se elimina el primer elemento de la cola

        def peek(): #se define la función peek
            return cola[0] if cola else None #se retorna el primer elemento de la cola si no está vacía

        def is_empty(): #se define la función is_empty
            return len(cola) == 0 #se retorna True si la cola está vacía 

        return { #se retorna un diccionario con las funciones
        "enqueue": enqueue, 
        "dequeue": dequeue,
        "peek": peek,
        "is_empty": is_empty}
    
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        if not matriz or not matriz[0]: #se verifica si la matriz está vacía
            return [] #se retorna una lista vacía
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))] #se retorna la matriz transpuesta
        pass 