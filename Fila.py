class Dado:
    #Construtor do Dado
    def __init__(self, valor):
        #Atributos setados com os valores padrões
        self.valor = valor
        self.prox = None
        
class Fila:
    #Construtor da Fila
    def __init__(self):
        #Atributos setados com os valores padrões
        self.inicio = None
        self.fim = None
        self.numeroDeElementos = 0
        
    def enfileirar(self, valor):
        
        novoDado = Dado(valor)
        
        if self.estaVazia() is True:
            self.inicio = self.fim = novoDado
        
        else: 
            self.fim.prox = novoDado
            self.fim = novoDado
        
        self.numeroDeElementos += 1
    
    def desenfileirar(self):
        
        if self.estaVazia() is True:
            print("Fila vazia")
            return None
        
        lixo = self.inicio
        self.inicio = self.inicio.prox
        self.numeroDeElementos -= 1
        return lixo.valor
    
    def tamanho(self):
        
        return self.numeroDeElementos
    
    def estaVazia(self):
        
        if self.fim is None: return True
        
        else: return False
    
    def buscar(self, valor):
        
        if self.estaVazia() is None: return "Fila vazia"
        
        temp = self.inicio
        
        for i in range(self.numeroDeElementos):
            
            if temp.valor == valor: return f"O valor {temp.valor} esta na fila !!"
            
            else:
                i+= 1
                temp = temp.prox
                
        else: return f"O valor {valor} não esta na fila !!"
        
    def mostrarFila(self):
        
        if self.estaVazia() is None: return "Fila vazia"
        
        temp = self.inicio
        
        print("[", end="")
        for i in range(self.numeroDeElementos-1):
            
            print(f"{temp.valor}", end=", ")
            temp = temp.prox
            i+=1
        
        else:
            print(f"{temp.valor}]")