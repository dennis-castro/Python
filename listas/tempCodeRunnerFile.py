from time import sleep
par = []
impar = []
lista = []


while True:
    while True:
        try:
            lista.append(int(input('Digite um numero: ')))
            print('\033[32mNumero adicionado com sucesso!!\033[m')