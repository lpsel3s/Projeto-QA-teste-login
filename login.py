
email_correto = "lucas@email.com"
senha_correta = "Abc123456"

email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

if email == "" and senha == "":
    print("Preencha o email e a senha!")

elif email == "":
    print("Informe seu email!")

elif senha == "":
    print("Informe sua senha!")

elif email == email_correto and senha == senha_correta:
    print("Login realizado com sucesso!")

else:
    print("Email ou senha incorretos!")
