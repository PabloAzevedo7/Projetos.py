import time
def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1 
    while inicio <= fim:    
     meio = (inicio + fim) // 2 
     chute = lista[meio]
     if chute == elemento:
        return meio
     elif chute > elemento:
        fim = meio - 1
     else:  
        inicio = meio + 1 
    return - 1       
lista = list(range(0,2048))
busca = 200
inicio = time.perf_counter() 
resultado = busca_binaria(lista, busca) 
fim = time.perf_counter()

if resultado != -1:
   print("Elemento encontrado no indice:", resultado)
   print("Tempo de execução da Busca binária:", fim - inicio, "segundos")
else: 
   print("Elemento não encontrado")   
   print("Tempo de execução da Busca binária:", fim - inicio, "segundos")