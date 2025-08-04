# PARTE 1

curso = "Curso de Python"

# print(curso[9:15]) "mostrar na tela da posição de 9 a 15"
# print(curso.strip()) "Retira os espaços em excesso"
# print(curso.lower().strip()) "caracteres em diminutivo"
# print(curso.upper()) "caracteres aumentativo"
# print(curso.replace("Python", "P")) "Substitui caracteres."

# a = curso.split(" ") # vai separar cadeias de caracteres atravez do espaço.

# print(a[2])
# print("Tamanho: " + str(len(curso)))

# PARTE 2

# exemplo = "internet"

# res = curso + " adiquirido da " + exemplo

# print(res)

cidade = "Belo Horizonte"
dia = 15
mes = "Janeiro"
ano = 2025
curso2 = "curso de Python"

data = "{}, {} de {} de {} \n \"{}\""

print(data.format(cidade, dia, mes, ano, curso2))