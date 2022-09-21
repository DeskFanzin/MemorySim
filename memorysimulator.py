resultadosFIFO = []
resultadosMRU = []
resultadosNUF = []
resultadosOtimo = []
sequenciaPags = []
tamanhoMoldura = []
quantPags = []

def FIFO():
    global sequenciaPags
    global tamanhoMoldura
    global resultadosFIFO
    contagemTrocasFIFO = 0
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
        resultadosFIFO.append(contagemTrocasFIFO)
        contagemTrocasFIFO = 0

def MRU():
    global resultadosMRU
    global sequenciaPags
    global tamanhoMoldura
    contagemTrocasMRU = 0
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
                    for k in moldura:
                        tempodeUso[k] += 1
                    tempodeUso[sequenciaPags[i][j]] = 0
                else:
                    tempodeUsoMoldura = {}
                    for k in sorted(moldura):
                        tempodeUsoMoldura[k] = tempodeUso[k]
                    maior = max(tempodeUsoMoldura, key=tempodeUsoMoldura.get)
                    moldura.pop(moldura.index(maior))
                    for k in moldura:
                        tempodeUso[k] += 1
                    moldura.append(sequenciaPags[i][j])
                    tempodeUso[sequenciaPags[i][j]] = 0
                    contagemTrocasMRU += 1
            else:
                if sequenciaPags[i][j] in moldura:
                    for k in moldura:
                        tempodeUso[k] += 1
                    tempodeUso[sequenciaPags[i][j]] = 0
                else:
                    ##aumenta o tempo de cada um na moldura
                    for k in moldura:
                        tempodeUso[k] += 1
                    moldura.append(sequenciaPags[i][j])
                    tempodeUso[sequenciaPags[i][j]] = 0
                    contagemTrocasMRU += 1
        moldura.clear()
        resultadosMRU.append(contagemTrocasMRU)
        contagemTrocasMRU = 0
        tempodeUso.clear()


def NUF():
    global resultadosNUF
    global sequenciaPags
    global tamanhoMoldura
    contagemTrocasNUF = 0
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
                    ##adiciona 1 ao tempo de uso da página para cada pagina na moldura
                    tempodeUso[sequenciaPags[i][j]] += 1
                else:
                    ##verifica qual página tem o menor tempo de uso e a substitui
                    ## O ERRO PROVAVELMENTE TÁ AQUI
                    tempodeUsoMoldura = {}
                    for k in sorted(moldura):
                        tempodeUsoMoldura[k] = tempodeUso[k]
                    menor = min(tempodeUsoMoldura, key=tempodeUsoMoldura.get)
                    moldura.pop(moldura.index(menor))
                    moldura.append(sequenciaPags[i][j])
                    contagemTrocasNUF += 1
            else:
                if sequenciaPags[i][j] in moldura:
                    tempodeUso[sequenciaPags[i][j]] += 1
                else:
                    moldura.append(sequenciaPags[i][j])
                    contagemTrocasNUF += 1
        moldura.clear()
        resultadosNUF.append(contagemTrocasNUF)
        contagemTrocasNUF = 0
        tempodeUso.clear()

def otimo():
    global resultadosOtimo
    global sequenciaPags
    global tamanhoMoldura
    contagemTrocasOtimo = 0
    moldura = []
    ## criando o tempo que será necessario para certa página novamente
    tempoNecessario = {}
    for i in range(len(quantPags)):
        for j in range(1, quantPags[i]+1):
            tempoNecessario[j] = 0 
        sequenciaPagsApagavel = sequenciaPags[i][:]
        for j in range(len(sequenciaPags[i])):
            if tamanhoMoldura[i] == len(moldura):
                if sequenciaPags[i][j] in moldura:
                    sequenciaPagsApagavel.remove(sequenciaPags[i][j])
                    try:
                        tempoNecessario[sequenciaPags[i][j]] = sequenciaPagsApagavel.index(sequenciaPags[i][j])
                    except ValueError:
                        tempoNecessario[sequenciaPags[i][j]] = 100
                else:
                    ## troca o que possui o maior tempo de espera
                    tempoNecessarioMoldura = {}
                    for k in sorted(moldura):
                        try:
                            tempoNecessario[k] = sequenciaPagsApagavel.index(k)
                        except ValueError:
                            tempoNecessario[k] = 100
                        tempoNecessarioMoldura[k] = tempoNecessario[k]
                    maior = max(tempoNecessarioMoldura, key=tempoNecessarioMoldura.get)
                    sequenciaPagsApagavel.remove(sequenciaPags[i][j])
                    moldura.pop(moldura.index(maior))
                    moldura.append(sequenciaPags[i][j])
                    try:
                        tempoNecessario[sequenciaPags[i][j]] = sequenciaPagsApagavel.index(sequenciaPags[i][j])
                    except ValueError:
                        tempoNecessario[sequenciaPags[i][j]] = 100
                    contagemTrocasOtimo += 1

            else:
                if sequenciaPags[i][j] in moldura:
                    sequenciaPagsApagavel.remove(sequenciaPags[i][j])
                    try:
                        tempoNecessario[sequenciaPags[i][j]] = sequenciaPagsApagavel.index(sequenciaPags[i][j])
                    except ValueError:
                        tempoNecessario[sequenciaPags[i][j]] = 100
                else:
                    sequenciaPagsApagavel.remove(sequenciaPags[i][j])
                    moldura.append(sequenciaPags[i][j])
                    try:
                        tempoNecessario[sequenciaPags[i][j]] = sequenciaPagsApagavel.index(sequenciaPags[i][j])
                    except ValueError:
                        tempoNecessario[sequenciaPags[i][j]] = 100
                    contagemTrocasOtimo += 1
        moldura.clear()
        resultadosOtimo.append(contagemTrocasOtimo)
        contagemTrocasOtimo = 0
        tempoNecessario.clear()
def main():
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
    FIFO()
    MRU()
    NUF()
    otimo()
    listaResultados = []
    empate = False
    maisProxOtimo = 0
    for i in range(len(resultadosFIFO)):
        listaResultados.append([resultadosFIFO[i], resultadosMRU[i], resultadosNUF[i]])
        ##acha o resultado mais próximo do ótimo na lista de resultados
        maisProxOtimo = min(listaResultados[i], key=lambda x:abs(x-resultadosOtimo[i]))
        ## acha se tem resultados duplicados
        dup = set()
        duplicados = []
        for x in listaResultados[i]:
            if x in dup:
                duplicados.append(x)
            else:
                dup.add(x)
        try:
            if duplicados[0] == maisProxOtimo:
                empate = True
            else:
                empate = False
        except IndexError:
            empate = False
        
        
        if empate == True:    
            print("{}|{}|{}|{}|empate".format(resultadosFIFO[i], resultadosMRU[i], resultadosNUF[i], resultadosOtimo[i]))
        else:
            if maisProxOtimo == resultadosFIFO[i]:
                print("{}|{}|{}|{}|FIFO".format(resultadosFIFO[i], resultadosMRU[i], resultadosNUF[i], resultadosOtimo[i]))
            elif maisProxOtimo == resultadosMRU[i]:
                print("{}|{}|{}|{}|MRU".format(resultadosFIFO[i], resultadosMRU[i], resultadosNUF[i], resultadosOtimo[i]))
            elif maisProxOtimo == resultadosNUF[i]:
                print("{}|{}|{}|{}|NUF".format(resultadosFIFO[i], resultadosMRU[i], resultadosNUF[i], resultadosOtimo[i]))            
        empate = False
main()