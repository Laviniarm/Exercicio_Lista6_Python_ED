class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class No:
    def __init__(self, carga: any):
        self.__carga = carga
        self.__prox = None
    
    def getCarga(self):
        return self.__carga
    
    def getProximo(self)->'No':
        return self.__prox
    
    def setProximo(self, novoProx:'No'):
        self.__prox = novoProx
    
    def temProximo(self)->bool:
        return self.__prox == None

    def __str__(self):
        return f'{self.__carga}'

class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tam = 0
    
    def estaVazia(self)-> bool:
        return self.__topo == None
    
    def tamanho(self) -> int:
        return self.__tam
    
    def __len__(self):
        return self.__tam
    
    def elemento(self, posicao:int)->any:
        if posicao <= 0 or posicao > self.tamanho():
            raise PilhaException(f"Posicao invalida. A pilha so tem {self.__tam} elementos.")
        
        contador = 1 
        cursor = self.__topo
        while(cursor != None):
            if contador == posicao:
                return cursor.getCarga()
            cursor = cursor.getProximo()
            contador += 1
        
                
    def busca(self, key:any)->int:
        contador = 1
        cursor = self.__topo
        while(cursor != None):
            if key == cursor.getCarga():
                return contador
            cursor = cursor.getProximo()
            contador += 1

        raise PilhaException(f"A chave {key} não está na pilha.")
    
    def empilhar(self, carga:any):
        no = No(carga)
        no.setProximo(self.__topo)
        self.__topo = no
        self.__tam += 1

    def desempilha(self):
        if self.__topo is None:
            raise PilhaException('Não há elementos para remoção. Pilha Vazia')
        carga = self.__topo.getCarga()
        self.__topo = self.__topo.getProximo()
        self.__tam -= 1
        return carga
    
    def topo(self):
        if self.__topo is None:
            raise PilhaException("Pilha Vazia")
        return self.__topo.getCarga
   
    def imprime(self):
        print(self.__str__())
        
    def __str__(self)->str:
        s = 'topo->[ '
        cursor = self.__topo
        while(cursor != None):
            s += f'{cursor.getCarga()}'
            if cursor.getProximo() is not None:
                s+= ', '
            cursor = cursor.getProximo()
        return s + "]"

    def subTopo(self):
        if self.__topo.getProximo() == None:
            raise PilhaException("A pilha não tem subtopo")
        else:
            return self.__topo.getProximo().getCarga()

    def desempilha_n( self, n:int)-> bool:
        if(self.tamanho() <= n):
            return False
        
        for i in range(n):
            self.desempilha()

        return True

    def esvazia(self):
        while self.__topo != None:
            self.desempilha()

    def obtemBase(self):
        if self.estaVazia():
            raise PilhaException(" A pilha está vazia") 
        
        cursor = self.__topo
        while(cursor.getProximo() != None):   
            cursor = cursor.getProximo()
        return cursor.getCarga()