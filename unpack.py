
#

# *args: descompactação de lista
# **kwargs: descompactação de dicionário (nome e chave)

# {'chave': valor}

# Objetos de usuário

lista = [2.05, 5.1, 1_000.21]
# Função qualquer
def funcao(x: float, y: float, z = 6):
    return x + y + z


# FOrma 1:
x, y, z = lista
print(funcao(x, y, z))




# **keyargs exemplo

d = {'b' : 2, 'a' : 2, 'c' : 1}

def funcao3(a, b, c = 10):
    return a - b + c

funcao3(**d) # funcao3()

