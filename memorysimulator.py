contagemTrocasFIFO = 0
contagemTrocasMRU = 0
contagemTrocasNUF = 0
contagemTrocasOtimo = 0
def FIFO():
    moldura = []
    nPaginas = []
    sequenciaPags = [1, 2, 7, 2, 3, 2, 2, 3, 4, 2, 1, 3, 1, 4, 5, 5, 6, 1, 3, 2, 6, 7, 7, 7, 8]
    tamanhoMoldura = 4
    global contagemTrocasFIFO
    for j in range(len(sequenciaPags)):
        if tamanhoMoldura == len(moldura):
            if sequenciaPags[j] in moldura:
                pass
            else:
                moldura.pop(0)
                moldura.append(sequenciaPags[j])
                contagemTrocasFIFO += 1
        else:
            if sequenciaPags[j] in moldura:
                pass
            else:
                moldura.append(sequenciaPags[j])
                contagemTrocasFIFO += 1
    print(contagemTrocasFIFO)
    print(moldura)        

def MRU():
    global contagemTrocasMRU

def NUF():
    global contagemTrocasNUF

def otimo():
    global contagemTrocasOtimo

def main():
    pass

FIFO()
