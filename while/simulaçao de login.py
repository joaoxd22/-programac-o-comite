usuario_correto = "joao"
senha_correta = 123 

tentativas = 0 
login_bem_sucedido = False

while tentativas < 3:
    print(f"numero de tentativas{tentativas + 1}de 3")
    usuario_digitado = input("digite o usuario")
    senha_digitada = input("digite a senha ")

    if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print("bem vindo!!!")
        login_bem_sucedido = True
        break
    else:
        print("usuario ou senha incorretos. Tente novamente." )

    tentativas += 1

    if not login_bem_sucedido:
        print("acesso bloqueado")


