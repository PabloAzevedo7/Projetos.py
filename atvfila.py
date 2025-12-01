from collections import deque

# simulando uma fila por ordem de chegada

fila = deque()
print("adiconando úsuarios a fila")

fila.append("Pablo")
print("fila atual:", list(fila))

fila.append("Pedro")
print("fila atual:", list(fila))

fila.append("Paulo")
print("fila atual:", list(fila))

fila.append("Anny")
print("fila atual:", list(fila))

while fila:
    pessoa = fila.popleft()
    print(f"atendendo: {pessoa}")
    print("fila atual:", list(fila))

print("\nFila vazia! todas as pessoas foram atendidas.")
