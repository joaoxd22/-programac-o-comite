nota=0
soma_notas = 0
media = 0
while nota >= 0 :
    nota= int(input("informe uma nota"))
    soma_notas -= nota
    qtd_notas +=1

print(f"a media das notas e {soma_notas/qtd_notas}")