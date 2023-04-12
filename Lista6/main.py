#from minhaPilha import Pilha
from PilhaE import Pilha, PilhaException

pilha1 = Pilha()
pilha1.empilhar(10)
pilha1.empilhar(20)
pilha1.empilhar(30)
pilha1.empilhar(40)
pilha1.empilhar(50)
print("pilha1:", pilha1)
pilha1.desempilha()
print("pilha depois de desempilhar:", pilha1)
pilha1.subTopo()
print("Subtopo da pilha:",pilha1.subTopo())
print("pilha desempilhada:",pilha1.desempilha_n(1))
print(pilha1)
print("Base da pilha:", pilha1.obtemBase())
pilha1.esvazia()
print(pilha1)