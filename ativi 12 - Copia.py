# Definição de credenciais fixas
USERNAME_CORRETO = "admin"
SENHA_CORRETA = "1234"

# Solicita ao usuário que insira nome de usuário e senha
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

# Verifica se as credenciais estão corretas
if usuario == USERNAME_CORRETO and senha == SENHA_CORRETA:
    print("Login bem-sucedido! Bem-vindo.")
else:
    print("Nome de usuário ou senha incorretos. Tente novamente.")
