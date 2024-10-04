# Sistema de Gestão de Notas de Alunos

def adicionar_notas():
    """Função para adicionar notas dos alunos a uma lista."""
    notas = []
    while True:
        nota = input("Digite a nota do aluno (ou 'sair' para finalizar): ")
        if nota.lower() == 'sair':
            break
        try:
            nota_float = float(nota)  # Converte a entrada para float
            if 0 <= nota_float <= 10:  # Valida se a nota está entre 0 e 10
                notas.append(nota_float)  # Adiciona a nota à lista
            else:
                print("Por favor, insira uma nota válida entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'sair'.")

    return notas

def calcular_media(notas):
    """Função para calcular a média das notas."""
    if notas:  # Verifica se a lista não está vazia
        return sum(notas) / len(notas)
    return 0

def determinar_situacao(media):
    """Função para determinar a situação do aluno com base na média."""
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_relatorio(notas, media, situacao):
    """Função para exibir o relatório final."""
    print("\n--- Relatório Final ---")
    print(f"Notas inseridas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

# Função principal
def main():
    """Função principal para executar o sistema."""
    print("Bem-vindo ao Sistema de Gestão de Notas de Alunos!")
    notas = adicionar_notas()  # Adiciona notas
    media = calcular_media(notas)  # Calcula a média
    situacao = determinar_situacao(media)  # Determina a situação
    exibir_relatorio(notas, media, situacao)  # Exibe o relatório

# Executa o sistema
main()
