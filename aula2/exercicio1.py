class ContaCorrente: 
    def __init__(self,valor): 
        self.valor = valor
        
    def tranferir(self, destino):
        transferido = float(input('quanto deseja tranferir?'))
        self.valor -= transferido
        destino.valor += transferido
        print(f'voce transferiu {transferido} para {destino}')
    
conta1 = ContaCorrente(1000)    
conta2 = ContaCorrente(0)

print(conta1.valor)
print(conta2.valor)

conta1.tranferir(conta2)

print(conta1.valor)
print(conta2.valor)

    
