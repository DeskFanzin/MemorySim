contagemTrocasFIFO = 0
contagemTrocasMRU = 0
contagemTrocasNUF = 0
contagemTrocasOtimo = 0
def FIFO():
    moldura = []
    nPaginas = []
    sequenciaPags = []
    tamanhoMoldura = 0
    ## abrindo arquivo (tem que fazer funcionar para todas as linhas)
    with open ("inMemoria.txt", "r") as arquivo:
        arquivo = arquivo.readline()
        arquivo = arquivo.split("|")
        tamanhoMoldura = int(arquivo[0])
        sequenciaPags = arquivo[2].split(" ")
        for i in range(len(sequenciaPags)):
            sequenciaPags[i] = int(sequenciaPags[i])
    ## 
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

if __name__ == "__main__":
    FIFO()
