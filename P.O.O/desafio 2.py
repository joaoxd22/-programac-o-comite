# ----------------- EXCEÇÕES PERSONALIZADAS -----------------

class VidaInvalidaError(Exception):
    """Erro lançado quando a vida chega a zero ou menos."""
    pass


# ----------------- CLASSE BASE: PERSONAGEM -----------------

class Personagem:
    def __init__(self, nome, vida, ataque):
        if vida <= 0:
            raise VidaInvalidaError("A vida do personagem deve ser maior que zero.")
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} atacou {inimigo.nome} causando {self.ataque} de dano.")

        if inimigo.vida <= 0:
            raise VidaInvalidaError(f"{inimigo.nome} perdeu toda a vida!")


# ----------------- CLASSES FILHAS -----------------

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=120, ataque=20)


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=35)


# ----------------- FUNÇÃO DE BATALHA -----------------

def batalha(p1, p2):
    print("\n⚔️ INÍCIO DA BATALHA ⚔️")
    print(f"{p1.nome} (Vida: {p1.vida}) VS {p2.nome} (Vida: {p2.vida})\n")

    turno = 1

    while True:
        print(f"----- TURNO {turno} -----")
        try:
            p1.atacar(p2)
            if p2.vida <= 0:
                print(f"\n🏆 {p1.nome} venceu a batalha!")
                break

            p2.atacar(p1)
            if p1.vida <= 0:
                print(f"\n🏆 {p2.nome} venceu a batalha!")
                break

        except VidaInvalidaError as e:
            print(e)
            break

        print(f"Vida de {p1.nome}: {p1.vida}")
        print(f"Vida de {p2.nome}: {p2.vida}\n")

        turno += 1


# ----------------- FUNÇÃO PRINCIPAL -----------------

def main():
    guerreiro = Guerreiro("Arthas")
    mago = Mago("Merlin")

    batalha(guerreiro, mago)


# Executa o programa
main()