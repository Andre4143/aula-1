preco = float(input('Digite o preço do produto: R$')) 
desconto = preco * 0.05 
nvpreco = preco - desconto 
print(f"O produto com desconto de 5% é: R${nvpreco:.2f}") 