contagemTrocasFIFO = 0
contagemTrocasMRU = 0
contagemTrocasNUF = 0
contagemTrocasOtimo = 0
sequenciaPags = []
tamanhoMoldura = []
moldura = []
def FIFO():
    global sequenciaPags
    global tamanhoMoldura
    global moldura
    global contagemTrocasFIFO

    ## abrindo arquivo (tem que fazer funcionar para todas as linhas, e não mudei nada além de deixar algumas variáveis globais)
    with open ("inMemoria.txt", "r") as arquivo:
        arquivo = arquivo.readline()
        arquivo = arquivo.split("|")
        tamanhoMoldura = int(arquivo[0])
        sequenciaPags = arquivo[2].split(" ")
        for i in range(len(sequenciaPags)):
            sequenciaPags[i] = int(sequenciaPags[i])
    ## 
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

def newFIFO():
    global sequenciaPags
    global tamanhoMoldura
    global moldura
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
    ## tentando fazer com que o programa funcione para todas as linhas do arquivo, falta conseguir o tamanhoMoldura e a moldura em si, para cada linha.
    with open("inMemoria.txt", "r") as arquivo:
        while linha := arquivo.readline():
            linha = linha.split("|")
            sequenciaPags.append(linha)
        novaseqpag =[]
        for i in sequenciaPags:
            novaseqpag.append(i[2].replace("\n", ""))
            tamanhoMoldura.append(i[0])
        sequenciaPags = novaseqpag
    FIFO()
