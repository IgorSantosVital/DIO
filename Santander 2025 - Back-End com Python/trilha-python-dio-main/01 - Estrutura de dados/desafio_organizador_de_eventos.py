# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    entrada = input()
    nome, temaEvento = map(str.strip, entrada.split(','))

    if temaEvento not in eventos:
        eventos[temaEvento] = []
    eventos[temaEvento].append(nome)



# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")