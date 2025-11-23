palavras = ["galo", "galinha", "peru", "gavião", "sapo"]
pilha = []
print ("empilhando palavras...")
for p in palavras:
    pilha.append(p)
    print ("pilha atual:", pilha)
print("\ndesempilhando(retirando do topo)...")  
while pilha:
    palavra = pilha.pop()
    print("removido:", palavra)
    print("pilha agora:", pilha)
print("\nTodos os elementos foram removidos. Pilha final:" , pilha) 