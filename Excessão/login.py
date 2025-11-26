class SenhaFracaError(Exception):
    pass

def cadastrar_usuario():
    usuario = input("Cadastre um usuário: ")

    while True:
        senha = input("Cadastre uma senha: ")
        confirmar = input("Confirme a senha: ")

        if senha != confirmar:
            print("As senhas não conferem. Tente novamente.")
            continue

        if len(senha) < 6:
            print("Senha fraca. Precisa ter pelo menos 6 caracteres.")
            continue

        break

    with open("usuario.txt", "w") as arq:
        arq.write(f"{usuario}:{senha}")

    print("Usuário cadastrado com sucesso!")

def login():
    while True:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        with open("usuario.txt", "r") as arq:
            dado = arq.read().strip()
            user_salvo, senha_salva = dado.split(":")

        if usuario == user_salvo and senha == senha_salva:
            print("Login realizado!")
            break
        else:
            print("Usuário ou senha incorretos. Tente novamente.\n")

def main():
    cadastrar_usuario()
    login()

main()