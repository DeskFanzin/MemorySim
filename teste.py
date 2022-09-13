##no MRU, sempre haverá um que está a mais tempo sem ser chamado.
def MRU():
    contagemTrocasMRU = 0
    ##sequenciaPags = [10, 23, 15, 1, 27, 25, 5, 12, 10, 4, 20, 4, 13, 22, 24, 2, 17, 16, 8, 15, 9, 23, 9, 9, 14, 14, 16, 26, 16, 2, 10, 21, 22, 14, 7, 11, 4, 26, 14, 24, 16, 5, 6, 23, 15, 15, 3, 9, 23, 15, 26, 23, 3, 4, 22, 5, 4, 10, 14, 19, 24, 26, 8, 17, 21, 17, 10, 13, 21, 11, 17, 6, 9, 27, 2, 8, 17, 4, 14, 12, 2]
    sequenciaPags = [1, 2, 3, 4, 5, 6, 3, 4, 4, 5, 4, 3, 3, 4, 5, 6, 3, 4, 1, 7, 8]
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
                for k in moldura:
                    if k != sequenciaPags[j]:
                        tempodeUso[k] += 1
            else:
                ##verifica qual página tem o menor tempo de uso e a substitui
                tempodeUsoMoldura = {}
                for k in sorted(moldura):
                    tempodeUsoMoldura[k] = tempodeUso[k]
                menor = min(tempodeUsoMoldura, key=tempodeUsoMoldura.get)
                print(tempodeUsoMoldura)
                moldura.pop(moldura.index(menor))
                moldura.append(sequenciaPags[j])
                for k in moldura:
                    if k != sequenciaPags[j]:
                        tempodeUso[k] += 1
                contagemTrocasMRU += 1
        else:
            if sequenciaPags[j] in moldura:
                for k in moldura:
                    if k != sequenciaPags[j]:
                        tempodeUso[k] += 1
            else:
                for k in moldura:
                    tempodeUso[k] += 1
                moldura.append(sequenciaPags[j])
                contagemTrocasMRU += 1
    moldura.clear()
    print(contagemTrocasMRU)
    contagemTrocasMRU = 0
    tempodeUso.clear()

MRU()