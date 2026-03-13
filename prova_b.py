"""
PROVA B - Fundamentos de Python para IA
Duração: 90 minutos | Valor Total: 100 pontos

Instruções:
- Preencha as funções abaixo implementando a lógica solicitada.
- Você é responsável por testar o seu próprio código. Sinta-se à vontade para 
  criar chamadas de teste no final do arquivo para garantir que a lógica funciona.
- Quando terminar, faça o commit e o push para o repositório.
"""

# ==============================================================================
# Questão 1: Manipulação de Dicionário (20 pontos)
# ==============================================================================
# Dado um dicionário onde as chaves são nomes de alunos e os valores são as suas notas,
# retorne um NOVO dicionário contendo apenas os alunos aprovados (nota >= 7.0).
def filtrar_aprovados(notas):
    alunos = {"Renato": 10.0, "Leite": 6.0, "Dudi": 7.2}

    aprovados = {}

    for nome, nota in alunos:
        if nota >= 7.0:
            aprovados(nome) == nota

    print(aprovados)

# ==============================================================================
# Questão 2: Funções Lambda e Sorted (20 pontos)
# ==============================================================================
# Tem uma lista de produtos representada por tuplas, ex: ("Teclado", 150). 
# Use a função `sorted` com uma função `lambda` para retornar essa lista 
# ordenada pelo preço (o segundo elemento da tupla) em ordem crescente.
def ordenar_por_preco(produtos):
    produtos = {1: ("Teclado", 200), 2: ("Mouse", 150), 3: ("Monitor", 1000)}
    return sorted(produtos, key=lambda produto: produto[1, 2, 3])

# ==============================================================================
# Questão 3: Funções Lambda e Map (20 pontos)
# ==============================================================================
# Dada uma lista de temperaturas em Celsius, use `map` e `lambda` para retornar 
# uma nova lista com as temperaturas convertidas para Fahrenheit.
# Fórmula: F = (C * 9/5) + 32
def converter_para_fahrenheit(temperaturas_celsius):
    c = temperaturas_celsius
    return list(map(lambda c: (c * 9/5) + 32, temperaturas_celsius))

# ==============================================================================
# Questão 4: Recursão (20 pontos)
# ==============================================================================
# Crie uma função recursiva que realize a divisão inteira entre dois números 
# positivos (numerador e denominador) utilizando APENAS subtrações sucessivas.
# ATENÇÃO: É proibido utilizar os operadores de divisão clássicos (/ ou //).
#
# Dica: O caso base ocorre quando o numerador for menor que o denominador (retorna 0).
# O passo recursivo subtrai o denominador do numerador e soma 1 ao resultado 
# da chamada recursiva.
def divisao_recursiva(numerador, denominador):
    if numerador < denominador:
        return 0
    
    return 1 + divisao_recursiva(numerador - denominador, denominador)

# ==============================================================================
# Questão 5: Teoria aplicada à IA (20 pontos)
# ==============================================================================
# "O conceito de Mutabilidade é fundamental em Python, especialmente ao lidar 
# com grandes volumes de dados (Listas, Tuplas, Dicionários). 
# Explique a diferença entre estruturas de dados mutáveis e imutáveis em Python. 
# Dê um exemplo de um problema que pode ocorrer se passarmos uma lista mutável 
# como argumento padrão numa função de pré-processamento de dados."

RESPOSTA_Q5 = """
#As estruturas mutáveis no python podem ser alteradas depois de serem feitas, como listas e dicionários.
#Já estruturas imutáveis não podem ser modificadas, como tuplas, strings e números.
#Ela pode ser modificada e prejudicar o código, por exemplo.
"""
if __name__ == "__main__":
    # Área livre para testes locais do aluno.
    # Exemplo de teste esperado para a Questão 4:
    # print(divisao_recursiva(20, 5)) # Deve imprimir 4
    # print(divisao_recursiva(17, 5)) # Deve imprimir 3
    print(filtrar_aprovados())
    print(ordenar_por_preco())
    print(converter_para_fahrenheit())
    print(divisao_recursiva())
