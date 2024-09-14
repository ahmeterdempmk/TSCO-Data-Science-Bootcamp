liste = [1, 2, 1, 3, 4, 5]
tekrarVarMi = False

for i in range(0, len(liste) - 1):
    for j in range(i+1, len(liste)):
        if liste[i] == liste[j]:
            tekrarVarMi = True
            break
    if tekrarVarMi:
        break

if tekrarVarMi:
    print("Listede tekrar vardır.")
else:
    print("Listede tekrar yoktur.")