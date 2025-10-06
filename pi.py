# 1) Importe o módulo (com alias 'rd')
import random as rd

# 2) (Opcional) Fixe a semente para resultados reproduzíveis
rd.seed(123)      # agora rd.random() e rd.uniform() vão gerar a mesma sequência sempre

# 3) Gera um float em [0.0, 1.0)
x1 = rd.random()
print(x1)         # ex: 0.6394267984578837

x = rd.uniform(0, 1)
print(x)         # float entre 0 e 1

##

N = 1_000_000
dentro = 0

for _ in range(N):
    x = rd.random()

    y = rd.random()

    if x*x + y*y <= 1:
        dentro += 1

proporcao = dentro / N
pi_aproximado = 4 * proporcao

print("Proporcao pi/4 =", proporcao)
print("pi =", pi_aproximado)