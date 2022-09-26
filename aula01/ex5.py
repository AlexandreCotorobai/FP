dd = (12 + 6) * 2
anual = dd * 365

print('O elevador percorreu:', anual/1000, 'KMs')

horas = '{:02d}:{:02d}:{:02d}'.format(anual//3600,(anual%3600)//60,(anual%3600)%60)
print(horas)