
def MRU():
    contagemTrocasMRU = 0
    sequenciaPags = [1, 2, 2, 2, 3, 4, 3, 4, 5, 5, 6, 1, 3, 2, 6, 7, 7, 7, 8]
    tamanhoMoldura = 3
    quantPags = 8
    moldura = []
    tempodeUso = {}
    ##criando a lista com o tempo sem uso de cada página
    for j in range(1, quantPags+1):
        tempodeUso[j] = 0
## inicio da lógica
    for j in range(len(sequenciaPags)):
        if tamanhoMoldura == len(moldura):
            if sequenciaPags[j] in moldura:
                ##adiciona 1 ao tempo de uso da página para cada pagina na moldura
                tempodeUso[sequenciaPags[j]] += 1
            else:
                ##verifica qual página tem o menor tempo de uso e a substitui
                ## O ERRO PROVAVELMENTE TÁ AQUI
                tempodeUsoMoldura = {}
                for k in sorted(moldura):
                    tempodeUsoMoldura[k] = tempodeUso[k]
                menor = min(tempodeUsoMoldura, key=tempodeUsoMoldura.get)
                moldura.pop(moldura.index(menor))
                moldura.append(sequenciaPags[j])
                contagemTrocasMRU += 1
        else:
            if sequenciaPags[j] in moldura:
                tempodeUso[sequenciaPags[j]] += 1
            else:
                moldura.append(sequenciaPags[j])
                contagemTrocasMRU += 1
    moldura.clear()
    print(contagemTrocasMRU)
    contagemTrocasMRU = 0
    tempodeUso.clear()

MRU()