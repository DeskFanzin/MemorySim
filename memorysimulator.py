from ast import Index


contagemTrocasFIFO = 0
contagemTrocasMRU = 0
contagemTrocasNUF = 0
contagemTrocasOtimo = 0
sequenciaPags = []
tamanhoMoldura = []
quantPags = []

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
    global sequenciaPags
    global tamanhoMoldura
    moldura = []
    tempodeUso = {}
    ##criando a lista com o tempo sem uso de cada página
    for i in range(len(quantPags)):
        for j in range(1, quantPags[i]+1):
            tempodeUso[j] = 0
        print(tempodeUso)
        tempodeUso.clear()
    ## inicio da lógica
    '''for i in range(len(tamanhoMoldura)):
        for j in range(len(sequenciaPags[i])):
            if tamanhoMoldura[i] == len(moldura):
                if sequenciaPags[i][j] in moldura:
                    ##adiciona 1 ao tempo de uso da página
                    tempodeUso[moldura.index(sequenciaPags[i][j])] += 1
                else:
                    try:
                        moldura.pop(tempodeUso.index(min(tempodeUso)))
                    except:
                        pass
                    moldura.append(sequenciaPags[i][j])
                    contagemTrocasMRU += 1
            else:
                if sequenciaPags[i][j] in moldura:
                    try:
                        tempodeUso[moldura.index(sequenciaPags[i][j])] += 1
                    except IndexError:
                        pass
                else:
                    moldura.append(sequenciaPags[i][j])
                    contagemTrocasMRU += 1
        moldura.clear()
        print(contagemTrocasMRU)
        contagemTrocasMRU = 0
        tempodeUso.clear()'''
    print(tempodeUso)
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
            quantPags.append(linha[1])
        ## transforma em inteiros a sequencia de paginas e o tamanho da moldura
        for i in range(len(sequenciaPags)):
            tamanhoMoldura[i] = int(tamanhoMoldura[i])
            quantPags[i] = int(quantPags[i])
            for j in range(len(sequenciaPags[i])):
                sequenciaPags[i][j] = int(sequenciaPags[i][j])
        MRU()