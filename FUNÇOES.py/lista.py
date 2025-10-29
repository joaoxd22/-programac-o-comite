def somar_lista_for(lista):
  soma = 0
  for elemento in lista:
    soma += elemento
  return soma
def somar_lista_sum(lista):
  return sum(lista)
minha_lista = [10, 20, 30, 40]


soma_for = somar_lista_for(minha_lista)
print(f"Soma (loop for): {soma_for}")


soma_builtin = somar_lista_sum(minha_lista)
print(f"Soma (sum()): {soma_builtin}") 
