#tabela hash com 3 posições 
tabela = [[], [], []]

#função hash simples
def funcao_hash(chave):
    return len(chave) % 3

def inserir(chave):
    indice = funcao_hash(chave)
    tabela[indice].append(chave)
    print(f"'{chave}' foi para o indice {indice}")

# lista com várias palavras
palavras = ["maça", "casa", "galo", "uva", "sol", "lua", "Pablo", "sapato"]

for p in palavras:
    inserir(p)

print("\ntabela final com colisões:")
print(tabela)
