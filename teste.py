##no MRU, sempre haverá um que está a mais tempo sem ser chamado.
def MRU():
    contagemTrocasOtimo = 0
    ##sequenciaPags = [10, 23, 15, 1, 27, 25, 5, 12, 10, 4, 20, 4, 13, 22, 24, 2, 17, 16, 8, 15, 9, 23, 9, 9, 14, 14, 16, 26, 16, 2, 10, 21, 22, 14, 7, 11, 4, 26, 14, 24, 16, 5, 6, 23, 15, 15, 3, 9, 23, 15, 26, 23, 3, 4, 22, 5, 4, 10, 14, 19, 24, 26, 8, 17, 21, 17, 10, 13, 21, 11, 17, 6, 9, 27, 2, 8, 17, 4, 14, 12, 2]
    ##sequenciaPags = [1, 2, 3, 4, 5, 6, 3, 4, 4, 5, 4, 3, 3, 4, 5, 6, 3, 4, 1, 7, 8]
    sequenciaPags = [1, 2, 2, 2, 3, 4, 3, 4, 5, 5, 6, 1, 3, 2, 6, 7, 7, 7, 8]
    tamanhoMoldura = 3
    quantPags = 8
    moldura = []
    tempoNecessario = {}
    ##criando a lista com o tempo sem uso de cada página
    for j in range(1, quantPags+1):
        tempoNecessario[j] = 0
    sequenciaPagsApagavel = sequenciaPags[:]
    for j in range(len(sequenciaPags)):
        print(sequenciaPagsApagavel)
        if tamanhoMoldura == len(moldura):
            if sequenciaPags[j] in moldura:
                sequenciaPagsApagavel.remove(sequenciaPags[j])
                try:
                    tempoNecessario[sequenciaPags[j]] = sequenciaPagsApagavel.index(sequenciaPags[j])
                except ValueError:
                    tempoNecessario[sequenciaPags[j]] = 100
            else:
                ## troca o que possui o maior tempo de espera
                tempoNecessarioMoldura = {}
                for k in sorted(moldura):
                    try:
                        tempoNecessario[k] = sequenciaPagsApagavel.index(k)
                        print(k)
                    except ValueError:
                        tempoNecessario[k] = 100
                    tempoNecessarioMoldura[k] = tempoNecessario[k]
                maior = max(tempoNecessarioMoldura, key=tempoNecessarioMoldura.get)
                print(tempoNecessarioMoldura)
                print("Maior: ", maior)
                sequenciaPagsApagavel.remove(sequenciaPags[j])
                moldura.pop(moldura.index(maior))
                moldura.append(sequenciaPags[j])
                try:
                    tempoNecessario[sequenciaPags[j]] = sequenciaPagsApagavel.index(sequenciaPags[j])
                except ValueError:
                    tempoNecessario[sequenciaPags[j]] = 100
                contagemTrocasOtimo += 1

        else:
            if sequenciaPags[j] in moldura:
                sequenciaPagsApagavel.remove(sequenciaPags[j])
                try:
                    tempoNecessario[sequenciaPags[j]] = sequenciaPagsApagavel.index(sequenciaPags[j])
                except ValueError:
                    tempoNecessario[sequenciaPags[j]] = 100
            else:
                sequenciaPagsApagavel.remove(sequenciaPags[j])
                moldura.append(sequenciaPags[j])
                try:
                    tempoNecessario[sequenciaPags[j]] = sequenciaPagsApagavel.index(sequenciaPags[j])
                except ValueError:
                    tempoNecessario[sequenciaPags[j]] = 100
                contagemTrocasOtimo += 1
    moldura.clear()
    print(contagemTrocasOtimo)
    contagemTrocasOtimo = 0
    tempoNecessario.clear()

MRU()