import datetime

# Data de agora.
data = datetime.datetime.now()
print(data)

print("\n")

# Dia, mês e ano
data2 = datetime.datetime.now()
print(str(data2.day) + "/" + str(data2.month) + "/" + str(data2.year))

print("\n")

# Data específica
nascimento = datetime.datetime(1991, 3, 7)
print(nascimento)

# O dia da semana de nascimento
print(nascimento.strftime("%A"))

# %a = dia da semana resumido
# #A = dia da semana completo
# %w = número do dia da semana
# %d = dia do mês
# %b = texto mês abreviado
# %B = texto mês 
# %m = número do mês
# %y = Ano com dois digitos
# %Y = Ano com 4 digitos
# %H = Hora com dois digitos 00 - 23
# %I = Hora com dois digitos 00 - 12
# %p = indica AM / PM
# %M = Minutos
# %S = Segundos
# %f = microsegundos
# %j = dia do ano 001 - 365
# %W = número da semana do ano

