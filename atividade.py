# atividade.py

def calcular_media(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return media

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    numeros = []
    while True:
        entrada = input("Digite uma nota (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        try:
            nota = float(entrada)
            numeros.append(nota)
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    if numeros:
        media = calcular_media(numeros)
        situacao = verificar_aprovacao(media)
        print("Média:", media)
        print("Situação:", situacao)
    else:
        print("Nenhuma nota foi inserida.")

if __name__ == '__main__':
    main()
