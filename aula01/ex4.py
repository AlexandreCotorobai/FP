tempo = int(input('Tempo? '))
horas = tempo//3600
minutos = (tempo - (horas * 3600))//60
segundos = tempo - (horas * 3600) - (minutos * 60)

print("{:02d}:{:02d}:{:02d}".format(horas,minutos,segundos))