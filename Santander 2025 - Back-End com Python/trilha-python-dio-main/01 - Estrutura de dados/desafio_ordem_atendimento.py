pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
ordenado_por_idade = sorted(pacientes, key=lambda x: x[1], reverse=True)
lista_urgente = ""
lista_idade = ""
lista_normal = ""
for paciente in ordenado_por_idade:
  if paciente[2] == "urgente":
    lista_urgente = lista_urgente + paciente[0] + ", "
  elif paciente[1] > 60:
    lista_idade = lista_idade + paciente[0] + ", "
  else:
    lista_normal = lista_normal + paciente[0] + ", "
    
lista_normal = lista_normal[:-2]
# TODO: Exiba a ordem de atendimento com título e vírgulas:
print(f"Ordem de Atendimento: {lista_urgente} {lista_idade} {lista_normal}")