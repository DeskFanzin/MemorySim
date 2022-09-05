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

    for i in range(len(tamanhoMoldura)): ## pega cada um dos tamanhos da moldura
        for j in range(len(sequenciaPags[i])): ## pega cada uma das sequencias de página
            if tamanhoMoldura[i] == len(moldura): ## compara o tamanho da moldura com o tamanho da moldura atual
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
    ## inicio da lógica
        for j in range(len(sequenciaPags[i])):
            if tamanhoMoldura[i] == len(moldura):
                if sequenciaPags[i][j] in moldura:
                    ##adiciona 1 ao tempo de uso da página
                    tempodeUso[sequenciaPags[i][j]] += 1
                else:
                    ##verifica qual página tem o menor tempo de uso e a substitui
                    menor = 0
                    for k in range(len(moldura)):
                        if tempodeUso[moldura[k]] < tempodeUso[moldura[menor]]:
                            menor = k
                    moldura.pop(menor)
                    moldura.append(sequenciaPags[i][j])
                    contagemTrocasMRU += 1
            else:
                if sequenciaPags[i][j] in moldura:
                    tempodeUso[sequenciaPags[i][j]] += 1
                else:
                    moldura.append(sequenciaPags[i][j])
                    contagemTrocasMRU += 1
        moldura.clear()
        print(contagemTrocasMRU)
        contagemTrocasMRU = 0
        tempodeUso.clear()


def NUF():
    global contagemTrocasNUF

def otimo():
    global contagemTrocasOtimo

def main():
    pass

if __name__ == "__main__":
    with open("inMemoria.txt", "r") as arquivo:
        while linha := arquivo.readline():
            linha = linha.split("|")
            sequenciaPags.append(linha[2].split(" ")) ##separa a string em uma lista com os números (sendo estes strings)
            tamanhoMoldura.append(linha[0]) ## adiciona o tamanho da moldura na lista com todos os tamanhos de moldura
            quantPags.append(linha[1]) ## adiciona a quantidade de páginas na lista com todas as quantidades de páginas
        ## transforma em inteiros as listas criadas
        for i in range(len(sequenciaPags)):
            tamanhoMoldura[i] = int(tamanhoMoldura[i])
            quantPags[i] = int(quantPags[i])
            for j in range(len(sequenciaPags[i])):
                sequenciaPags[i][j] = int(sequenciaPags[i][j])
    MRU()
