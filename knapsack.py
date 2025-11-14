# Problema da Mochila 0/1 usando Programação Dinâmica

def knapsack_01(weights, values, W):
    # Número de itens
    n = len(weights)
    
    # Criando uma tabela DP para armazenar os resultados dos subproblemas
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Preenchendo a tabela DP
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                # Caso o item i seja incluído ou não
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Caso o item i não seja incluído
                dp[i][w] = dp[i - 1][w]
    
    # A última célula da tabela contém a solução ótima
    return dp[n][W]

# Exemplo 1
weights1 = [10, 20, 30]
values1 = [60, 100, 120]
W1 = 50
print(f"Exemplo 1 - O valor máximo que pode ser obtido é: {knapsack_01(weights1, values1, W1)}")

# Exemplo 2
weights2 = [10, 20, 30, 40]
values2 = [50, 70, 80, 90]
W2 = 50
print(f"Exemplo 2 - O valor máximo que pode ser obtido é: {knapsack_01(weights2, values2, W2)}")
