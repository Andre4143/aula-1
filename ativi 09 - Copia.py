num1 = int(input("digite um numero :"))
num2 = int(input("digite o segundo numero :"))

if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    if num2 != 0: 
        resultado = num1 / num2
    else:
        resultado = "Erro: Não é possível dividir por zero!"
else:
    resultado = "Operação inválida!"


print("Resultado:", resultado)