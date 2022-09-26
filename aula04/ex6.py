
def leibnizPi4(termos):
    sum = 0
    for i in range(termos):
        x = ((-1)**i) / (2*i + 1)
        sum = sum + x
    return sum

print(leibnizPi4(3))
