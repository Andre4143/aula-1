quantidade = int(input("Digite a quantidade de números: "))


numeros = [3]

for i in range(quantidade):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

media = sum(numeros) / quantidade


print(f"A média dos números é: {media:.2f}")



