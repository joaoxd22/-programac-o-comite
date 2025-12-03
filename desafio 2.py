class UsuarioNaoEncontrado(Exception):
    pass

class SenhaInvalida(Exception):
    pass


def validar_login(usuario, senha):
    usuarios = {"admin": "123", "joao": "abc"}

    if usuario not in usuarios:
        raise UsuarioNaoEncontrado()

    if senha != usuarios[usuario]:
        raise SenhaInvalida()

    return True


def sistema_login():
    tentativas = 0

    while tentativas < 3:
        user = input("Usuário: ")
        pwd = input("Senha: ")

        try:
            if validar_login(user, pwd):
                print("Login realizado com sucesso!")
                return
        except UsuarioNaoEncontrado:
            print("Erro: usuário não encontrado.")
        except SenhaInvalida:
            print("Erro: senha incorreta.")

        tentativas += 1
        print(f"Tentativas restantes: {3 - tentativas}")

    print("Número de tentativas excedido. Acesso bloqueado.")


def main():
    sistema_login()


main()
