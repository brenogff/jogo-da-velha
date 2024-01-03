import random

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro na tela."""
    print(" ")

    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o jogador atual venceu."""
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def verificar_empate(tabuleiro):
    """Verifica se o jogo terminou em empate."""
    return all(tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))

def realizar_jogada(tabuleiro, jogador, linha, coluna):
    """Realiza a jogada do jogador no tabuleiro."""
    if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        print("Jogada inválida. Tente novamente.")
        return False

def jogar_contra_computador(nome_jogador):
    """Modo de jogo contra o computador."""
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    computador = 'O'
    placar = {nome_jogador: 0, 'Computador': 0}

    while True:
        imprimir_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"Jogador {jogador_atual} ({nome_jogador}) venceu!")
            placar[nome_jogador] += 1
            break
        elif verificar_empate(tabuleiro):
            print("O jogo terminou em empate!")
            break

        if jogador_atual == 'X':
            try:
                linha = int(input("Digite o número da linha (0, 1, 2): "))
                coluna = int(input("Digite o número da coluna (0, 1, 2): "))
                if realizar_jogada(tabuleiro, jogador_atual, linha, coluna):
                    jogador_atual = computador
            except ValueError:
                print("Entrada inválida. Digite um número.")
        else:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
            if realizar_jogada(tabuleiro, jogador_atual, linha, coluna):
                jogador_atual = 'X'

        if verificar_vitoria(tabuleiro, computador):
            imprimir_tabuleiro(tabuleiro)
            print(f"Computador venceu!")
            placar['Computador'] += 1
            break

    return placar

def jogar_dois_jogadores(nome_jogador1, nome_jogador2):
    """Modo de jogo para dois jogadores."""
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    placar = {nome_jogador1: 0, nome_jogador2: 0}

    while True:
        imprimir_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"Jogador {jogador_atual} venceu!")
            placar[jogador_atual] += 1
            break
        elif verificar_empate(tabuleiro):
            print("O jogo terminou em empate!")
            break

        try:
            linha = int(input(f"{jogador_atual}, digite o número da linha (0, 1, 2): "))
            coluna = int(input(f"{jogador_atual}, digite o número da coluna (0, 1, 2): "))
            if realizar_jogada(tabuleiro, jogador_atual, linha, coluna):
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        except ValueError:
            print("Entrada inválida. Digite um número.")

    return placar

def main():
    """Função principal para iniciar o jogo."""
    print("Bem-vindo ao Jogo da Velha!")

    nome_jogador = input("Digite seu nome ou nick: ")

    while True:
        modo_jogo = input("Escolha o modo de jogo (1 - Contra o Computador, 2 - Dois Jogadores): ")

        if modo_jogo == '1':
            placar = jogar_contra_computador(nome_jogador)
        elif modo_jogo == '2':
            nome_jogador2 = input("Digite o nome ou nick do segundo jogador: ")
            placar = jogar_dois_jogadores(nome_jogador, nome_jogador2)
        else:
            print("Escolha inválida. Encerrando o jogo.")
            break

        print("Placar:")
        for jogador, pontos in placar.items():
            print(f"{jogador}: {pontos} ponto(s)")

        jogar_novamente = input("Deseja jogar novamente? (S/N): ")
        if jogar_novamente.upper() != 'S':
            break

if __name__ == "__main__":
    main()
