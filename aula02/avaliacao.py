CTP = float(input('Nota da CTP: '))
CP = float(input('Nota da CP: '))
ATPR = 0.0
APR = 0.0

if CP < 6.5 or CTP < 6.5:
    print('Chumbado')
    exit(1)
elif (CTP * 0.36 + CP * 0.64)< 10:
    ATPR = float(input('Nota da ATPR: '))
    APR = float(input('Nota da APR: '))

NF = max(CTP, ATPR) * 0.36 + max(CP, APR) * 0.64

print(NF)
