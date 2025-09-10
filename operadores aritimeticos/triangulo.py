lado_1 = int(input("me informe o valor do primeiro lado do triangulo "))
lado_2 = int(input("me informe o valor do segundo lado do triangulo "))
lado_3 = int(input("me informe o valor do terceiro lado lado do triangulo "))
if lado_1 + lado_2 > lado_3:
    print("a soma dos dois lados é amior que o terceiro lado")
else:
    print("A SOMA DOS DOIS LADOS NAO E MAIOR QUE O TERCEIRO")
if lado_1 == lado_2 == lado_3:
    print("seu triangulo e equilatero")
else:
    print("seu triangulo nao é equilatero")
if lado_1 == lado_2 != lado_3 :
    print("seu triangulo é isosceles")
else:
    print("nao e isosceles")
if lado_1 != lado_2 != lado_3:
    print(" seu triangulo é escaleno ")
else:
    print("seu triangulo nao é escaleno  ")