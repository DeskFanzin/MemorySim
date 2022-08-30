contagemTrocasFIFO = 0
contagemTrocasMRU = 0
contagemTrocasNUF = 0
contagemTrocasOtimo = 0
sequenciaPags = []
tamanhoMoldura = []

def FIFO(): ##utilize o newFIFO##
    global sequenciaPags
    global tamanhoMoldura
    global contagemTrocasFIFO
    moldura = []
    ## abrindo arquivo (tem que fazer funcionar para todas as linhas, e não mudei nada além de deixar algumas variáveis globais)
    with open ("teste.txt", "r") as arquivo:
        arquivo = arquivo.readline()
        arquivo = arquivo.split("|")
        tamanhoMoldura = int(arquivo[0])
        sequenciaPags = arquivo[2].split(" ")
        for i in range(len(sequenciaPags)):
            sequenciaPags[i] = int(sequenciaPags[i])
        print(sequenciaPags)
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
    global contagemTrocasFIFO
    global sequenciaPags
    global tamanhoMoldura
    moldura = []

    for i in range(len(tamanhoMoldura)):
        tamanhoMoldura[i] = int(tamanhoMoldura[i]) ## transforma em inteiro cada um dos tamanhos da moldura
        for j in range(len(sequenciaPags[i])):
            if tamanhoMoldura[i] == len(moldura):
                if sequenciaPags[i][j] in moldura:
                    pass
                else:
                    moldura.pop(0)
                    moldura.append(sequenciaPags[i][j])
                    contagemTrocasFIFO += 1
            else:
                if sequenciaPags[i][j] in moldura:
                    pass
                else:
                    moldura.append(sequenciaPags[i][j])
                    contagemTrocasFIFO += 1
        moldura.clear()
        print(contagemTrocasFIFO)
        contagemTrocasFIFO = 0
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
            sequenciaPags.append(linha[2].split(" ")) ##separa a string em uma lista com os números (sendo estes strings)
            tamanhoMoldura.append(linha[0])
        ## transforma em inteiros a sequencia de paginas
        for i in range(len(sequenciaPags)):
            for j in range(len(sequenciaPags[i])):
                sequenciaPags[i][j] = int(sequenciaPags[i][j])
        newFIFO()